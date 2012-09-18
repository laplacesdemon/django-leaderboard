from django import forms

class ScoreForm(forms.Form):
    user_id = forms.IntegerField(required=True, help_text="The id of the user")
    score = forms.IntegerField(required=True, help_text="Score as positive integer")
