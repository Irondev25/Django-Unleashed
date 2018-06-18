from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'tag': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
            'startup': forms.SelectMultiple(attrs={
                'class':'form-control'
            })
        }
    
    def clean_slug(self):
        return self.cleaned_data['slug'].lower()
