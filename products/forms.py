from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

from products.models import Category, Occasion, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        labels = {
            'name': 'Име',
            'description': 'Описание',
        }
        help_texts = {
            'name': 'Само букви и интервали, напр. „Свещници“.',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Свещници'}),
            'description': forms.Textarea(attrs={'placeholder': 'Кратко описание на категорията', 'rows': 3}),
        }
        error_messages = {
            'name': {
                'unique': 'Вече има категория с това име.',
                'required': 'Въведи име на категорията.',
            },
        }


class OccasionForm(forms.ModelForm):
    class Meta:
        model = Occasion
        fields = ['name']
        labels = {
            'name': 'Повод',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Рожден ден'}),
        }
        error_messages = {
            'name': {
                'unique': 'Този повод вече съществува.',
                'required': 'Въведи име на повода.',
            },
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at']
        labels = {
            'title': 'Име на продукта',
            'category': 'Категория',
            'occasions': 'Подходящ за',
            'description': 'Описание',
            'price': 'Цена (€)',
            'image': 'Снимка',
            'is_available': 'Наличен',
        }
        help_texts = {
            'image': 'JPG или PNG, до 5 MB.',
            'occasions': 'Може да избереш няколко повода.',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Бутилка „Лавандула“'}),
            'occasions': forms.CheckboxSelectMultiple(),
            'description': forms.Textarea(attrs={'placeholder': 'Материали, размери, техника', 'rows': 4}),
            'price': forms.NumberInput(attrs={'placeholder': '24.50', 'step': '0.01'}),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': 'В тази категория вече има продукт с това име.',
            },
            'title': {
                'required': 'Въведи име на продукта.',
            },
            'price': {
                'required': 'Въведи цена.',
                'min_value': 'Цената не може да е отрицателна.',
            },
            'image': {
                'required': 'Качи снимка на продукта.',
                'invalid_image': 'Файлът не е снимка.',
            },
        }


class ProductEditForm(ProductForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].disabled = True
        self.fields['category'].help_text = 'Категорията не може да се сменя.'


class ProductFilterForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label='Всички категории',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    occasion = forms.ModelChoiceField(
        queryset=Occasion.objects.all(),
        required=False,
        empty_label='Всички поводи',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    sort = forms.ChoiceField(
        choices=[
            ('', 'Най-нови'),
            ('price', 'Цена: ниска към висока'),
            ('-price', 'Цена: висока към ниска'),
            ('title', 'По име'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )



