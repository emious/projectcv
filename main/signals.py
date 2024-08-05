from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Task, Project, Comment
from main.views import send_notif
from django.core.cache import cache


@receiver(post_save, sender=Task)
def send_instance_saved_notification(sender, instance, created, **kwargs):
    if created:
        message = f"Task created: {instance.title}"
        send_notif(message)
    else:
        message = f"Task updated: {instance.title}"
        send_notif(message)


@receiver(post_delete, sender=Task)
def send_instance_deleted_notification(sender, instance, **kwargs):
    message = f"Task deleted: {instance.title}"
    send_notif(message)


@receiver(post_save, sender=Project)
@receiver(post_delete, sender=Project)
def invalidate_project_cache(sender, **kwargs):
    cache.delete_pattern('v1/projects*')
    cache.delete_pattern('v1/view_project*')


@receiver(post_save, sender=Comment)
@receiver(post_delete, sender=Comment)
def invalidate_project_cache(sender, **kwargs):
    cache.delete_pattern('v1/view_tasks*')
    cache.delete_pattern('v1/view_task*')


@receiver(post_save, sender=Comment)
@receiver(post_delete, sender=Comment)
def invalidate_project_cache(sender, **kwargs):
    cache.delete_pattern('v1/view_comment_taks')

