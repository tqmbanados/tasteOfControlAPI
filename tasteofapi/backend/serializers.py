from rest_framework import serializers

from .models import FullScore, Instrument, Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('action', 'stage',)


class FullScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullScore
        fields = ('score_data',)


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ('score_data', 'instrument', 'duration')
