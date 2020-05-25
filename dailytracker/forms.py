from django.forms import ModelForm
from .models import DailyTracker

class TrackerForm(ModelForm):

    class Meta:
        model = DailyTracker
        exclude = ['user', 'date', 'supervisor']