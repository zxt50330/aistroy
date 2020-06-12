from services.models import models, ModelBase


class Resource(ModelBase):
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=200)

    def play(self):
        '''
        使用资源
        :return:
        '''
        ...
