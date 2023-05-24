# -*- coding: utf-8 -*-
from hackcqooc.core import Core

import threading
import logging
from time import sleep
import random

class skipper(threading.Thread):
    """用于执行跳过课程任务的线程类"""

    def __init__(self, core: Core, sectionList: list,ifslow:False) -> None:
        """参数说明：
        *core* 功能内核对象，来自src.core
        *sectionList* 包含课程ID的字符串列表
        """
        threading.Thread.__init__(self)
        self.core = core
        self.sectionList = sectionList
        self.success = 0
        self.fail = 0
        self.current = 1
        self.state = False
        self.ifslow = ifslow

    def run(self) -> None:
        logging.info("skip thread started")
        self.skip(self.sectionList)

    def skip(self, sectionList: list) -> None:
        logging.info("skip task started")
        for i in sectionList:
            result = self.core.skip_section(i)
            if result["code"] == 200:
                self.success += 1
            else:
                self.fail += 1
            # 对于任务列表长度为1的情况就没有必要sleep这么久了，只有长度超过1的才要分别sleep 31秒
            if len(sectionList) != 1:
                if(self.ifslow==False):
                    sleep(31)
                else:
                    sleep_time =  random.randint(100,180)
                    sleep(sleep_time)
                
            self.current += 1
        # 跳出循环说明任务执行完成，修改状态标志位为True
        self.state = True

    def getState(self) -> bool:
        """返回True说明任务执行完成，False为未完成"""
        return self.state
