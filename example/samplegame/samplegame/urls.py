from django.http import HttpResponseRedirect
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Redirect to leaderboard
    url(r'^$', lambda r : HttpResponseRedirect('leaderboard/highscores/sample_game/')),

    # Leaderboard
    url(r'^leaderboard/', include('django_leaderboard.urls')),

    # auth support for rest framework
    url(r'^restframework', include('djangorestframework.urls', namespace='djangorestframework'))
)
