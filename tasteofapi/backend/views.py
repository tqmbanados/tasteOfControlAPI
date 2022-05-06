from django.shortcuts import render
from .models import FullScore, Actor, Instrument
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FullScoreSerializer, ActorSerializer, InstrumentSerializer


class MainScoreView(APIView):
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


class InstrumentView(APIView):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer

    def get(self, request):
        instrument_name = request.query_params.get('instrument')
        request_measure = request.query_params.get('measure')
        query = self.queryset.filter(instrument=instrument_name)
        if len(query) > 0:
            instrument = query[0]
            measure = instrument.measure
            if measure != request_measure:
                print("WARNING: REQUESTED MEASURE DIFFERENT FROM HELD MEASURE\n",
                      f'Requested: {request_measure}. Current: {measure}')
            data = {'instrument': instrument.instrument,
                    'score_data': instrument.score_data,
                    'duration': instrument.duration}
            return Response(data, status=status.HTTP_200_OK)
        data = {'instrument': "error"}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        instrument_name = request.data.get('instrument')
        instrument_model = self.queryset.filter(instrument=instrument_name)[0]
        serializer = InstrumentSerializer(instrument_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(instrument_model.score_data, status=status.HTTP_200_OK)
        return Response(instrument_model.score_data, status=status.HTTP_400_BAD_REQUEST)


class ActorView(APIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request):
        number = request.query_params.get('number')
        query = self.queryset.filter(number=number)
        if len(query) > 0:
            actor = query[0]
            data = {'action': actor.action,
                    'stage': actor.stage}
            return Response(data, status=status.HTTP_200_OK)
        else:
            actor = self.queryset[-1]
            data = {'action': actor.action,
                    'stage': actor.stage}
            return Response(data, status=status.HTTP_206_PARTIAL_CONTENT)

    def put(self, request):
        actor_model = self.queryset[0]
        serializer = ActorSerializer(actor_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(actor_model.action, status=status.HTTP_200_OK)
        return Response(actor_model.action, status=status.HTTP_400_BAD_REQUEST)