from django import forms
from django.core.validators import RegexValidator

class UserComment(forms.Form):
    name = forms.CharField(max_length=10, label='Имя')
    nerobot = forms.BooleanField(error_messages={'required':'поставьте галочку'})
    comment = forms.CharField(widget=forms.Textarea, label='комментарий',
                              min_length=10,
                              error_messages={'min_length':'мин 10 символов'})
    email = forms.EmailField(required=False, validators=[
        RegexValidator('^[A-Za-z0-9_]{1,100}(@){1}(mail.ru){1}$', message='неправильный email')
    ])

def f1(value):
    if value[0]!='#':
        raise forms.ValidationError('нужна # в начале')
    if len(value)!=4:
        raise forms.ValidationError('нужно 4 символа')
    if not value[1:].isdigit():
        raise forms.ValidationError('нужно написать цифры')
    pass


class UserTel(forms.Form):
    name = forms.CharField(max_length=10, label='Имя')
    tel = forms.CharField(label='телефон', validators=[
        RegexValidator('^[+][7]{1}[0-9]{10}$', message='неправильный телефон')
    ])
    code = forms.CharField(max_length=4, label='секретный код',
                           widget=forms.TextInput(attrs={'placeholder': '#000'}),
                           validators=[f1])
    vibor=(('super','super'),('based','based'))
    tarif = forms.ChoiceField(choices=vibor)

class UserNew(UserTel):
    new = forms.CharField()