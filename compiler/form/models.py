from django.db import models
from .fields import NonStrippingTextField


class Code(models.Model):
    code = NonStrippingTextField()
