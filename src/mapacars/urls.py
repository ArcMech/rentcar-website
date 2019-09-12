
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from post.views import (index, blog, post, help, shop, contact)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name='post_list'),
    path('post/<id>', post, name='post-detail'),
    path('help/', help),
    path('shop/', shop),
    path('contact/', contact)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
