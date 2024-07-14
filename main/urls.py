from django.urls import path
from main import views


urlpatterns = [
    path('v1/projects', views.ProjectListApi.as_view()),

]
