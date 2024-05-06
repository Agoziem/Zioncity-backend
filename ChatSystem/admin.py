from django.contrib import admin
from .models import *

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'school', 'created_at')
    list_filter = ('school__Schoolname', 'created_at')
    search_fields = ('name', 'school__Schoolname')
    sortable_by = ('created_at',)

@admin.register(RoomMessage)
class RoomMessageAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'room', 'timestamp')
    list_filter = ('room__name', 'timestamp')
    search_fields = ('user__username', 'content')
    sortable_by = ('timestamp',)

    def get_username(self, obj):
        return obj.user.username

@admin.register(PersonalChatRoom)
class PersonalChatRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_user1_username', 'get_user2_username', 'created_at')
    list_filter = ('user1__username', 'user2__username', 'created_at')
    search_fields = ('user1__username', 'user2__username')
    sortable_by = ('created_at',)

    def get_user1_username(self, obj):
        return obj.user1.username

    def get_user2_username(self, obj):
        return obj.user2.username

@admin.register(PersonalChatMessage)
class PersonalChatMessageAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'room', 'timestamp')
    list_filter = ('room__name', 'timestamp')
    search_fields = ('user__username', 'content')
    sortable_by = ('timestamp',)

    def get_username(self, obj):
        return obj.user.username


