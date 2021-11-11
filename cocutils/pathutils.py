# -*- coding:utf-8 -*-
from sc import SupercellSWF
import os

def findAllFile(basePath, endsWith):
    for root, ds, fs in os.walk(basePath):
        for f in fs:
            if f.endswith(endsWith):
                fullname = os.path.join(root, f)
                yield fullname

