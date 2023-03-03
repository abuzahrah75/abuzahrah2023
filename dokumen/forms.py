from django import forms

from .models import Dokumen

# class DokumenForm(forms.Form):
#     nama = forms.CharField()
#     keterangan = forms.Textarea()
#     status_dokumen = forms.ModelChoiceField(queryset=Dokumen.objects.all())

class Dokumen2Form(forms.ModelForm):
    class Meta:
        model = Dokumen
        fields = ['nama', 'keterangan','kategori', 'status_dokumen']