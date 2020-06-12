from services.models import models, ModelBase
from story_resource.models import Resource


class TaskTimes(ModelBase):
    frequency = models.CharField(max_length=10)  # 固化参数 周1-7 每小时 等等

    def set_cron(self):
        """
        设置计划任务
        :return:
        """
        ...

    def add_cron(self):
        """
        新增任务
        :return:
        """
        ...

    def del_cron(self):
        ...


class TaskList(ModelBase):
    name = models.CharField(max_length=40)
    start_time = models.TimeField(verbose_name='开始时间')
    end_time = models.TimeField(null=True, blank=True)
    resource = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True)
    times = models.ManyToManyField(TaskTimes)

    def do(self):
        """
        执行任务
        :return:
        """
        self.resource.play()
