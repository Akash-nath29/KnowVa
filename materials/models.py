from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Material(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Add this line
    file = models.FileField(upload_to='materials/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_materials', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_materials', blank=True)

    def total_likes(self):
        return self.likes.count()
    
    def total_dislikes(self):
        return self.dislikes.count()

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse("material-detail", kwargs={"pk": self.pk})
