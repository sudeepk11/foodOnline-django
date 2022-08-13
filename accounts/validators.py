from django.core.exceptions import ValidationError
import os


def allow_only_images_validator(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.PNG', '.JPG', 'JPEG']
    if not ext.upper() in valid_extensions:
        raise ValidationError('Unsupported File Extension, Only .jpg , .jpeg and .png files are allowed')

