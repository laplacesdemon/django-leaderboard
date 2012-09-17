django-leaderboard
==================

A Django leaderboard (scoreboard) app, using redis as its backend. This app is a wrapper for the python-leaderboard api https://github.com/agoragames/python-leaderboard

The app uses Redis KVS for its back-end and stores the scores on its 'sorted set' data structure, which keeps the data ordered and allows us to retrieve, update and delete scores efficiently. 

With this app, you can get the leaderboard with pagination, create scores, update or delete them. Even get rankings around the given score.

Requirements
------------

Installation
------------

Usage
-----


Example
-------


