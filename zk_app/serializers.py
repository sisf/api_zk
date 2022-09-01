from rest_framework import serializers
from zk_app.models import Gust,Movie,Reservation

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class GustSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gust
        fields = ['pk', 'reservation', 'name', 'mobile']