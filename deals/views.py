import pandas as pd
from rest_framework import generics, views
from rest_framework.response import Response


from . import serializers as deals_ser
from . import models


class FileUpload(generics.CreateAPIView):
    serializer_class = deals_ser.FileSerializer

    def get(self, request, *args, **kwargs):
        data = self.create_clean_data_model()
        result = data.values('username', 'spent_money', 'gems')[:5]

        return Response({'data': result}, status=200)

    def post(self, request, *args, **kwargs):
        self.clear_data()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']

        try:
            self.parse(file)
        except AttributeError:
            return Response({'Ошибка': 'В процессе обработки файла произошла ошибка'})

        return Response({'Ответ': 'Файл обработан без ошибок'}, status=200)


    def parse(self, file):
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            if not models.Clients.objects.filter(username=row['customer']).exists():
                new_client = models.Clients(
                    username=row['customer']
                )
                new_client.save()

            if not models.Gems.objects.filter(gem=row['item']).exists():
                new_gem = models.Gems(
                    gem=row['item']
                )
                new_gem.save()

        for _, row in reader.iterrows():
            clean_file = models.ContentFile(
                customer=models.Clients.objects.get(username=row['customer']),
                item=models.Gems.objects.get(gem=row['item']),
                total=row['total'],
                quantity=row['quantity'],
                date=row['date']
            )
            clean_file.save()

    def create_clean_data_model(self):
        for cl_obj in models.Clients.objects.all():
            data = {
                'username': cl_obj.username,
                'spent_money': 0,
                'gems': ''
            }
            for cont_obj in models.ContentFile.objects.filter(customer=models.Clients.objects.get(username=cl_obj.username)):
                data['spent_money'] += cont_obj.total
                data['gems'] += '{}, '.format(cont_obj.item.gem)

            clean_data = models.Clean_data(
                username=data.get('username'),
                spent_money=data.get('spent_money'),
                gems=data.get('gems')
            )
            clean_data.save()

        return models.Clean_data.objects.order_by('-spent_money')


    def clear_data(self):
        models.ContentFile.objects.all().delete()
        models.Gems.objects.all().delete()
        models.Clients.objects.all().delete()
        models.Clean_data.objects.all().delete()

