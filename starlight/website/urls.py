from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
	url(r'^$', views.indexView, name='index'),
	url(r'^gallery/$', views.galleryView, name='gallery'),
	url(r'^gallery/(?P<cat_name>[A-Za-z]+)/$', views.categoryView, name='category'),#DetailView.as_view(), name='detail'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
