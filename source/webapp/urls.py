from django.contrib import admin
from django.urls import path, include

from webapp.views import MessageCreateView, SentMessageView, IncomingMessageView

app_name = 'webapp'

urlpatterns = [
    path('message/<int:pk>/', MessageCreateView.as_view(), name='write_message'),
    path('messages/incoming/', IncomingMessageView.as_view(), name='incoming_msg'),
    path('messages/sent/', SentMessageView.as_view(), name='sent_msg')
]
