from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


## Rooms
class Room(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=50, default="ROOM NAME")
    desc = models.CharField(max_length=500, default="ROOM DESCRIPTION")
    #items = models.CharField(max_length=500, default=" ")
    #map = models.IntegerField(max_length=500, default=" ")
    NORTH = models.CharField(max_length=150, blank=True)
    SOUTH = models.CharField(max_length=150, blank=True)
    EAST = models.CharField(max_length=150, blank=True)
    WEST = models.CharField(max_length=150, blank=True)
    map = ArrayField(ArrayField(models.IntegerField(
        null=True, blank=True), null=True, blank=True), blank=True,)

    def __str__(self):
        return self.name

    # create function to connect rooms

    def rm_connects(self, destination, heading):
        destinationID = destination.id
        reverse_dirs = {"NORTH": "SOUTH", "SOUTH": "NORTH",
                        "EAST": "WEST", "WEST": "EAST"}
        reverse_dir = reverse_dirs[heading]
        setattr(self, f"{heading}_to", destinationID)
        setattr(destination, f"{reverse_dir}_to", self.id)
        self.save()

    # # fn to create player naming/id
    # def player_handle(self, active_playerID):
    #     return[p.user.username for p in Player.objects.filter(rm_current=self.id) if p.id != int(active_playerID)]

    # # fn to create player uuid
    # def playerUUID(self, active_playerID):
    #     return[p.uuid for p in Player.objects.filter(rm_current=self.id) if p.id != int(active_playerID)]

## Extended User
class Player(AbstractUser):
    
    rm_current = models.IntegerField(default=0)
    

    # create fn to initialize

    def init(self):
        if self.rm_current == 0:
            self.rm_current == Room.objects.first().id
            self.x = Room.objects.first().x
            self.y = Room.objects.first().y
            self.save()

    def room(self):
        try:
            return Room.objects.get(id=self.rm_current)
        except Room.DoesNotExist:
            self.init()
            return self.room()


@receiver(post_save, sender=Player)
# fn to create player
def create_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(player=instance)
        Token.objects.create(player=instance)


@receiver(post_save, sender=Player)
def save_player(sender, instance, **kwargs):
    instance.Player.save()
