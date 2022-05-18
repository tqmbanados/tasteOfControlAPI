from rest_framework import serializers

from .models import FullScore, Instrument, Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('action', 'stage', 'number')


class FullScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullScore
        fields = ('score_data',)


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ('score_data', 'instrument', 'duration', 'measure')


class ImageSerializer(serializers.ModelSerializer):
    image_data = serializers.ImageField(max_length=64, allow_empty_file=False, allow_null=False,
                                        use_url=True, required=False)

    class Meta:
        model = Instrument
        fields = ('image_data', 'instrument', 'duration', 'measure')
