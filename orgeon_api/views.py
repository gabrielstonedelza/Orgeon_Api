from django.shortcuts import get_object_or_404

from .models import (Volunteer,Events,Partnership,NewsUpdate,Report,Post,Comments,Gallery,ContactUs,ClientInfoProgress,Reviews,UsersCheckedIn)

from .serializers import (VolunteerSerializer,EventsSerializer,PartnershipSerializer,NewsUpdateSerializer,ReportSerializer,PostSerializer,CommentSerializer,GallerySerializer,ContactUsSerializer,ClientInfoProgressSerializer,ReviewSerializer,UserCheckInSerializer)

from datetime import datetime,date,time,timedelta
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response

from orgeon_users.serializers import ProfileSerializer
from orgeon_users.models import User,Profile
from django.utils import timezone
from .process_mail import send_my_mail
from django.conf import settings

# post and get volunteers
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_volunteer(request):
    serializer = VolunteerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        send_my_mail(f"New Volunteer", settings.EMAIL_HOST_USER, "gabrielstonedelza@gmail.com",
                     {"":""},"default_templates/new_volunteer.html")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_volunteers(request):
    volunteers = Volunteer.objects.all().order_by('-date_volunteered')
    serializer = VolunteerSerializer(volunteers,many=True)
    return Response(serializer.data)

# post and get events
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_event(request):
    serializer = EventsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_events(request):
    events = Events.objects.all().order_by('-date_posted')
    serializer = EventsSerializer(events,many=True)
    return Response(serializer.data)


# post and get partners
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_partner(request):
    serializer = PartnershipSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        send_my_mail(f"New Partner", settings.EMAIL_HOST_USER, "gabrielstonedelza@gmail.com",
                     {"": ""}, "default_templates/new_partnership.html")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_partners(request):
    partners = Partnership.objects.all().order_by('-date_posted')
    serializer = PartnershipSerializer(partners,many=True)
    return Response(serializer.data)

# post and get news
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_news_update(request):
    serializer = NewsUpdateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_news_update(request):
    news = NewsUpdate.objects.all().order_by('-date_posted')
    serializer = NewsUpdateSerializer(news,many=True)
    return Response(serializer.data)

# post and get gallery
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_to_gallery(request):
    serializer = GallerySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_gallery_list(request):
    gallery = Gallery.objects.all().order_by('-date_posted')
    serializer = GallerySerializer(gallery,many=True)
    return Response(serializer.data)

# post and get contact us
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_to_contacts(request):
    serializer = ContactUsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        send_my_mail(f"New Contact Message", settings.EMAIL_HOST_USER, "gabrielstonedelza@gmail.com",
                     {"": ""}, "default_templates/contact.html")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_contact_list(request):
    contacts = ContactUs.objects.all().order_by('-date_contacted')
    serializer = ContactUsSerializer(contacts,many=True)
    return Response(serializer.data)

# post and get Review
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_to_reviews(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        send_my_mail(f"New Review", settings.EMAIL_HOST_USER, "gabrielstonedelza@gmail.com",
                     {"": ""}, "default_templates/review.html")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_review_list(request):
    reviews = Reviews.objects.all().order_by('-date_posted')
    serializer = ReviewSerializer(reviews,many=True)
    return Response(serializer.data)

# post and get report
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_reports(request):
    serializer = ReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        send_my_mail(f"New Report", settings.EMAIL_HOST_USER, "gabrielstonedelza@gmail.com",
                     {"": ""}, "default_templates/report.html")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_report_list(request):
    reports = Report.objects.all().order_by('-date_posted')
    serializer = ReportSerializer(reports,many=True)
    return Response(serializer.data)

# post and get post
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_posts(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_post_list(request):
    posts = Post.objects.all().order_by('-date_posted')
    serializer = PostSerializer(posts,many=True)
    return Response(serializer.data)

# post and get clients
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_client(request):
    serializer = ClientInfoProgressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(assessment_officer=request.user)
        send_my_mail(f"New Client", settings.EMAIL_HOST_USER, "gabrielstonedelza@gmail.com",
                     {"": ""}, "default_templates/client.html")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_client_list(request):
    clients = ClientInfoProgress.objects.all().order_by('-date_issued')
    serializer = ClientInfoProgressSerializer(clients,many=True)
    return Response(serializer.data)

# post and get check ins
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def check_in(request):
    serializer = UserCheckInSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_check_in_lists(request):
    check_ins = UsersCheckedIn.objects.all().order_by('-date_checked_in')
    serializer = UserCheckInSerializer(check_ins,many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT'])
@permission_classes([permissions.AllowAny])
def update_client(request, id):
    client = get_object_or_404(ClientInfoProgress, id=id)
    serializer = ClientInfoProgressSerializer(client, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        send_my_mail(f"Client Updated", settings.EMAIL_HOST_USER, "gabrielstonedelza@gmail.com",
                     {"": ""}, "default_templates/client_update.html")
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)