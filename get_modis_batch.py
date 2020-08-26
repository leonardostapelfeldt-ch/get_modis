#!/usr/bin/env python
# small program that calls get_modis.py and allows downloading data for several
# year and tiles

import numpy as np
import os
import subprocess
import sys

yr_start = 2001
yr_end = 2019

d_start = 120 # first day
d_end = 280 # last day

user = 'horst.machguth@unifr.ch'
pw = 'Chilchigir_2'

outdir = '/home/horstm/erc/sat_modis_raw'

tiles = ['h15v02','h16v02']

years = np.arange(yr_start, yr_end+1, 1)

for t in tiles:
    for y in years:
        # Crop using gdalwarp
        cmd = '/home/horstm/src/get_modis/get_modis.py -u ' + user +\
               ' -P ' + pw + ' -s MOST -l NSIDC -t ' + t +\
               ' -b ' + str(d_start) + ' -e ' + str(d_end) + ' -y ' + str(int(y)) +\
               ' -o ' + outdir + ' -v -p MOD10A1.006'

        print('** CMD ** ' + cmd)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
		    stderr=subprocess.PIPE,	shell=True)
        (stdout,stderr) = p.communicate()
        p.wait()
        if p.returncode != 0:
	        print(': get_modis failed: ' + str(stderr))
