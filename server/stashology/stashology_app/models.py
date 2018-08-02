import uuid
from django.db import models


class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["created_at"])
        ]


class Finish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["created_at"])
        ]


class Color(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["created_at"])
        ]


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["created_at"])
        ]


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    caption = models.CharField(max_length=255, null=False)
    NATURAL = "N"
    ARTIFICIAL = "A"
    LIGHTING_TYPES = (
        (NATURAL, "Natural"),
        (ARTIFICIAL, "Artificial")
    )
    lighting_type = models.CharField(
        max_length=1,
        choices=LIGHTING_TYPES,
        default=NATURAL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.caption} with lighting type {self.lighting_type}"

    class Meta:
        indexes = [
            models.Index(fields=["lighting_type"]),
            models.Index(fields=["created_at"])
        ]


# Polish
# {
# Id: string,
# Name: string,
# Brand: Brand,
# Finish: Finish,
# Colors: Array<Color>,
# Photos: {
# 	Natural light: Array<Photo>,
# 	Artificial light: Array<Photo>,
# 	In use: Array<Photo>
# },
# Tags: Array<Tag>
# }

class Polish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    finish = models.ForeignKey(Finish, on_delete=models.CASCADE)
    colors = models.ManyToManyField(Color)
    photos = models.ManyToManyField(Photo)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} by {self.brand.name}"

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["brand"]),
            models.Index(fields=["finish"]),
            models.Index(fields=["colors"]),
            models.Index(fields=["tags"]),
            models.Index(fields=["created_at"])
        ]
