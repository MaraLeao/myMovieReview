from django import forms

class MovieSearchForm(forms.Form):
    title = forms.CharField(label='Title', max_length=255)

class ReviewForm(forms.Form):
    userName = forms.CharField(label='User Name', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}))
    userRating = forms.IntegerField(label='User Rating (1-5)', min_value=1, max_value=5, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    userReview = forms.CharField(label='User Review', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your review here'}))

