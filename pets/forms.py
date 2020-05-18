from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='Fist Name')
    last_name = forms.CharField(max_length=100, label='Last Name')
    email = forms.EmailField(label='Email', max_length=100)
    massage = forms.CharField(label='Message', widget=forms.Textarea(
        attrs={
            'placeholder': 'Leave Here Your Message'
        }
    ))
