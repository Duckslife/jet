from django.conf.urls import url
from django.urls import include

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$',views.post_list, name='post_list'),
]
