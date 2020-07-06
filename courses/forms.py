from django import forms


class QuestionForm(forms.Form):
    email = forms.EmailField()
    question = forms.CharField(widget=forms.Textarea, max_length=255, required=True)