from django import forms

from testeinoa.models import Asset


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ('asset_code', 'tunel_max', 'tunel_min', 'update_frequency', 'email')
        widgets = {
            'asset_code': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 330px;',
                'placeholder': 'Código do Ativo'
                }),
            'tunel_max': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Túnel Máximo'}),
            'tunel_min': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Túnel Mínimo'}),
            'update_frequency': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Taxa de Verificação (min)'
                }),
            'email': forms.EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                })
        }
        
    def clean(self):
            cleaned_data = super().clean()
            tunel_max = cleaned_data.get("tunel_max")
            tunel_min = cleaned_data.get("tunel_min")

            if tunel_max and tunel_min:
                if tunel_min >= tunel_max:
                    raise forms.ValidationError(
                        'Túnel máximo deve ser maior que mínimo.'
                    )