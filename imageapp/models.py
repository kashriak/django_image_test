from django.db import models

class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="images")#こちらの通り

    def __str__(self):
        return self.title
