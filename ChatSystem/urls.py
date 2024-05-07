from django.urls import path
from .views.Personalchatviews import *
from .views.Roomchatviews import *

urlpatterns = [
    path('getchatrooms/<int:school_id>/', getChatRooms, name='get_chat_rooms'),
    path('getchatroom/<str:chatroom_name>/', getChatRoom, name='get_chat_room'),
    path('createchatroom/<int:school_id>/', createChatRoom, name='create_chat_room'),
    path('editchatroom/<int:chatroom_id>/', editChatRoom, name='edit_chat_room'),
    path('deletechatroom/<int:chatroom_id>/', deleteChatRoom, name='delete_chat_room'),

    path('getroomchats/<int:chatroom_id>/',getRoomMessages, name='get_personal_chats'),

    path('getpersonalchatrooms/<int:user_id>/', getPersonalChatRooms, name='get_personal_chat_rooms'),
    path('getpersonalchatroom/<int:personalchatroom_id>/', getPersonalChatRoom, name='get_personal_chat_room'),
    path('createpersonalchatroom/<int:user_id>/', createPersonalChatRoom, name='create_personal_chat_room'),
    path('deletepersonalchatroom/<int:personalchatroom_id>/', deletePersonalChatRoom, name='delete_personal_chat_room'),

    path('getpersonalchatroommessages/<int:personalchatroom_id>/', getPersonalChatMessages, name='get_personal_chat_messages'),
]