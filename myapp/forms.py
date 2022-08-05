from django import forms
from .models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'image', 'author', 'body')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'image', 'author', 'body')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'boby':forms.Textarea(attrs={'class':'form-control'}),
        }