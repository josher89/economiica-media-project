from django.db import models


class EconomiicaMedia(models.Model):
    title = models.CharField(max_length=100, help_text="Media file title")
    description = models.TextField(blank=True, help_text="Media file description")
    image_url = models.URLField(
        max_length=200, blank=True, help_text="URL of the image"
    )
    video_url = models.URLField(
        max_length=200, blank=True, help_text="URL of the video"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Timestamp when the media was added"
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="Timestamp when the media was last updated"
    )

    def __str__(self):
        return self.title
