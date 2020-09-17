# blog/models.py
from django.db import models

class Article(models.Model):
    """A blog article model."""
    title = models.CharField(max_length=75)
    content = models.TextField()
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        """Return the title."""
        return self.title
