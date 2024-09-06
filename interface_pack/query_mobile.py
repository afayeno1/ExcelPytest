#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

class Keyword:

    def interface(self,method,url,**kwargs):
        session=requests.Session()
        res=session.request(method=method,url=url,**kwargs)
        res=session.request
        return res

if __name__=="__main__":
    key=Keyword()
    url = 'http://xhzw.api.bdymkt.com/carrier'
    params = {'mobile':'13912341234'}
    headers = {

        'Content-Type': 'application/json;charset=UTF-8',
        'X-Bce-Signature': 'AppCode/1f401b426fb94eddb1f4e77e60e12411'
    }
    res=key.interface(method="post",url=url,data=params,headers=headers)
    # r = requests.post(url=url,data=params,headers=headers)
    print(res)
    print(res.json())
    print(res.status_code)
