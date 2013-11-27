from django.conf.urls import patterns, url

urlpatterns = patterns('catalog.views',
    url(r'^export/$', "export_xsl", name='export_assets_xsl'),
    url(r'^json/$', "list_json", name='assets_json'),
    url(r'^$', "list", name='catalog'),
)
