from django.forms import ModelForm

class NameForm(ModelForm):
    your_name = forms.CharField(label='Your name', max_length=100)
    
class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=['name','title','birth_date']
