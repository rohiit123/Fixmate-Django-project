from django import forms
from .models import Worker


class WorkerForm(forms.ModelForm):

    class Meta:
        model = Worker

        fields = [
            "service",
            "experience",
            "starting_price",
            "about",
            "address",
            "profile_photo",
            "available",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

        self.fields["available"].widget.attrs["class"] = "form-check-input"

        self.fields["about"].widget.attrs.update({
            "rows": 5,
            "placeholder": "Tell customers about yourself..."
        })