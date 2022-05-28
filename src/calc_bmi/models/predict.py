from django.db import models

RESULT_CHOICES = (
    (1, 'dog'),
    (2, 'cat')
)

class Predict(models.Model):
    result = models.IntegerField(choices=RESULT_CHOICES)
    image = models.ImageField(
        upload_to="images/"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)