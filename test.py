#!/user/bin/env python3
# -*- coding: utf-8 -*-
import platform
platform.platform()   #获取操作系统名称及版本号

platform.version()    #获取操作系统版本号

platform.architecture()   #获取操作系统的位数

platform.machine()    #计算机类型

platform.node()       #计算机的网络名称

platform.processor()  #计算机处理器信息

platform.uname()      #上面所有的信息汇总

print(platform.platform().split('-') [1])