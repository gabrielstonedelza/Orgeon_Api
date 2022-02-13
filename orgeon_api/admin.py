from django.contrib import admin

from .models import Volunteer, Events, Partnership, Report, Post, Gallery, ContactUs, ClientInfoProgress, \
    UsersCheckedIn

admin.site.register(Volunteer)
admin.site.register(Events)
admin.site.register(Partnership)
admin.site.register(Report)
admin.site.register(Post)
admin.site.register(Gallery)
admin.site.register(ContactUs)
admin.site.register(ClientInfoProgress)
admin.site.register(UsersCheckedIn)

