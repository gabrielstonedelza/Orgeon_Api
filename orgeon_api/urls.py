from django.urls import path

from . import views

urlpatterns = [
    path('add_volunteer/',views.add_volunteer),
    path('get_volunteers/',views.get_volunteers),
    path('add_event/',views.add_event),
    path('get_events/',views.get_events),
    path('add_partner/',views.add_partner),
    path('get_partners/',views.get_partners),
    path('add_news_update/',views.add_news_update),
    path('get_news_update/',views.get_news_update),
    path('add_to_gallery/',views.add_to_gallery),
    path('get_gallery_list/',views.get_gallery_list),
    path('add_to_contacts/',views.add_to_contacts),
    path('get_contact_list/',views.get_contact_list),
    path('add_to_reviews/',views.add_to_reviews),
    path('get_review_list/',views.get_review_list),
    path('add_reports/',views.add_reports),
    path('get_report_list/',views.get_report_list),
    path('add_to_posts/',views.add_to_posts),
    path('get_post_list/',views.get_post_list),
    path('add_client/',views.add_client),
    path('get_client_list/',views.get_post_list),
    path('update_client/<int:id>/',views.update_client),
    path('check_in/',views.check_in),
    path('get_check_in_lists/',views.get_check_in_lists),
]