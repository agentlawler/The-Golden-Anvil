from django.db import models

# specifying choices

RARITY_CHOICES = (
    ("common", "Common"),
    ("uncommon", "Uncommon"),
    ("rare", "Rare"),
    ("very_rare", "Very Rare"),
    ("legendary", "Legendary"),
    ("artifact", "Artifact"),
    ("unknown", "Unknown Rarity"),
    ("vary", "Varies")
)


# Create your models here.

class User(models.Model):
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)
    username = models.CharField(max_length=50, null=False, blank = False)
    password = models.CharField(max_length=50, null=False, blank = False)
    name = models.TextField(max_length=50, null=False, blank = False)
    email = models.EmailField(max_length=75, null=False, blank = False)

    def __str__(self):
        return self.username


class Item(models.Model):
    name = models.CharField(max_length=100, null=False, blank = False)
    rarity = models.CharField(max_length=50, choices=RARITY_CHOICES, default="common")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    attunement = models.BooleanField()
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='cart')
    total = models.DecimalField(max_digits=12, decimal_places=2)