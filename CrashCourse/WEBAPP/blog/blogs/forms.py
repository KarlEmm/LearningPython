from django.forms import ModelForm, Textarea
from .models import BlogPost

class BlogPostForm(ModelForm):
  class Meta:
    model = BlogPost
    fields = ['title', 'content']
    widgets = {
      'content': Textarea(attrs={'cols': 80, 'rows': 20}),
    }