from django.db import models


class User(models.Model):
    ROLE_CHOICES = [
        ('presenter', 'Presenter'),
        ('debater', 'Debater'),
        ('observer', 'Observer'),
    ]
    telegram_id = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=100, default="no username")
    age = models.PositiveIntegerField(blank=True, null=True)
    certificate = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_registered = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    language = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        blank=True,
        null=True,
        default='observer'
    )

    def __str__(self):
        return f"{self.first_name} {self.user_name} ({self.phone_number})"
