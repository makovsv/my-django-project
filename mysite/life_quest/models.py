from django.db import models

class LifeProfile(models.Model):
    myusername = models.CharField(max_length=30)
    birth_year = models.DateField(auto_now=False,auto_now_add=False)
    gender = models.BooleanField(default=True)
    calc_result = models.IntegerField(default=11)

    def __str__ (self):
         return "Пользователь %s %s %s %s" % (self.myusername, self.birth_year, self.gender, self.calc_result)

    class Meta:
        verbose_name = 'Life_Profile'
        verbose_name_plural = 'Life_Profiles'


class CalcModel(models.Model):
    calc_method = models.IntegerField(default = 0)
