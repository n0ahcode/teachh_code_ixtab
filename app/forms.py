from django import forms
from .models import CodeModel



class CodeModelForm(forms.ModelForm):
    class Meta:
        model = CodeModel
        fields = ['title','text','name','tags']
        widgets = {
                    'title':forms.TextInput(attrs={'placeholder':'記入例:title'}),
                    'text':forms.Textarea(attrs={'rows':4}),

        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)
