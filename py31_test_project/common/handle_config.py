import os
from configparser import ConfigParser
from py31_test_project.common.handle_path import CONF_DIR


# 继承父类
class Config(ConfigParser):
    def __init__(self, filename, encoding='utf-8'):
        # 不能重写父类的init方法，所以超类继承
        super().__init__()
        self.read(filename, encoding=encoding)


conf = Config(os.path.join(CONF_DIR, 'config.ini'))
