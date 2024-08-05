from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('v1/projects', views.ProjectListApi.as_view(), name='projects'),
    path('v1/add_project', views.AddProjectApi.as_view(), name='add_project'),
    path('v1/view_project/<pk>', views.ViewProjectApi.as_view(), name='view_project'),
    path('v1/update_project/<pk>', views.UpdateProjectApi.as_view(), name='update_project'),
    path('v1/del_project/<pk>', views.DelProjectApi.as_view(), name='del_project'),
    path('v1/view_tasks', views.ListTasksApi.as_view()),
    path('v1/add_task', views.AddTaskApi.as_view()),
    path('v1/view_task/<pk>', views.ViewTaskApi.as_view()),
    path('v1/update_task/<pk>', views.UpdateTaskApi.as_view()),
    path('v1/del_task/<pk>', views.DelTaskApi.as_view()),
    path('v1/add_comment_task/<pk>', views.AddCommnetTaskApi.as_view()),
    path('v1/view_comment_taks/<pk>', views.ListCommentTaskApi.as_view()),
    path('v1/due_24_task/', views.get_tasks_due_within_24_hours.as_view(), name='due_24_task'),
    path('v1/send_notif/', views.SendNotifAPI),

]

