from django.db import models

#
# class FileModel(models.Model):
#     file = models.FileField(upload_to='uploads/')


class Gems(models.Model):
    gem = models.CharField(max_length=100)

    def __str__(self):
        return self.gem


class Clients(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Clean_data(models.Model):
    username = models.CharField(max_length=100)
    spent_money = models.IntegerField(default=0)
    gems = models.CharField(max_length=500, default='')


class ContentFile(models.Model):
    customer = models.ForeignKey(Clients,
                                 related_name='clients',
                                 on_delete=models.CASCADE)
    item = models.ForeignKey(Gems,
                             related_name='gems',
                             on_delete=models.CASCADE)
    total = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=False, auto_now=False)

