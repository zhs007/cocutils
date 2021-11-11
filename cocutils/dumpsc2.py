# -*- coding:utf-8 -*-
from sc import SupercellSWF
import os

def sc2png(fn, outputPath):
    swf = SupercellSWF()
    swf.load(fn)

    base_name, ext = os.path.splitext(os.path.basename(fn))
    
    for i in range(len(swf.textures)):
        t = swf.textures[i]
        fn1 = base_name + '_' + str(i) + '.png'
        t.image.save(os.path.join(outputPath, fn1), "PNG")