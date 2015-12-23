#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Author: limanman
# E-mail: xmdevops@vip.qq.com
# Wrdate: 2015/12/22 23:13:33
# Target:
#

import sys
import json
from   aliyunsdkcore import client
from   aliyunsdkecs.request.v20140526 import DescribeInstancesRequest

class Aliyun_ECS(object):
    def __init__(self, AccessKey, AccessSecret, RegionId):
        self.RegionId    = RegionId
        self.AccessKey   = AccessKey
        self.AccessSecret= AccessSecret

    def get_DescribeInstancesRes(self, res_format="json"):
        region_cli = client.AcsClient(
                self.AccessKey,
                self.AccessSecret,
                self.RegionId)
        region_req = DescribeInstancesRequest.DescribeInstancesRequest()
        region_req.set_accept_format(res_format)
        region_res = json.loads(region_cli.do_action(region_req))
        return region_res

if __name__ == '__main__':
    sys.exit('can only be imported, could not run directly!')
