from django.contrib import admin

from .models import (Volunteer, Events, Partnership, Report, Post, Gallery, ContactUs, ClientInfoProgress, \
                     UsersCheckedIn, Notifications,
                     PostComments, LikePost, ReportComments)

admin.site.register(Volunteer)
admin.site.register(Events)
admin.site.register(Partnership)
admin.site.register(Report)
admin.site.register(Post)
admin.site.register(Gallery)
admin.site.register(ContactUs)
admin.site.register(ClientInfoProgress)
admin.site.register(UsersCheckedIn)
admin.site.register(Notifications)
admin.site.register(PostComments)
admin.site.register(LikePost)
admin.site.register(ReportComments)
