from django import forms
from tasks.models import Task, Comment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "end_time"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

        self.fields["end_time"].widget.attrs["class"] += " "


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control", "placeholder": "Write your comment here..."})
        }