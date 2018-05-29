import configparser
from datetime import datetime
import os
from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings
from django.core.management.color import color_style
from edc_device import DevicePermissions, DeviceAddPermission, DeviceChangePermission
from edc_device.apps import AppConfig as BaseEdcDeviceAppConfig
from edc_device.constants import CENTRAL_SERVER, CLIENT, NODE_SERVER


config = configparser.RawConfigParser()
config.read(os.path.join(settings.ETC_DIR,
                         settings.APP_NAME,
                         settings.CONFIG_FILE))


class AppConfig(DjangoAppConfig):
    name = 'training_program'
    base_template_name = 'training_program/base.html'
    dashboard_url_name = 'home_url'
    listboard_url_name = 'home_url'


class EdcDeviceAppConfig(BaseEdcDeviceAppConfig):
    use_settings = True
    device_id = settings.DEVICE_ID
    device_role = settings.DEVICE_ROLE
    device_permissions = DevicePermissions(
        DeviceAddPermission(
            model='plot.plot',
            device_roles=[CENTRAL_SERVER, CLIENT]),
        DeviceChangePermission(
            model='plot.plot',
            device_roles=[NODE_SERVER, CENTRAL_SERVER, CLIENT]))
