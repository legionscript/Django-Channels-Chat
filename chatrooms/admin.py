from django.contrib import admin
from .models import Chat, ChatRoom

admin.site.register(ChatRoom)
admin.site.register(Chat)
