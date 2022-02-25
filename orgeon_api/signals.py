from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import (Volunteer, Partnership, Post, Report, ContactUs, Notifications, ClientInfoProgress, UsersCheckedIn,
                     PostComments, LikePost, ReportComments)

User = settings.AUTH_USER_MODEL
from orgeon_users.models import User as orgeonusers


@receiver(post_save, sender=Volunteer)
def alert_volunteer_created(sender, created, instance, **kwargs):
    title = f"Got new Volunteer"
    notification_tag = "Volunteer"
    message = f"{instance.name} just volunteered for Orgeon"
    admin_user = orgeonusers.objects.get(id=1)

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_tag=notification_tag,
                                     notification_title=title, notification_message=message, user2=admin_user,
                                     volunteer_id=instance.id)


@receiver(post_save, sender=Partnership)
def alert_partner_created(sender, created, instance, **kwargs):
    title = f"Got new Partner"
    notification_tag = "Partnership"
    message = f"{instance.name} wants to partner with Orgeon"
    admin_user = orgeonusers.objects.get(id=1)

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_tag=notification_tag,
                                     notification_title=title, notification_message=message, user2=admin_user,
                                     partner_id=instance.id)


@receiver(post_save, sender=ContactUs)
def alert_contact_message(sender, created, instance, **kwargs):
    title = f"Got new message from {instance.name}"
    notification_tag = "Contact"
    message = f"{instance.name} sent a message to Orgeon"
    admin_user = orgeonusers.objects.get(id=1)

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_tag=notification_tag,
                                     notification_title=title, notification_message=message, user2=admin_user,
                                     contact_id=instance.id)


@receiver(post_save, sender=Report)
def alert_new_report(sender, created, instance, **kwargs):
    title = f"New report from {instance.user.username}"
    notification_tag = "Report"
    message = f"{instance.title}"
    users = orgeonusers.objects.exclude(id=instance.user.id)

    if created:
        for i in users:
            Notifications.objects.create(notification_id=instance.id, notification_tag=notification_tag,
                                         notification_title=title, notification_message=message, user=instance.user,
                                         user2=i,
                                         report_id=instance.id)


@receiver(post_save, sender=ClientInfoProgress)
def alert_client_progress(sender, created, instance, **kwargs):
    title = f"Update on Client"
    notification_tag = "Client"
    message = f"A client was added or updated"
    admin_user = orgeonusers.objects.get(id=1)

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_tag=notification_tag,
                                     notification_title=title, notification_message=message,
                                     user=instance.assessment_officer,
                                     user2=admin_user,
                                     client_id=instance.id)


@receiver(post_save, sender=Post)
def alert_post_from_employees(sender, created, instance, **kwargs):
    title = f"New post from {instance.author}"
    notification_tag = "Posts"
    message = f"{instance.title}"
    admin_user = orgeonusers.objects.get(id=1)
    users = orgeonusers.objects.exclude(id=instance.user.id)

    if created:
        for i in users:
            Notifications.objects.create(notification_id=instance.id, notification_tag=notification_tag,
                                         notification_title=title, notification_message=message, user=admin_user,
                                         user2=i,
                                         posts_id=instance.id)


@receiver(post_save, sender=PostComments)
def alert_post_comments(sender, created, instance, **kwargs):
    title = f"New post comment"
    notification_tag = "Post_Comment"
    message = f"{instance.user.username} commented on  post '{instance.post.title}'"
    users = orgeonusers.objects.exclude(id=instance.user.id)

    if created:
        for i in users:
            Notifications.objects.create(notification_id=instance.id, notification_tag=notification_tag,
                                         notification_title=title, notification_message=message, user=instance.user,
                                         user2=i,
                                         posts_id=instance.id)


@receiver(post_save, sender=LikePost)
def alert_liked_post(sender, created, instance, **kwargs):
    title = f"New post like"
    notification_tag = "Post_Like"
    message = f"{instance.user.username} liked post '{instance.post.title}'"
    users = orgeonusers.objects.exclude(id=instance.user.id)

    if created:
        for i in users:
            Notifications.objects.create(notification_id=instance.id, notification_tag=notification_tag,
                                         notification_title=title, notification_message=message, user=instance.user,
                                         user2=i,
                                         posts_id=instance.id)


@receiver(post_save, sender=ReportComments)
def alert_report_comments(sender, created, instance, **kwargs):
    title = f"New report comment"
    notification_tag = "Report_Comment"
    message = f"{instance.user.username} commented on report '{instance.report.title}'"
    users = orgeonusers.objects.exclude(id=instance.user.id)

    if created:
        for i in users:
            Notifications.objects.create(notification_id=instance.id, notification_tag=notification_tag,
                                         notification_title=title, notification_message=message, user=instance.user,
                                         user2=i,
                                         report_id=instance.id)
