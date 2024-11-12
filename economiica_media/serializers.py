from rest_framework import serializers
from .models import EconomiicaMedia


class EconomiicaMediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = EconomiicaMedia
        fields = [
            "id",
            "title",
            "description",
            "image_url",
            "video_url",
            "created_at",
            "created_at",
        ]

        def validate_text(self, value):
            if EconomiicaMedia.objects.filter(text=value).exists():
                raise serializers.ValidationError("Duplicate message detected")
            return value
