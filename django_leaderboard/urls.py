from django.conf.urls.defaults import *
from django_leaderboard.views import ScoresView, ScoresAroundMeView

urlpatterns = patterns('django_leaderboard.views',
    # Api urls
    #url(r'^$', ScoresView.as_view(), name='leaderboard_api'),
    url(r'^api/(?P<game>[\w.@+-]+)/user/(?P<user_id>[\w.@+-]+)/', ScoresAroundMeView.as_view(), name='leaderboard_around_me_api'),
    url(r'^api/(?P<game>[\w.@+-]+)/$', ScoresView.as_view(), name='leaderboard_api'),
    url(r'^api/(?P<game>[\w.@+-]+)/(?P<page>[0-9]+)/$', ScoresView.as_view(), name='leaderboard_api_with_page'),

    # the leaderboard for the high scores
    url(r'^highscores/(?P<game>[\w.@+-]+)/$', 'highscores', name="leaderboard_high_scores"),
    url(r'^highscores/(?P<game>[\w.@+-]+)/(?P<page>[\w.@+-]+)/$', 'highscores', name="leaderboard_high_scores_with_page"),
)
