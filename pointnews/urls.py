"""
Definition of urls for pointnews.
"""

from datetime import datetime
from django.conf.urls import url,include
from rest_framework import routers,viewsets,serializers
from app.models import PostTb01
import django.contrib.auth.views
#from django.contrib.auth.models import User
import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=PostTb01
        field=('site','heading','post_link','post_date')

#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = User
#        fields = ('url', 'username', 'email', 'is_staff')

#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    print(queryset)
#    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset=PostTb01.objects.all()
    serializer_class=PostSerializer

router=routers.DefaultRouter()
router.register(r'posts',PostViewSet)
#router.register(r'users', UserViewSet)









urlpatterns = [
    # Examples:
    url(r'^api', include(router.urls)),
    url(r'^$', app.views.myhomePage.as_view(), name='home'),
    url(r'^(?P<id>\w+)/$',app.views.postdetail,name='postdetail'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    
    #url(r'^users$', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
