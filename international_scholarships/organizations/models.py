from django.db import models

# Create your models here.


class Organization(models.Model):

    social_nets = [
        ('Facebook', 'Facebook'),
        ('Twitter', 'Twitter'),
        ('Instagram', 'Instagram'),
        ('TikTok', 'TikTok')
    ]

    name_org = models.CharField(max_length = 50)
    headquarters = models.CharField(max_length = 50)
    email_org = models.EmailField(max_length = 50)
    phone_org = models.CharField(max_length = 20)
    website_org = models.CharField(max_length = 50)
    social_media = models.CharField(max_length = 50, choices = social_nets)
    socialmed_name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'organizations'
    
    def __str__(self):
        return self.name_org