from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import View
from .forms import MessageForm
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from .models import Message
from profiles.models import Profile
from .email import Email

class MessageView(View):
    template_name = 'messages.html'

    def get(self, request, recipient, sender, *args, **kwargs):
        if Profile.objects.filter(username=request.user).exists():
            user_profile = Profile.objects.get(user=request.user)
        form = MessageForm()
        sender_user = Profile.objects.all().get(username=sender)
        user = request.user
        recipient_user = Profile.objects.get(user=request.user)
        try:
            messages = Message.objects.filter(Q(recipient=request.user, sender=sender_user.user) | Q(recipient=sender_user.user, sender=request.user)).order_by('created')
        except ObjectDoesNotExist:
            messages = None
        context = {
            'form': form, 'messages': messages,
            'user': user, 'sender_user': sender_user,
            'recipient_user': recipient_user, 'user_profile': user_profile
        }
        return render(request, self.template_name, context)

    def post(self, request, recipient, sender, *args, **kwargs):
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            recipient_user = Profile.objects.all().get(username=sender)
            message.recipient = recipient_user.user
            text = form.cleaned_data['text']
            if form.cleaned_data['image'] is not None:
                message.image = form.cleaned_data['image']
            form = MessageForm()
            message.save()
            Email.messageRecievedFromMate(request, message.recipient.email, message.sender, message.recipient)
            return redirect('messages:messaging', request.user, recipient_user.user)
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

    def get_queryset(self):
        queryset = super(OwnerMixin, self).get_queryset()
        return queryset.filter(recipient=self.request.user)