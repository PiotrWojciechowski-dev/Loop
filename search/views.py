from django.shortcuts import render, get_object_or_404
from profiles.models import Profile
from django.db.models import Q
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()

def search_result(request):
    profiles = None
    query = None
    #products_filter = ProductFilter(request.GET, queryset=Product.objects.all())
    #products = products_filter.qs
    if 'q' in request.GET:
        query = request.GET.get('q')
        profiles = Profile.objects.all().filter(Q(username__contains=query))
        user_profile = Profile.objects.get(user=request.user)
        context = {
            'profiles': profiles, 'user_profile':user_profile,
        }
    return render(request, 'search.html', context)
