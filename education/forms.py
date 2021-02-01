from django.db.models import fields
from django.forms import ModelForm
from .models import HomeWorkAnswer

# Create the form class.
class HomeWorkAnswerForm(ModelForm):
    class Meta:
        model = HomeWorkAnswer
        fields = ['student','home_work','answer_file','answer_text']
 