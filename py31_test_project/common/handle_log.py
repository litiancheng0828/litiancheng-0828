import logging
import os
from logging.handlers import TimedRotatingFileHandler
from py31_test_project.common.handle_path import LOG_DIR
from py31_test_project.common.handle_config import conf


class HandleLog:
    @staticmethod
    def create_logger():
        '''创建日志收集器'''
        # 1、创建日志收集器
        log = logging.getLogger('TC')
        log.setLevel(conf.get('logging', 'level'))  # 设置收集日志的等级

        # 2、创建一个输出到文件的输出渠道
        fh = TimedRotatingFileHandler(filename=os.path.join(LOG_DIR, conf.get('logging', 'log_name')),
                                      when='d',
                                      interval=1,
                                      backupCount=7,
                                      encoding='utf-8')
        fh.setLevel(conf.get('logging', 'fh_level'))  # 设置输出等级
        log.addHandler(fh)  # 添加到收集器中

        # 3、创建一个输出到控制台的输出渠道
        sh = logging.StreamHandler()
        sh.setLevel(conf.get('logging', 'sh_level'))  # 设置输出等级
        log.addHandler(sh)  # 添加到收集器中

        # 4、设置日志输出格式
        formatter = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        mate = logging.Formatter(formatter)
        fh.setFormatter(mate)  # 添加格式到文件的输出渠道
        sh.setFormatter(mate)  # 添加格式到控制台的输出渠道

        return log


log = HandleLog.create_logger()
