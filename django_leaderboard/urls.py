from django.conf.urls.defaults import *

urlpatterns = patterns('django_leaderboard.views',
    # Api for creating a score
    url(r'^api/create-score/?$', 'api_create_score', name="leaderboard_create_score"),

    # Api for creating a score
    url(r'^api/update-score/?$', 'api_update_score', name="leaderboard_update_score"),

    # Api for deleting a score
    url(r'^api/delete-score/?$', 'api_delete_score', name="leaderboard_delete_score"),

    # Api the leaderboard for the user
    url(r'^api/user/(?P<game>[\w.@+-]+)/(?P<username>[\w.@+-]+)/$', 'api_leaderboard_for_user', name="leaderboard_for_user"),

    # Api for the leaderboard for the high scores
    url(r'^api/highscores/(?P<game>[\w.@+-]+)/$', 'api_leaderboard_high_scores', name="leaderboard_high_scores"),
    url(r'^api/highscores/(?P<game>[\w.@+-]+)/(?P<page>[\w.@+-]+)/$', 'api_leaderboard_high_scores', name="leaderboard_high_scores_with_page"),

    # the leaderboard for the high scores
    url(r'^highscores/(?P<game>[\w.@+-]+)/(?P<page>[\w.@+-]+)/$', 'leaderboard_high_scores', name="leaderboard_high_scores"),
)
