from django.db import models

class LifeProfile(models.Model):
    myusername = models.CharField(max_length=250)
    birth_year = models.IntegerField()
    smoking = models.BooleanField(default=True)

    def __str__ (self):
        return "Пользователь %s %s" % (self.myusername, self.birth_year)

    class Meta:
        verbose_name = 'Life_Profile'
        verbose_name_plural = 'Life_Profiles'
