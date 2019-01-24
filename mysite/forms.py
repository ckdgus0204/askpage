from django import forms
from .models import Me, Ask,Comment

class MeForm(forms.ModelForm):
    class Meta:
        model =Me
        fields = {'title','text',}

class AskForm(forms.ModelForm):
    class Meta:
        model =Ask
        fields = {'nickname','text',}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'nickname','text',}