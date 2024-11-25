from django import forms
from .models import Comment,Reply,CommentReaction

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'message']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['name', 'message']

class CommentReactionForm(forms.ModelForm):
    class Meta:
        model = CommentReaction
        fields = ['like', 'dislike']
