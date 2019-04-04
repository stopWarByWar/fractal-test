# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client, models
import json



if __name__ == '__main__':
    try:
        cred = credential.Credential("AKIDqfMvKmNHJLssq1Ga4zSUP8oPWbWFP7D8", "IUXTGCz6Qn1738KwOkyu63hItLhdhcq1")
        client = cvm_client.CvmClient(cred, "ap-guangzhou")
        req = models.DescribeZonesRequest()
        response = client.DescribeInstances(req)
        resp = json.loads(response.to_json_string(),encoding='utf-8')

        print type(resp)
        print(resp)

    except TencentCloudSDKException as err:
        print(err)

    file = "ip.txt"

    with open(file, 'w') as f:

        instances = resp["InstanceSet"]

        for instance in instances:
            ip = instance["PrivateIpAddresses"]
            f.writelines(ip[0]+'\n')
            print ip


    with open(file,"r") as f:
        contain = f.read()
        arr = contain.split('\n')
        print contain


