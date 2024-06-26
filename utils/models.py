# -*- coding: utf-8 -*-
# @Time    : 2021/2/25 上午10:43
# @Author  : Hsurich
import base64

# from Crypto.Cipher import AES
from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    """基类模型"""
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    available = models.SmallIntegerField(choices=[(1, '可用'), (0, '不可用')], default=1)
    deleted = models.SmallIntegerField(choices=[(1, '删除'), (0, '未删')], default=0)

    class Meta:
        abstract = True  # 抽象模型类, 用于继承使用


# class BasePasswordModels(models.Model):
#     """需要密码加解密的基类模型"""
#
#     class Meta:
#         abstract = True
#
#     @staticmethod
#     def encrypt(row_password: str):
#         """
#         AES 加密登录密码
#         :param row_password: 原明文密码
#         :return: AES加密后密码
#         """
#         aes = AES.new(str.encode(settings.SECRET_KEY[4:20]), AES.MODE_ECB)
#         while len(row_password) % 16 != 0:
#             row_password += '\0'
#         return str(base64.encodebytes(aes.encrypt(str.encode(row_password))), encoding='utf8').replace('\n', '')
#
#     def set_password(self, field_name, field_value):
#         """加密密码并保存实例"""
#         self.__setattr__(field_name, self.encrypt(field_value))
#
#     def get_password_display(self, field_name):
#         """
#         AES 解密登录密码
#         :return: 原明文密码
#         """
#         aes = AES.new(str.encode(settings.SECRET_KEY[4:20]), AES.MODE_ECB)
#         return str(
#             aes.decrypt(base64.decodebytes(bytes(str(self.__getattribute__(field_name)), encoding='utf8'))).rstrip(
#                 b'\0').decode("utf8"))
