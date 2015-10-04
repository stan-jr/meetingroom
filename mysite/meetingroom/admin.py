from django.contrib import admin

# Register your models here.
from meetingroom.models import Meeting,Member,MeetingRoom,Team,MembersJoin 
admin.site.register(Meeting)
admin.site.register(Member)
admin.site.register(MembersJoin)
admin.site.register(MeetingRoom)
admin.site.register(Team)