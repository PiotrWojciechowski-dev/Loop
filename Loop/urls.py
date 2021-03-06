"""Loop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user.views import SignUpView, SignInView, SignOutView, UserDelete, change_password
import profiles.urls 
from post.views import HomeView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('logout/', SignOutView.as_view(), name='signout'),
    path('changePassword/', change_password, name='change_password'),
    path('delete_user/<int:pk>', UserDelete.as_view(), name='delete_user'),
    path('', include('post.urls')),
    path('user/', include('user.urls')),
    path('search/', include('search.urls')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('likes/', include('likes.urls')),
    path('messages/', include('private_messages.urls', namespace='messaging')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('shop/', include('shop.urls', namespace='shop')),
    path('order/', include('order.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('groupchat/', include('groupchat.urls', namespace='groupchat'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)