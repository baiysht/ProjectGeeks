from django.urls import path
from Task import views


urlpatterns = [
    path('api/v1/tasks/', views.TaskListCreatAPIView.as_view()),
    path('api/v1/tasks/<int:id>/', views.TaskDetailUpdateDeleteAPIView.as_view()),
]