from django.db import models
import uuid
# Create your models here.



class OCRHistory(models.Model):
    uid = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    image = models.ImageField(upload_to="ocrimages/")
    file = models.FileField(upload_to="files/")

    def __str__(self):
        return self.image