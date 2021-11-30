from django.forms import ModelForm, TextInput, EmailInput
from django.forms.utils import ErrorList
from store.models import Contact

#from .models import Contact

class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="small error">%s</p>' % e for e in self])

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email"]
        widget = {
            'name' : TextInput(attrs={'class': 'form-contral'}),
            'email' : EmailInput(attrs={'class': 'form-contral'})
        }