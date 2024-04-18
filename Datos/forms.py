from django import forms
from .models import Area, Persona, Tonner, Retiro_Tonner

class FormArea(forms.ModelForm):
    class Meta:
        model = Area
        fields = '__all__'

class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class FormTonner(forms.ModelForm):
    class Meta:
        model = Tonner
        fields = '__all__'

class FormsRetiroTonner(forms.ModelForm):
    class Meta: 
        model = Retiro_Tonner
        fields = ['r_persona', 'cantidad_retirada']