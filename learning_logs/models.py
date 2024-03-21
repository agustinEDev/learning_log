from django.db import models

class Topic(models.Model):
    """Un tema sobre el que está aprendiendo el usuario."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Devuelve una representacion del modelo como cadena."""
        return self.text


