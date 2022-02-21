from django import forms


class RollValidation(forms.Form):

    def clean(self):
        cleaned_data = super().clean()
        rollno = cleaned_data.get("roll_number")

        if rollno < 1000:
            print("Enter number greater than 1000.")

        if rollno > 9999:
            print("Enter number smaller than 9999.")