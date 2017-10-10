from rest_framework.routers import SimpleRouter
from .views import FavDirectorViewSet, PlanRecommenderViewSet, ShowRecommenderViewSet, CompletionRateViewSet, showBudgetRecommenderViewSet

router = SimpleRouter()
router.register("FavDirector", FavDirectorViewSet)
router.register("PlanRecommender",PlanRecommenderViewSet)
router.register("ShowRecommender", ShowRecommenderViewSet)
router.register("CompletionRate", CompletionRateViewSet)
router.register("showBudgetRecommender", showBudgetRecommenderViewSet)

urlpatterns = router.urls
