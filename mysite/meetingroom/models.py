from django.db import models

# Create your models here.

# class meetingReserve()
class Meeting(models.Model):
	creater = models.CharField(max_length=40)
	team = models.CharField(max_length=20)
	teamId = models.CharField(max_length=20)
	roomName = models.CharField(max_length=20)
	subject = models.CharField(max_length=40)
	issue = models.CharField(max_length=40)
	meetingType = models.CharField(max_length=10)
	date = models.CharField(max_length=20)
	start_time = models.CharField(max_length=20)
	end_time = models.CharField(max_length=20)
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
    

class MembersJoin(models.Model):
	meeting =  models.ForeignKey(Meeting)
	e_mail = models.CharField(max_length=40)

class Member(models.Model):
	firstName = models.CharField(max_length=40)
	lastName = models.CharField(max_length=20)
	nickName = models.CharField(max_length=20)
	e_mail = models.CharField(max_length=40)
	team = models.CharField(max_length=20)
	teamId = models.CharField(max_length=20)
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

class Team(models.Model):
	teamName = models.CharField(max_length=20)
	teamId = models.CharField(max_length=20)
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

class MeetingRoom(models.Model):
	roomName = models.CharField(max_length=20)
	roomNameId = models.CharField(max_length=20)
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)