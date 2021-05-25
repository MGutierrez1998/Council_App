from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import Council
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    PROGRESS_REPORT = (
        ('Request', 'Request'),
        ('In Progress', 'In Progress'),
        ('Complete', 'Complete'),
    )
    FAULT_REPORT = [
        ('Waste', 'Waste'),
        ('Graffiti', 'Graffiti'),
        ('Vehicles and Parking', 'Vehicles and Parking'),
        ('Damaged Footpath', 'Damaged Footpath'),
        ('Tree Maintenance', 'Tree Maintenance'),
        ('Other', 'Other'),
    ]

    progress = models.CharField(default='Request',max_length=11, choices=PROGRESS_REPORT)
    problem = models.CharField(max_length=20, choices=FAULT_REPORT)

    street_num = models.IntegerField()
    street_name = models.CharField(max_length=100)
    suburb = models.CharField(max_length=50)

    image = models.ImageField(upload_to='images', blank=True)

    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.progress} for {self.problem} at {self.council}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

    """ Commented out
    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)"""
