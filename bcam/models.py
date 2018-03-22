from django.db import models

# Create your models here.
def upload_location (instance, filename):
    return "%s" %( filename )

class Image(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(
		upload_to=upload_location,
		null=True,
		blank=True,
		)
