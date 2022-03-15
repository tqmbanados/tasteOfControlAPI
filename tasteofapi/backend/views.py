from django.shortcuts import render
from .models import FullScore, Actor, Instrument
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import FullScoreSerializer, ActorSerializer, InstrumentSerializer


class MainScoreView(ModelViewSet):
    queryset = FullScore.objects.all()
    serializer_class = FullScoreSerializer

    def get(self, request):
        score_model = self.queryset[0]
        data = {'score_data': score_model.score_data}

        return Response(data, status=status.HTTP_200_OK)

    def put(self, request):
        score_model = self.queryset[0]
        serializer = FullScoreSerializer(score_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(score_model.score_data, status=status.HTTP_200_OK)
        return Response(score_model.score_data, status=status.HTTP_400_BAD_REQUEST)


class InstrumentView(ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer

    def get(self, request):
        instrument_name = request.get('instrument')
        instrument = self.queryset.filter(instrument=instrument_name)[0]
        data = {'instrument': instrument_name,
                'score_data': instrument.score_data}
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request):
        instrument_model = self.queryset[0]
        serializer = InstrumentSerializer(instrument_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(instrument_model.score_data, status=status.HTTP_200_OK)
        return Response(instrument_model.score_data, status=status.HTTP_400_BAD_REQUEST)
