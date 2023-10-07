from django import forms

from school.models import Groups


class TeachersForm(forms.Form):
    first_name = forms.CharField(label="Ім'я")
    surname = forms.CharField(label="Прізвище")
    patronymic = forms.CharField(label="По батькові")
    birth_date = forms.DateField(label="Дата народження")
    subject = forms.CharField(label="Назва предмету")

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if len(first_name) > 30:
            raise forms.ValidationError(
                "Name is too long, max length is 30/Ім'я занадто вилеке, максимальна довжина 30"
            )
        if any(char.isdigit() for char in first_name):
            raise forms.ValidationError(
                "The name must not contain any numbers/Ім'я не повинно мати цифр"
            )

    def clean_surname(self):
        surname = self.cleaned_data["surname"]
        if len(surname) > 30:
            raise forms.ValidationError(
                "Surname is too long, max length is 30/Прізвище занадто велике, максимальна довжина 30"
            )
        if any(char.isdigit() for char in surname):
            raise forms.ValidationError(
                "The surname must not contain any numbers/Прізвище не повинно мати цифр"
            )

    def clean_patronymic(self):
        patronymic = self.cleaned_data["patronymic"]
        if len(patronymic) > 30:
            raise forms.ValidationError(
                "Patronymic is too long, max length is 30/Прізвище по батькові занадто велике, максимальна довжина 30"
            )
        if any(char.isdigit() for char in patronymic):
            raise forms.ValidationError(
                "The patronymic must not contain any numbers/Прізвище по батькові не повинно мати цифр"
            )

    def clean_subject(self):
        subject = self.cleaned_data["subject"]
        if len(subject) > 100:
            raise forms.ValidationError(
                "Subject name is too long, max length is 100/Назва предмету занадто велика, максимальна довжина 100"
            )


class GroupsForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ["group_name", "curator"]
