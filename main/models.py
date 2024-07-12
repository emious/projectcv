from django.db import models

# Create your models here.


class Project(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, verbose_name="id")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Task (models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.IntegerField(primary_key=True, auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()


class Comment(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)









