from django import forms
from .models import reviews

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "required": "Your name must not be empty!",
#         "max_length": "Pls enter a shorter name!"
#     })
#     review_text = forms.CharField(label="Your Feedback", max_length=200, widget=forms.Textarea)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = reviews
        fields = "__all__" #["user_name", "review_text", "rating"]
        #exclude = "owner_comment"
        labels = {
            "user_name":"Your Name",
            "review_text":"Your Feedback",
            "rating":"Your Rating"
        }

        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "Pls enter a shorter name!"
            }
        }