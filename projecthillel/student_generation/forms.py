from django import forms

from student_generation.models import CreateStudent


class StudentForm(forms.ModelForm):
    class Meta:
        model = CreateStudent
        fields = ["first_name", "last_name", "birth_date"]
        labels = {
            "first_name": "Ім'я",
            "last_name": "Прізвище",
            "birth_date": "Дата народження",
        }

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if len(first_name) > 50:
            raise forms.ValidationError(
                "Name is too long, max length is 50/Ім'я занадто вилеке, максимальна довжина 50"
            )

        if any(char.isdigit() for char in first_name):
            raise forms.ValidationError(
                "The name must not contain any numbers/Ім'я не повинно мати цифр"
            )
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if len(last_name) > 30:
            raise forms.ValidationError(
                "Last name is too long, max length is 50/Прізвище занадто велике, максимальна довжина 50"
            )
        if any(char.isdigit() for char in last_name):
            raise forms.ValidationError(
                "The last name must not contain any numbers/Прізвище не повинно мати цифр"
            )
        return last_name


class AddToGroup(forms.ModelForm):
    class Meta:
        model = CreateStudent
        fields = ["group"]
