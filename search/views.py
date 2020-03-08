from django.shortcuts import render
from profiles.models import Profile
from django.db.models import Q
# Create your views here.

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
            'profiles': profiles, 'user_profile':user_profile
        }
    return render(request, 'search.html', context)
