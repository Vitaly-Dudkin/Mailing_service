from django import forms
from blog.models import Blog
from mailing.forms import StyleFormMixin


class BlogForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Blog
        exclude = ('views_number', 'publication_date')
