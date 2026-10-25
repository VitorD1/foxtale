from django import forms

from stories.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['created_at']
        labels = {
            'title': 'Заглавие',
            'section': 'Секция',
            'occasion': 'Повод',
            'text': 'Текст',
            'image': 'Снимка',
            'products': 'Препоръчани продукти',
        }
        help_texts = {
            'occasion': 'Само за секция „Идеи“.',
            'image': 'По желание. JPG или PNG, до 5 MB.',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Подарък за сватба'}),
            'text': forms.Textarea(attrs={'placeholder': 'Поне 20 символа', 'rows': 6}),
            'products': forms.CheckboxSelectMultiple(),
        }
        error_messages = {
            'title': {
                'required': 'Въведи заглавие.',
                'min_length': 'Заглавието трябва да е поне 3 символа.',
            },
            'text': {
                'required': 'Въведи текст.',
                'min_length': 'Текстът трябва да е поне 20 символа.',
            },
            'section': {
                'required': 'Избери секция.',
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        section = cleaned_data.get('section')
        occasion = cleaned_data.get('occasion')

        if occasion and section != Article.Section.IDEAS:
            self.add_error('occasion', 'Повод се избира само за секция „Идеи“.')

        if section == Article.Section.ABOUT:
            others = Article.objects.filter(section=section).exclude(pk=self.instance.pk)
            if others.exists():
                self.add_error('section', 'Вече има статия „За мен“. Редактирай нея.')

        return cleaned_data


class ArticleEditForm(ArticleForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['section'].disabled = True


class ArticleDeleteForm(ArticleForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
