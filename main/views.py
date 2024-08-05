import datetime
from datetime import timedelta
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Project, Task, Comment
from main.serializers import ProjectSerializer, TaskSerializer, CommentSerializer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .mixins import CachedListMixin


def send_notif(message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notifications",
        {
            'type': "send_notification",
            'message': message,
        }
    )


@api_view(['POST'])
def SendNotifAPI(request):
    if request.method == "POST":
        try:
            data = request.data
            message = data.get('message')
            send_notif(message)
            response_data = {
                'message': message,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProjectListApi(CachedListMixin, generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class AddProjectApi(generics.CreateAPIView):
    serializer_class = ProjectSerializer


class ViewProjectApi(CachedListMixin, generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class UpdateProjectApi(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class DelProjectApi(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ListTasksApi(CachedListMixin, generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class AddTaskApi(generics.CreateAPIView):
    serializer_class = TaskSerializer


class ViewTaskApi(CachedListMixin, generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UpdateTaskApi(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = ProjectSerializer


class DelTaskApi(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = ProjectSerializer


class AddCommnetTaskApi(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ListCommentTaskApi(CachedListMixin, generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# • Create a Celery task to send an email reminder for tasks due within the next 24 hours.
class get_tasks_due_within_24_hours(generics.ListAPIView):
    now = datetime.datetime.now()
    next_24_hours = now + timedelta(hours=24)
    queryset = Task.objects.filter(due_date__gte=now, due_date__lte=next_24_hours)
    # queryset = Task.objects.filter(due_date__gte= now + timedelta(hours=23,minutes=45), due_date__lte=next_24_hours)
    serializer_class = TaskSerializer
