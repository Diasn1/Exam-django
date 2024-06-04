from django import forms
from .models import Post, Comment, Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:  # Минимальное количество символов для поста
            raise forms.ValidationError('Content should have at least 10 characters.')
        return content

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 5:  # Минимальное количество символов для комментария
            raise forms.ValidationError('Content should have at least 5 characters.')
        return content

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
