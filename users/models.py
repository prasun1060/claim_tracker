from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    DESIGNATION_CHOICES = [
        ('MANAGER', 'Manager'),
        ('SUPERVISOR', 'Supervisor'),
        ('ASSOCIATE', 'Associate'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=20, choices=DESIGNATION_CHOICES, default="ASSOCIATE")
    
    def __str__(self):
        return f'{self.user.username}\'s profile'

class TeamMember(models.Model):
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="supervisor")
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name="member")

    def __str__(self):
        return f'{self.supervisor.username}\'s member: {self.member.username}'