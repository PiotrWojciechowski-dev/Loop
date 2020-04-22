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

    def get(self, request, groupchat_id, groupchat_name, *args, **kwargs):
        form = GroupMessageForm()
        user = request.user
        groupchat = GroupChat.objects.all().get(id=groupchat_id)
        try:
            messages = GroupMessage.objects.filter(Q(recipient=groupchat))
        except ObjectDoesNotExist:
            messages = None
        context = {
            'form': form, 'messages': messages, 'user': user
        }
        return render(request, self.template_name, context)

    def post(self, request, groupchat_id, groupchat_name, *args, **kwargs):
        groupchat = GroupChat.objects.all().get(name=recipient)
        form = GroupMessageForm(request.POST, request.FILES)
        if form.is_valid():
            GroupMessage = form.save(commit=False)
            GroupMessage.sender = request.user
            GroupMessage.recipient = groupchat
            text = form.cleaned_data['text']
            if form.cleaned_data['image'] is not None:
                print('hello')
                GroupMessage.image = form.cleaned_data['image']
            form = GroupMessageForm()
            GroupMessage.save()
            return redirect('groupchat:messaging', groupchat.PK)
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

    def get_queryset(self):
        queryset = super(OwnerMixin, self).get_queryset()
        return queryset.filter(recipient=self.request.user)
