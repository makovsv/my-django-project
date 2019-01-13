from django.db import models

class Subscriber(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=132)

    def __str__ (self):
        return "Пользователь %s %s" % (self.email, self.name)

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'A lot of subsribers'
