# -*- coding: utf-8 -*-
from logging import getLogger, config, StreamHandler, DEBUG
import os

import sys
sys.path.append('./')
from logutil import LogUtil
from importenv import ImportEnvKeyEnum
import importenv as setting
from dataclass import Data

PYTHON_APP_HOME = os.getenv('PYTHON_APP_HOME')
logger = getLogger(__name__)
log_conf = LogUtil.get_log_conf(PYTHON_APP_HOME + '/config/log_config.json')
config.dictConfig(log_conf)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

if __name__ == '__main__':
  logger.info('Start')
  logger.info('----')
  hoge = []
  logger.info(type(hoge))

  logger.info('----')

  hoge.append('hoge')
  logger.info(type(hoge))
  logger.info(type(hoge[0]))

  logger.info('----')

  hoge.append(1)
  logger.info(type(hoge))
  logger.info(type(hoge[1]))

  logger.info('----')
  
  data = Data(id = 1, hoge = 'hoge')
  logger.info(type(data))

  logger.info('----')
  
  logger.info('Finish')
