from django.db import models
from uuid import uuid4 as UUID4
from django.utils.timezone import now as djnow
from django.utils.text import slugify 


class Post(models.Model):
    uuid = models.UUIDField(default=UUID4,
                            editable=False,
                            primary_key=
                            True)
    title = models.CharField(max_length=55,
                             unique=True,
                             null=True,
                             blank=True,
                             editable=True,
                             help_text="title")
    content = models.TextField(max_length=2048,
                               editable=True,
                               blank=True,
                               null=True,
                               help_text="content")
    slug = models.SlugField(default="", null=False)
    created_at = models.DateTimeField(default=djnow,
                                      editable=False,
                                      help_text="created at")
    updated_at = models.DateTimeField(default=djnow,
                                      help_text="updated at")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
