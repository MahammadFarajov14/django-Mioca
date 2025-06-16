from django.db.models.signals import post_save
from django.utils.text import slugify
from product.models import Product
from django.dispatch import receiver


@receiver(post_save, sender = Product)
def product_slug(created, instance, *args, **kwargs):
    if created:
        instance.slug = slugify(instance.title) + str(instance.id)
        if instance.quantity <= 0:
            instance.type = 'Not Avaible'
        elif instance.quantity > 0:
            print((instance.updated_date - instance.created_date).days)
            if (instance.updated_date - instance.created_date).days >= 10:
                instance.type = 'New'
            elif (instance.updated_date - instance.created_date).days < 10:
                instance.type = 'Sale'


        # if instance.u
        instance.save()