#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Author: limanman
# E-mail: xmdevops@vip.qq.com
# Wrdate: 2015/12/22 23:13:33
# Target:
#

import json
import pprint
import common_dat
import aliyun_ecs


if __name__ == '__main__':
    for region in common_dat.RegionId:
        ecs = aliyun_ecs.Aliyun_ECS(common_dat.AccessKey, common_dat.AccessSecret, region)
        print region, ':'
        pprint.pprint(ecs.get_DescribeInstancesRes())
        del ecs
