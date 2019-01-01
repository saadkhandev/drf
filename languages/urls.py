from django.urls import path, include
from languages import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
urlpatterns = [
    path('', include(router.urls))
]
