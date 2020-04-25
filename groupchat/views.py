from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import View
from .forms import  GroupChatForm, GroupMessageForm
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from .models import GroupChat, GroupMessage
from profiles.models import Profile
from profiles.models import Mates

class GroupMessageView(View):
    template_name = 'groupchats.html'

    def get(self, request, groupchat_id, groupchat_name, *args, **kwargs):
        form = GroupMessageForm()
        user = request.user
        user_profile = Profile.objects.get(user=request.user)
        sender_user = Profile.objects.get(user=request.user)
        groupchat = GroupChat.objects.all().get(id=groupchat_id)
        profiles = Profile.objects.all()
        try:
            messages = GroupMessage.objects.filter(Q(recipient=groupchat))
        except ObjectDoesNotExist:
            messages = None
        context = {
            'form': form, 'messages': messages, 'user': user, 'groupchat':groupchat, 'user_profile':user_profile,
            'sender_user': sender_user, 'profiles':profiles
        }
        return render(request, self.template_name, context)

    def post(self, request, groupchat_id, groupchat_name, *args, **kwargs):
        groupchat = GroupChat.objects.all().get(id=groupchat_id)
        form = GroupMessageForm(request.POST, request.FILES)
        if form.is_valid():
            GroupMessage = form.save(commit=False)
            GroupMessage.sender = request.user
            GroupMessage.recipient =  GroupChat.objects.all().get(id=groupchat_id)
            text = form.cleaned_data['text']
            if form.cleaned_data['image'] is not None:
                GroupMessage.image = form.cleaned_data['image']
            form = GroupMessageForm()
            GroupMessage.save()
            return redirect('groupchat:messaging', groupchat.id, groupchat.name)
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

    def get_queryset(self):
        queryset = super(OwnerMixin, self).get_queryset()
        return queryset.filter(recipient=self.request.user)

def create_group(request):
    confirmed_mates = []
    try:
        mate = Mates.objects.get(current_user=request.user)
        mates = mate.users.all()
    except ObjectDoesNotExist:
        mates = None
        posts = Post.objects.filter(Q(user=user)).order_by('-created')
        files = PostFile.objects.filter(Q(user=user))
        comments = Comment.objects.filter(Q(user=user)).order_by('-created')
    if mates != None:
        for m in mates:
            try:
                confirmed_mate = Mates.objects.get(current_user=m, users=request.user)
                confirmed_mates.append(confirmed_mate.current_user.username)
            except ObjectDoesNotExist: 
                confirmed_mate = None

    if request.method == 'POST':
        print("Hello")
        form = GroupChatForm(confirmed_mates, request.POST, request.FILES)
        if form.is_valid():
            print("hey there")
            groupchat = form.save(commit=False)
            if request.user.is_authenticated:
                owner = request.user
                groupchat.owner = owner
            if form.cleaned_data['groupchatImage'] is not None:
                groupchat.groupImage = form.cleaned_data['groupchatImage']
            groupchat.name = form.cleaned_data['name']
            groupchat = form.save()
            groupchat.save()
            members = form.cleaned_data['members']
            groupchat.members.set(form.cleaned_data['members'])
            groupchat.members.add(owner.id)
            groupchat.save()
            return redirect('groupchat:messaging', groupchat.id, groupchat.name)
    else:
        form = GroupChatForm(confirmed_mates)
    return render(request, 'createGroupchats.html', {'form':form})