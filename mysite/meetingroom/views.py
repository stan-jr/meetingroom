# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from datetime import datetime

# Create your views here.
def hello_world(request):
    return render(request,
                  'hello_world.html',
                  {'current_time': datetime.now()}
                  )

def menu(request):
	food1 = {'name':'蛋炒飯','price':60,'comment':'好吃','is_spicy':False}
	food2 = {'name':'蒜泥白肉','price':160,'comment':'人氣推薦','is_spicy':True}
	foods =[food1,food2]

	return render_to_response(
                  'menu.html',
                  locals()
                  )
from meetingroom.models import Meeting,MembersJoin

def members(request):
	meetings = Meeting.objects.all()
	return render_to_response('members.html',locals())

