from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, ListView

from webapp.forms import MessageForm
from webapp.models import Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    template_name = 'message_create.html'
    form_class = MessageForm
    model = Message

    def form_valid(self, form):
        author = self.request.user
        recipient = get_object_or_404(get_user_model(), pk=self.kwargs.get('pk'))
        message = form.save(commit=False)
        message.author = author
        message.recipient = recipient
        message.save()
        return redirect('index')


class IncomingMessageView(ListView):
    template_name = 'incoming_message.html'
    context_object_name = 'recipient_messages'
    paginate_by = 5
    paginate_orphans = 2

    def get_queryset(self):
        return Message.objects.filter(recipient=self.request.user)


class SentMessageView(ListView):
    template_name = 'sent_message.html'
    context_object_name = 'sent_messages'
    paginate_by = 5
    paginate_orphans = 2

    def get_queryset(self):
        return Message.objects.filter(author=self.request.user)