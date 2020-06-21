from django import forms

from .models import Post,Comment
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
        'text': SummernoteWidget(),
        'title': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '200px'}}),
    }

    
        

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author','email','text')
