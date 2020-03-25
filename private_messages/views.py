from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import View
from .forms import MessageForm
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from .models import Message

class MessageView(View):
    template_name = 'messages.html'

    def get(self, request, *args, **kwargs):
        form = MessageForm()
        try:
            messages = Message.objects.get(recipient=request.user)
        except ObjectDoesNotExist:
            messages = None
        context = {
            'form': form, 'messages': messages
        }
        return render(request, self.template_name, context)

    def post(self, request, recipient, *args, **kwargs):
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient.set(recipient)
            message.save()
            text = form.cleaned_data['message']
            if form.cleaned_data['image'] is not None:
                profile.profile_image = form.cleaned_data['image']
            form = MessageForm
            mess.save()
            return redirect("messages:messaging")
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

    def get_queryset(self):
        queryset = super(OwnerMixin, self).get_queryset()
        return queryset.filter(recipient=self.request.user)