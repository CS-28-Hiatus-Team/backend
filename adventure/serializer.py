from rest_framework import serializers


class RoomSerializer(serializers.Serializer):
    id = serializers.AutoField(primary_key=True)
    name = serializers.CharField(max_length=50, default="DEFAULT TITLE")
    description = serializers.CharField(
        max_length=500, default="DEFAULT DESCRIPTION")
    n_to = serializers.CharField(max_length=1)
    s_to = serializers.CharField(max_length=1)
    e_to = serializers.CharField(max_length=1)
    w_to = serializers.CharField(max_length=1)
    x = serializers.IntegerField(default=0)
    y = serializers.IntegerField(default=0)
