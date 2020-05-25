from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DailyTracker(models.Model):
    MARKET_CHOICES = [
        ('IN', 'Indiana'),
        ('MD', 'Maryland'),
        ('NV', 'Nevada'),
        ('NY', 'New York'),
        ('WA', 'Washington'),
        ('CO', 'Colorado'),
    ]
    PLATFORM_CHOICES = [
        ('Facets', 'Facets'),
        ('CWS', 'CWS'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    claim_no = models.IntegerField()
    billed_charges = models.FloatField()
    benefit = models.FloatField()
    market = models.CharField(max_length=12, choices=MARKET_CHOICES, default= 'IN')
    platform = models.CharField(max_length=12, choices=PLATFORM_CHOICES, default='Facets')
    supervisor = models.CharField(max_length=50, default="Preetam Bagi")

    def __str__(self):
        return f'{self.user.username}s claim {self.claim_no}'
