# blog/models.py
from django.utils import timezone
from autoslug import AutoSlugField
from django import forms
from django.contrib.auth.models import User

from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    """A blog article model."""
    title = models.CharField(max_length=75)
    slug = AutoSlugField(populate_from='title')
    content = RichTextUploadingField(max_length=2000)
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        """Return the title."""
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(Article, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    related_paper = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(editable=False)

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(Comment, self).save(*args, **kwargs)


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'related_paper', 'author']
        widgets = {'related_paper': forms.HiddenInput(),
                   'author': forms.HiddenInput()
                   }
