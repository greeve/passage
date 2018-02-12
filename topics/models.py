from django.db import models
from . import constants


class Term(models.Model):
    label = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    source = models.URLField(max_legth=255)
    related_terms = models.ForeignKey('self', on_delete=models.CASCADE)


class Reference(models.Model):
    label = models.CharField(max_length=255)
    term = models.ForeignKey('Term', related_name='references')
    category = models.CharField(
        max_length=1,
        choices=constants.CATEGORY_CHOICES,
        default=constants.SCRIPTURE,
    )

    # Scripture reference fields
    volume = models.CharField(
        max_length=3,
        choices=constants.VOLUME_CHOICES,
        default=constants.BOM,
        null=True,
    )
    book = models.CharField(max_length=50, null=True)
    chapter = models.PositiveSmallIntegerField(null=True)
    verses = models.CharField(max_length=255, null=True)

    # Hymn reference fields
    hymn_number = models.PositiveSmallIntegerField(null=True)

    # Conference address fields
    year = models.PositiveSmallIntegerField(null=True)
    month = models.PositiveSmallIntegerField(
        choices=constants.MONTH_CHOICES,
        default=constants.APRIL,
        null=True,
    )
    session = models.CharField(
        max_lenth=5,
        choices=constants.SESSION_CHOICES,
        default=constants.SAT_AM,
        null=True,
    )
    speaker = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
