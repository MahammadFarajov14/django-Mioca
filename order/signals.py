from django.db.models.signals import post_save
from order.models import Order, Basket
from django.dispatch import receiver

@receiver(post_save, sender=Order)
def order_slug(created, instance, *args, **kwargs):
    if created:
        instance.basket = Basket.objects.filter(user = instance.user, is_active = True).first()
        instance.save()