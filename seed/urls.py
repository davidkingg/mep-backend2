
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.views.static import serve
#from django.conf.urls import url


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("mep.urls")),
    #path('api-auth/', include('rest_framework.urls')),
    # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += [re_path(r'^.*', TemplateView.as_view())]
