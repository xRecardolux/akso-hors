from django.contrib import admin

# Register your models here.
import xadmin
from xadmin import views


class GlobalSetting (object):
    # 设置后台管理标题
    site_title = 'Akso医院预约就诊管理后台'

    # 设置后台管理底部信息
    site_footer = '2019@中南民族大学计算机科学学院 鲁王兰夫'


xadmin.site.register(views.CommAdminView, GlobalSetting)


class BaseSetting(object):
    # 启用主题管理器   
    enable_themes = True

    # 使用主题   
    use_bootswatch = True


# 注册主题设置
xadmin.site.register(views.BaseAdminView, BaseSetting)

