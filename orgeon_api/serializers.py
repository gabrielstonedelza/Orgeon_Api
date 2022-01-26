from rest_framework import serializers
from .models import Volunteer,Events,Partnership,NewsUpdate,Report,Post,Comments,Gallery,ContactUs,ClientInfoProgress,NotifyMe,Reviews,UsersCheckedIn

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ['id','name','email','profession','country','photo','phone','why_join_Orgeon','date_volunteered']

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id','theme','venue','date_of_event','event_poster','description_of_event','slug','date_posted']

class PartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = ['id','partnership','name','email','phone','date_posted']


class  NewsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsUpdate
        fields = ['id','title','message','date_posted']

class ReportSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Report
        fields = ['id','user','username','title','report','has_read','report_doc','slug','date_posted']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username

class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Post
        fields = ['id','author','username','title','message','views','has_read','need_replies','slug','date_posted']

    def get_username(self, user):
        username = user.user.username
        return username

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Comments
        fields = ['id','user','username','post','comment','slug','date_posted']

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id','image_caption','image','date_posted']

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ['id','name','email','phone','message','date_contacted']

class ClientInfoProgressSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = ClientInfoProgress
        fields = ['id','care_plan','assessment_officer','name','age','email','phone','emergency_phone','gender','client_image','next_of_kin','issue','progress','assessment_phase_details','development_phase_details','planning_phase_details','implementation_phase_details','evaluation_phase_details','star_phase_details','slug','date_issued']

    def get_username(self, user):
        username = user.user.username
        return username

class NotificationSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = NotifyMe
        fields = ['id','user','username','notify_title','notify_alert','post_slug','report_slug','comment_slug','sender_or_receiver','read','slug','date_notified']

    def get_username(self, user):
        username = user.user.username
        return username

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id','review_content','ratings','date_posted']

class UserCheckInSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = UsersCheckedIn
        fields = ['id','user','username','checked_in','check_date','has_checked_in','date_checked_in']

    def get_username(self, user):
        username = user.user.username
        return username