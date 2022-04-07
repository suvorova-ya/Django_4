from.models import Post
from django.forms import ModelForm,DateInput

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','text', 'author','dateCreation']


