from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from .models import State, Club
from .serializers import StateSerializer, ClubSerializer


class StateList(generics.ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class ClubList(APIView):
    def get(self, request, state_slug, *args, **kwargs):
        state = get_object_or_404(State, slug=state_slug)
        clubs = Club.objects.filter(State=state)
        data = ClubSerializer(clubs, many=True).data
        return Response(data)
