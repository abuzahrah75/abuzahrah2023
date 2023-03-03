from django import forms

from .models import Tugasan

class TugasanForm(forms.ModelForm):
    class Meta:
        model = Tugasan
        fields = ['nama', 'st_tugas', 'kategori']
