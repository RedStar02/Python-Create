from django.forms import ModelForm
from app.models import Login

# Create the form class.
class CarrosForm(ModelForm):
    class Meta:
        model = Login
        fields = ['name', 'email', 'password', 'birthday']