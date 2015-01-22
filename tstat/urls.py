from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('dash.views',
                       url(r'^homework/$', 'homework'),
                       # Examples:
                       # url(r'^$', 'tstat.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       )

urlpatterns += patterns('tracker.views',
                        url(r'^tracker/', 'tracker'),
                        )
