from django.db import models

# Create your models here.


class UserType(models.Model):
    """用户类型"""

    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    """用户信息"""
    username = models.CharField('用户名', max_length=30)
    pwd = models.CharField('用户密码', max_length=32)
    email = models.EmailField('邮箱地址', max_length=32)

    user_type = models.ForeignKey(UserType)

    def __str__(self):
        return self.username


class HostInfo(models.Model):
    """主机信息"""
    hostname = models.CharField('主机名称', max_length=30)
    ip = models.GenericIPAddressField('主机IP', max_length=64)
    port = models.IntegerField('主机端口')
    department = models.CharField('部门', max_length=32)
    status = models.BooleanField('状态', default=True)
    area = models.CharField('地区', max_length=32)
    onlin_time = models.DateTimeField('上线时间', )
    update_time = models.DateTimeField('下线时间', )
    description = models.TextField('详细信息', )

    user = models.ForeignKey(UserInfo)

    def __str__(self):
        return self.hostname
