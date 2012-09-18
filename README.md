django-leaderboard
==================

A Django leaderboard (scoreboard) app, using redis as its backend. This app is a wrapper for the python-leaderboard api https://github.com/agoragames/python-leaderboard

The app uses Redis KVS for its back-end and stores the scores on its 'sorted set' data structure, which keeps the data ordered and allows us to retrieve, update and delete scores efficiently. 

With this app, you can get the leaderboard with pagination, create scores, update or delete them. Even get rankings around the given score.

Features
--------

  * RESTful api for creating, updating, deleting and retrieving high scores or scores around the user
  * Standard view for displaying high scores with pagination

Not implemented features
------------------------

  * delete method for the api

Requirements
------------

Python leaderboards module `pip install leaderboard`, note that this module will install redis and hiredis modules as its dependancy
djangorestframework `pip install djangorestframework` for providing the rest behavior. 

Installation
------------

  * Add the `django_leaderboard` folder to your path.
  * Add `django_leaderboard` to APPS list in settings.py
  * Make sure that your redis server is running.
  * Add following lines to your urls.py file.
  * Run `python manage.py runserver` to test it out.

    url(r'^leaderboard/', include('django_leaderboard.urls')),
    # auth support for rest framework
    url(r'^restframework', include('djangorestframework.urls', namespace='djangorestframework'))
    
Usage
-----

Thanks to `djangorestframeword`, you can just visit `http://localhost:8000/leaderboard/api/<game-identifier>/` to create, update or get the leaderboard.

Other urls are `http://localhost:8000/leaderboard/api/<game-identifier>/user/<user-id>/` for scores around the user, and `http://localhost:8000/leaderboard/api/<game-identifier>/<page-id>/` for pagination. Please see `urls.py` to see the full list or urls.

To create new ranking using the api, send a POST request to `http://localhost:8000/leaderboard/api/<game-identifier>/`. Game identifier is the key to determine your game to the system. it can be anything. Parameters are `user_id`and `score`.  
To see the html table of leaderboard, go to `http://localhost:8000/leaderboard/highscores/<game-identifier>/` page.

Example
-------

There is an example project in the source to make it easy to start.

Contributions
-------------

Please feel free to contribute.
