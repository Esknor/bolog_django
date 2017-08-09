from django.conf.urls import url, include
from django.contrib import admin
import blog, logoginsys

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'', include('blog.urls')),
	url(r'^auth/', include('logoginsys.urls')),
]
