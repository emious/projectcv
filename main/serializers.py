from rest_framework import serializers
from main.models import Project, Comment, Task


class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(allow_blank=True)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(allow_blank=True)
    STATUS_CHOICES = (
        ("pending", "'Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    )
    status = serializers.ChoiceField(choices=STATUS_CHOICES, default='friendly')
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    due_date = serializers.DateTimeField()

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.due_date = validated_data.get('due_date', instance.due_date)

        instance.save()
        return instance


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField(required=True, max_length=255)
    content = serializers.CharField(required=True, max_length=255)
    created_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):

        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.author = validated_data.get('author', instance.author)
        instance.content = validated_data.get('content', instance.content)
        instance.created_at = validated_data.get('created_at', instance.created_at)

        instance.save()
        return instance