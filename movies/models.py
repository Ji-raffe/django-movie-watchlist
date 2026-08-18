from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Movie(models.Model):

    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, null=True, blank=True)
    release_year = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1888), MaxValueValidator(2100)]
    )
    personal_rating = models.PositiveSmallIntegerField(
        choices=[
            (1, '1 - Poor'),
            (2, '2 - Disappoint'),
            (3, '3 - Average'),
            (4, '4 - Enjoyable'),
            (5, '5 - Masterpiece'),
        ],
        null=True,
        blank=True
    )
    is_watched = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_added']
