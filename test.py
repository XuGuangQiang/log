#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-02
# @Author  : guangqiang_xu (981886190@qq.com)
# @Version : $Id$
from log import spider_log

log_name = 'tieba'
log_folder_name = './{}_logs'.format(log_name)
logger = spider_log(log_name=log_name, log_folder_name=log_folder_name)

logger.info('info message')