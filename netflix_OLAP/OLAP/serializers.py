from rest_framework import serializers
from .models import FavDirector, PlanRecommender, ShowRecommender, CompletionRate, showBudgetRecommender

class FavDirectorSerializer(serializers.ModelSerializer) :
    class Meta:
        model = FavDirector
        fields = ('user_id','user_Name','director_id','director_Name')


class PlanRecommenderSerializer(serializers.ModelSerializer) :
    class Meta:
        model = PlanRecommender
        fields = ('user_id', 'user_Name', 'user_Age', 'plan_Name', 'plan_id')



class ShowRecommenderSerializer(serializers.ModelSerializer) :
    class Meta:
        model = ShowRecommender
        fields = ('user_id','user_Name','show_Name', 'show_id', 'genre_id', 'genre_Type')



class CompletionRateSerializer(serializers.ModelSerializer) :
    class Meta:
        model = CompletionRate
        fields = ('user_id','user_Name','director_Name','show_Name', 'show_id', 'runtime')



class showBudgetRecommenderSerializer(serializers.ModelSerializer) :
    class Meta:
        model = showBudgetRecommender
        fields = ('user_id','user_Name','show_id', 'show_Name','budget_Amount')
