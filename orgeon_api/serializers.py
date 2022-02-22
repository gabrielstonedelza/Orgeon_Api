from rest_framework import serializers
from .models import (Volunteer, Events, Partnership, Report, Post, Gallery, ContactUs, ClientInfoProgress, \
                     UsersCheckedIn, Notifications, PostComments, LikePost, ReportComments)


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ['id', 'name', 'email', 'profession', 'country', 'photo', 'phone', 'why_join_Orgeon',
                  'get_volunteer_photo', 'date_volunteered']


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'theme', 'venue', 'date_of_event', 'event_poster', 'description_of_event', 'get_event_poster',
                  'slug', 'date_posted']


class PartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = ['id', 'name', 'email', 'phone', 'date_posted']


class ReportSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Report
        fields = ['id', 'user', 'username', 'title', 'report', 'has_read', 'report_doc', 'views', 'date_posted']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username


class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Post
        fields = ['id', 'author', 'username', 'title', 'message', 'views',
                  'date_posted']
        read_only_fields = ['author']

    def get_username(self, user):
        username = user.author.username
        return username


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'image_caption', 'image', 'get_gallery_item', 'date_posted']


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'name', 'email', 'phone', 'message', 'date_contacted']


class ClientInfoProgressSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = ClientInfoProgress
        fields = ['id', 'care_plan', 'username', 'assessment_officer', 'name', 'age', 'email', 'phone',
                  'emergency_phone', 'gender', 'client_image', 'next_of_kin', 'issue', 'progress',
                  'assessment_phase_details', 'development_phase_details', 'planning_phase_details',
                  'implementation_phase_details', 'evaluation_phase_details', 'star_phase_details', 'slug',
                  'date_issued']
        read_only_fields = ['assessment_officer']

    def get_username(self, user):
        username = user.assessment_officer.username
        return username


class UserCheckInSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = UsersCheckedIn
        fields = ['id', 'user', 'username', 'check_date', 'date_checked_in']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username


class NotificationSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    username2 = serializers.SerializerMethodField('get_username2')

    class Meta:
        model = Notifications
        fields = ['id', 'notification_id', 'notification_title', 'notification_tag', 'notification_message', 'read',
                  'notification_trigger',
                  'user', 'user2', 'username', 'username2', 'volunteer_id', 'partner_id', 'contact_id', 'report_id',
                  'client_id', 'posts_id',
                  'checked_in_id', 'date_created']

    def get_username(self, user):
        username = user.user.username
        return username

    def get_username2(self, user):
        username2 = user.user2.username
        return username2


class PostCommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = PostComments
        fields = ['id', 'post', 'user', 'username', 'comment', 'date_created']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username


class LikePostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = LikePost
        fields = ['id', 'post', 'user', 'username', 'likes', 'date_liked']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username


class ReportCommentsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = ReportComments
        fields = ['id', 'report', 'user', 'comment', 'date_created']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username
