from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    email      = models.EmailField(primary_key=True)
    phone      = models.IntegerField()
    password   = models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.first_name + " " +self.last_name
    
class Bid(models.Model):
    headline = models.CharField(max_length=100)
    posted_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='bid_last_owner')
    bid_description = models.CharField(max_length=2000)
    start_price = models.IntegerField(default=0)
    sold_price = models.IntegerField(default=0, editable=False)
    bought_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='bid_curr_owner')

    #Each user can participate in many auctions and each auction can have many users
    #So, this confirms many-to-many relationship between User and Bid
    bidders = models.ManyToManyField(User)

    def __str__(self) -> str:
        return self.headline



