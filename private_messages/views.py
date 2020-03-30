from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import View
from .forms import MessageForm
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from .models import Message
from profiles.models import Profile

class MessageView(View):
    template_name = 'messages.html'

    def get(self, request, recipient, sender, *args, **kwargs):
        form = MessageForm()
        sender_user = Profile.objects.all().get(username=sender)
        buser = request.user
        try:
            messages = Message.objects.filter(Q(recipient=request.user, sender=sender_user.user) | Q(recipient=sender_user.user, sender=request.user)).order_by('created')
        except ObjectDoesNotExist:
            messages = None
        context = {
            'form': form, 'messages': messages, 'buser': buser
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
                print('hello')
                message.image = form.cleaned_data['image']
            form = MessageForm()
            message.save()
            return redirect('messages:messaging', request.user, recipient_user.user)
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

    def get_queryset(self):
        queryset = super(OwnerMixin, self).get_queryset()
        return queryset.filter(recipient=self.request.user)