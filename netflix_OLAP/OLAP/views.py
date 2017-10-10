from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


from .serializers import (FavDirectorSerializer, PlanRecommenderSerializer, ShowRecommenderSerializer, CompletionRateSerializer, showBudgetRecommenderSerializer)
from .models import FavDirector, PlanRecommender, ShowRecommender, CompletionRate, showBudgetRecommender

class FavDirectorViewSet(ModelViewSet):
    serializer_class = FavDirectorSerializer
    queryset = FavDirector.objects.all()

class PlanRecommenderViewSet(ModelViewSet):
    serializer_class = PlanRecommenderSerializer
    queryset = PlanRecommender.objects.all()

class ShowRecommenderViewSet(ModelViewSet):
    serializer_class = ShowRecommenderSerializer
    queryset = ShowRecommender.objects.all()

class CompletionRateViewSet(ModelViewSet):
    serializer_class = CompletionRateSerializer
    queryset = CompletionRate.objects.all()

class showBudgetRecommenderViewSet(ModelViewSet):
    serializer_class = showBudgetRecommenderSerializer
    queryset = showBudgetRecommender.objects.all()
