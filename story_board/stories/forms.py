from django.forms import ModelForm, CharField, TextInput, Textarea

from .models import Story


class Story_Form(ModelForm):
    """docstring for Post_Form"""

    title = CharField(max_length=250, widget=TextInput(
        attrs={
            "type": "text",
            "class": "form-control",
            "id": "TitleTextArea",
            "maxlength": 60,
            "placeholder": "E.g. 'My First Title'"},), required=True,)

    body = CharField(max_length=1000, widget=Textarea(
        attrs={
            "class": "form-control",
            "id": "levelCommentsControlTextarea1",
            "placeholder": "Add body here",
            "rows": 5, },), required=True,)

    class Meta:
        """docstring for Meta"""
        model = Story
        fields = ['title', 'body', 'user', ]