# -*- coding:utf-8 -*-
import sys 
import pandas as pd
sys.path.append("..")
import cocutils

# cocutils.dumpsc('./building_bases_tex.sc', './', False)
# cocutils.dumpsc('./buildings.csv', './', False)
cocutils.sc2png('./building_bases_tex.sc', './')