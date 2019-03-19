from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url(r'^$',views.article,name='photosToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photos,name = 'pastPhotos'),
    url(r'^search/', views.search_category, name='search_category'),  
    url(r'^^media\/', views.display_location, name='display_location'), 
    url(r'^article/(\d+)',views.article,name ='article')
 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
