#!/usr/bin/env python
# -*- coding: utf-8 -*-
from string import Template

ss={"token":123456}
url="http://www.baidu.com/?${token}"

print(Template(url).substitute(ss))

