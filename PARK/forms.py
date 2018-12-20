from django import forms
from PARK.models import User

class NewUserForms(forms.ModelForm):
          domain=forms.ChoiceField(choices=[('Clothing','Clothing'),
                    ('Toiltries','Toiltries',),
                    ('Footware','Footware',),
                    ('Study Material','Study Material',),
                    ('Grocery','Grocery',)])
          class Meta():
                    model = User
                    fields = '__all__'
          