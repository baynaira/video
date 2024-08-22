from django.db import models

class Video(models.Model):
    DIFFICULTY_CHOICES = (
        ('beginner', 'Beginner'),
        ('advanced', 'Advanced'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.title