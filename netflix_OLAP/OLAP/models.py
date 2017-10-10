from django.db import models



class FavDirector(models.Model):    #Gathers data on favourite director of the user
    user_id = models.IntegerField()
    user_Name = models.CharField(max_length=255)
    director_id = models.CharField(max_length=255)
    director_Name = models.CharField(max_length=255)



class PlanRecommender(models.Model):    # Gathers data on plans user purchases
    user_id = models.IntegerField()
    user_Name = models.CharField(max_length=255)
    user_Age = models.IntegerField()
    plan_Name = models.CharField(max_length=255)
    plan_id = models.IntegerField()



class ShowRecommender(models.Model):    # Gathers data on type of shows user watches
    user_id = models.IntegerField()
    user_Name = models.CharField(max_length=255)
    show_Name = models.CharField(max_length=255)
    show_id = models.IntegerField()
    genre_id = models.IntegerField()
    genre_Type = models.CharField(max_length=255)



class CompletionRate(models.Model):    #Gathers data on whether user has followed through with the show and gone on to view more seasons and episodes
    user_id = models.IntegerField()
    user_Name = models.CharField(max_length=255)
    director_Name = models.CharField(max_length=255)
    show_Name = models.CharField(max_length=255)
    show_id = models.IntegerField()
    runtime = models.IntegerField()



class showBudgetRecommender(models.Model):    #Gathers data on shows watched according to budget by the user
    user_id = models.IntegerField()
    user_Name = models.CharField(max_length=255)
    show_id = models.IntegerField()
    show_Name = models.CharField(max_length=255)
    budget_Amount = models.IntegerField()
