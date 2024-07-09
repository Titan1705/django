from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name,  fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class']  = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('views_counter',)

    forbidden_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for name in self.forbidden_words:
            if name in cleaned_data:
                raise forms.ValidationError('Нельзя создавать продукты с запрещенными словами')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for description in self.forbidden_words:
            if description in cleaned_data:
                raise forms.ValidationError('Нельзя создавать продукты с запрещенными словами')

        return cleaned_data


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"