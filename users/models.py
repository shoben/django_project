from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField( default='default.png', upload_to = 'profile_pics')

  def __str__(self):
    return f'{self.user.username} Profile'

  def save(self):
    super().save()

    img = Image.open(self.image.path)

    IMG_MAX = 150

    if img.height > IMG_MAX or img.width > IMG_MAX:
      output_size = (IMG_MAX, IMG_MAX)
      img.thumbnail(output_size)
      img.save(self.image.path)
