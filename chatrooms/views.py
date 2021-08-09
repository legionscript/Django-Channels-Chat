from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class Index(LoginRequiredMixin, View):
	def get(self, request):
		return render(request, 'chatrooms/index.html')

class Room(LoginRequiredMixin, View):
	def get(self, request, room_name):
		return render(request, 'chatrooms/room.html', {'room_name': room_name})
