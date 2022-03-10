import os


class BasicConfig:
    DD_RUM_APPLICATION_ID = os.environ.get('DD_RUM_APPLICATION')
    DD_RUM_CLIENT_TOKEN = os.environ.get('DD_RUM_CLIENT_TOKEN')
    DD_RUM_SERVICE = os.environ.get('DD_RUM_SERVICE')
    DD_RUM_ENABLED = os.environ.get('DD_RUM_ENABLED')
    DD_RUM_ENV = os.environ.get('DD_RUM_ENV')


class DevelopmentConfig(BasicConfig):
    DEBUG = True


class ProductionConfig(BasicConfig):
    DEBUG = False
