import os
from django.test import TestCase
from django.conf import settings

# Create your tests here.
filepath = os.path.join(settings.MEDIA_ROOT, 'test.jpg')
print (filepath)
