from django import forms
from .models import NewsletterSubscriber


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your email address',
                'class': 'bg-transparent border-b border-white/30 focus:border-primary py-3 px-1 text-sm outline-none flex-1 transition-colors'
            })
        }
