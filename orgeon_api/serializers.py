from rest_framework import serializers
from .models import Volunteer,Events,Partnership,NewsUpdate,Report,Post,Gallery,ContactUs,ClientInfoProgress,Reviews,UsersCheckedIn,Stories

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ['id','name','email','profession','country','photo','phone','why_join_Orgeon','get_volunteer_photo','date_volunteered']

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id','theme','venue','date_of_event','event_poster','description_of_event','get_event_poster','slug','date_posted']

class PartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = ['id','name','email','phone','date_posted']

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
        read_only_fields = ['author']

    def get_username(self, user):
        username = user.author.username
        return username

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id','image_caption','image','get_gallery_item','date_posted']

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id','name','email','phone','message','date_contacted']

class ClientInfoProgressSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = ClientInfoProgress
        fields = ['id','care_plan','username','assessment_officer','name','age','email','phone','emergency_phone','gender','client_image','next_of_kin','issue','progress','assessment_phase_details','development_phase_details','planning_phase_details','implementation_phase_details','evaluation_phase_details','star_phase_details','slug','date_issued']
        read_only_fields = ['assessment_officer']

    def get_username(self, user):
        username = user.assessment_officer.username
        return username

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id','name','review_content','ratings','date_posted']

class UserCheckInSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = UsersCheckedIn
        fields = ['id','user','username','check_date','date_checked_in']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username

class StoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = ['id','youtube_link','date_posted']