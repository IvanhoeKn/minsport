from django.contrib import admin
from .models import Status, VerifyStatus, Users, VerifyUsers, VerificationUser, Events, Organizations, ConnectUserToOrg, TableParticipants, VerificationEvent


admin.site.register(Status)
admin.site.register(VerifyStatus)
admin.site.register(Users)
admin.site.register(VerifyUsers)
admin.site.register(VerificationUser)
admin.site.register(Events)
admin.site.register(Organizations)
admin.site.register(ConnectUserToOrg)
admin.site.register(TableParticipants)
admin.site.register(VerificationEvent)
# Register your models here.
