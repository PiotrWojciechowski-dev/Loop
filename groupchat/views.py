from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import View
from .forms import  GroupChatForm, GroupMessageForm
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from .models import GroupChat, GroupMessage
from profiles.models import Profile

class GroupMessageView(View):
    template_name = 'groupchats.html'

    def get(self, request, sender, recipient, *args, **kwargs):
        form = GroupMessageForm()
        user = request.user
        try:
            messages = GroupMessage.objects.filter(Q(recipient=request.user, sender=sender_user.user) | Q(recipient=sender_user.user, sender=request.user)).order_by('created')
        except ObjectDoesNotExist:
            messages = None
        context = {
            'form': form, 'messages': messages, 'user': user
        }
        return render(request, self.template_name, context)

    def post(self, request, recipient, sender, *args, **kwargs):
        groupchat = GroupChat.objects.all().get(name=recipient)
        form = GroupMessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = groupchat
            text = form.cleaned_data['text']
            if form.cleaned_data['image'] is not None:
                print('hello')
                message.image = form.cleaned_data['image']
            form = GroupMessageForm()
            message.save()
            return redirect('messages:messaging', request.user, recipient_user.user)
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

    def get_queryset(self):
        queryset = super(OwnerMixin, self).get_queryset()
        return queryset.filter(recipient=self.request.user)
