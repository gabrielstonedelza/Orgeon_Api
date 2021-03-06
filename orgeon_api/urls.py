from django.urls import path

from . import views

urlpatterns = [
    path('add_volunteer/', views.add_volunteer),
    path('get_volunteers/', views.get_volunteers),
    path('volunteer_detail/<int:id>/', views.volunteer_detail),
    path('delete_volunteer/<int:id>/', views.delete_volunteer),
    path('add_event/', views.add_event),
    path('get_events/', views.get_events),
    path('add_partner/', views.add_partner),
    path('get_partners/', views.get_partners),
    path('partner_detail/<int:id>/', views.partner_detail),
    path('delete_partner/<int:id>/', views.delete_partner),

    path('add_to_gallery/', views.add_to_gallery),
    path('get_gallery_list/', views.get_gallery_list),
    path('add_to_contacts/', views.add_to_contacts),
    path('get_contact_list/', views.get_contact_list),

    path('add_reports/', views.add_reports),
    path('get_report_list/', views.get_report_list),
    path('report_detail/<int:id>/', views.report_detail),
    path('add_to_posts/', views.add_to_posts),
    path('get_post_list/', views.get_post_list),
    path('add_client/', views.add_client),
    path('get_client_list/', views.get_post_list),
    path('update_client/<int:id>/', views.update_client),
    path('check_in/', views.check_in),
    path('get_check_in_lists/', views.get_check_in_lists),

    path('get_user_notifications/', views.get_user_notifications),
    path('get_all_user_notifications/', views.get_all_user_notifications),
    path('get_triggered_notifications/', views.get_triggered_notifications),
    path("read_notification/<int:id>/", views.read_notification),

    path('add_post_comment/<int:id>/', views.add_post_comment),
    path('add_reports_comment/<int:id>/', views.add_report_comment),
    path('get_all_report_comments/<int:id>/', views.get_all_report_comment),

    path('get_post_comments/', views.get_post_comments),
    path('get_report_comments/', views.get_repost_comments),

]
