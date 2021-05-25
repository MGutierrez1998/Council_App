from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Council(models.Model):
    COUNCIL_OPTION = [
        ('Albury', 'Albury'),
        ('Armidale Regional', 'Armidale Regional'),
        ('Ballina', 'Ballina'),
        ('Balranald', 'Balranald'),
        ('Bathurst Regional', 'Bathurst Regional'),
        ('Bega Valley', 'Bega Valley'),
        ('Bellingen', 'Bellingen'),
        ('Blacktown', 'Blacktown'),
        ('Bland', 'Bland'),
        ('Blue Mountains', 'Blue Mountains'),
        ('Broken Hill', 'Broken Hill'),
        ('Byron', 'Byron'),
        ('Cabonne', 'Cabonne'),
        ('Campbelltown', 'Campbelltown'),
        ('Canada Bay', 'Canada Bay'),
        ('Canterbury-Blacktown', 'Canterbury-Blacktown'),
        ('Carrathool', 'Carrathool'),
        ('Central Coast', 'Central Coast'),
        ('Cessnock', 'Cessnock'),
        ('Cobar', 'Cobar'),
        ('Coffs Harbour', 'Coffs Harbour'),
        ('Cumberland', 'Cumberland'),
        ('Eurobodalla', 'Eurobodalla'),
        ('Fairfield', 'Fairfield'),
        ('Gunnedah', 'Gunnedah'),
        ('Gwydir', 'Gwydir'),
        ('Inner West', 'Inner West'),
        ('Kyogle', 'Kyogle'),
        ('Lachlan', 'Lachlan'),
        ('Lithgow', 'Lithgow'),
        ('Liverpool', 'Liverpool'),
        ('Moore Plains', 'Moore Plains'),
        ('Mosman', 'Mosman'),
        ('Murray River', 'Murray River'),
        ('North Sydney', 'North Sydney'),
        ('Northern Beaches', 'Northern Beaches'),
        ('Parramatta', 'Parramatta'),
        ('Snowy Monaro Regional', 'Snowy Monaro Regional'),
        ('Strathfield', 'Strathfield'),
        ('Sydney', 'Sydney'),
        ('Tamworth Regional', 'Tamworth Regional'),
        ('Weddin', 'Weddin'),
        ('Wollondilly', 'Wollondilly'),
        ('Wollongong', 'Wollongong'),
        ('Woollahra', 'Woollahra'),
        ('Yass Valley', 'Yass Valley'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    council = models.CharField(max_length=21, choices=COUNCIL_OPTION)

    def __str__(self):
        return f'{self.council}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
