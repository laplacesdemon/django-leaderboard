from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from decorators import json_view
from leaderboard import Leaderboard

def leaderboard_high_scores(request, game, page=1):
    """
    the html view for leaderboards
    """
    pass

@json_view
def api_leaderboard_high_scores(request, game, page=1):
    """
    the list of high scores
    """
    lb = Leaderboard(game)
    scores = lb.leaders(int(page))

    # Return empty array if no records found
    return scores if (scores) else []

@json_view
def api_leaderboard_for_user(request, username, game):
    """
    The scores around the user's high score
    """
    user = User.objects.get(username=username)
    lb = Leaderboard(game)
    scores = lb.around_me(user.pk)
    return scores if (scores) else []

@login_required
@require_http_methods(["POST"])
def api_create_score(request):
    """
    Json api for creating high score

    Params:
        user_id: user's primary key
        game: game identifier
        score: integer score
    """
    user_id = request.POST.get('user_id')
    game = request.POST.get('game')
    score = request.POST.get('score')
    user = User.objects.get(pk=user_id)
    lb = Leaderboard(game)
    success = lb.rank_mamber(user.pk, score)
    return {"result": success}

#@login_required
@require_http_methods(["POST"])
def api_update_score(request):
    """
    Json api for updating score
    """
    pass

@login_required
@require_http_methods(["POST"])
def api_delete_score(request):
    """
    Json api for deleting the score
    """
    pass
