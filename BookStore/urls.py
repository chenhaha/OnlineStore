from django.conf.urls import url
from BookStore import views
#from django.contrib import admin


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^cart/$', views.cart, name='about'),
    url(r'^category/$', views.category, name='category'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^myaccount/$', views.myaccount, name='myaccount'),
    url(r'^register/$', views.register, name='register'),
    url(r'^specials/$', views.specials, name='specials'),
    url(r'^details/$', views.details, name='details'),
]