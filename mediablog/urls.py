from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from blog.views import post_list, post_detail, search
urlpatterns = [
    path('', post_list, name='post-list'),
    path('post/<id>/', post_detail, name='post-detail'),
    path('search/', search, name='search'),
    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)