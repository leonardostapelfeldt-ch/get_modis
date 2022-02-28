#!/usr/bin/env python
# small program that calls get_modis.py and allows downloading data for several
# year and tiles

import numpy as np
import subprocess
import platform

osys = platform.system()
print('operating system is %s' %osys)

yr_start = 2000
yr_end = 2021

# d_start = 120  # first day
# d_end = 280  # last day
d_start = 120  # first day
d_end = 280  # last day

user = 'leonardostapelfeldt@gmail.com'
pw = 'Unifrproject1'

if osys != 'Windows':
    outdir = '/Volumes/Windows/Unifr/modis_raw'
else:
    outdir = r'N:/MODIS/sat_modis_raw/MOD10A1'

# tiles = ['h15v02','h16v01', 'h16v02']
tiles = ['h17v00', 'h17v01']

years = np.arange(yr_start, yr_end+1, 1)

d_end += 1  # add one as the last element is not downloaded

for t in tiles:
    for y in years:
        # Crop using gdalwarp
        if osys != 'Windows':
            cmd = '/Users/leonardostapelfeldt/PycharmProjects/get_modis/get_modis.py -u ' + user +\
                   ' -P ' + pw + ' -s MOST -l NSIDC -t ' + t +\
                   ' -b ' + str(d_start) + ' -e ' + str(d_end) + ' -y ' + str(int(y)) +\
                   ' -o ' + outdir + ' -v -p MOD10A1.006'
        else:
            # cmd = r'python C:\horst\src\py\get_modis\get_modis.py -u ' + user + \
            #       ' -P ' + pw + ' -s MOST -l NSIDC -t ' + t + \
            #       ' -b ' + str(d_start) + ' -e ' + str(d_end) + ' -y ' + str(int(y)) + \
            #       ' -o ' + outdir + ' -v -p MOD10A1.006'
            cmd = r'python C:\Users\machg\PycharmProjects\get_modis\get_modis.py -u ' + user + \
                  ' -P ' + pw + ' -s MOST -l NSIDC -t ' + t + \
                  ' -b ' + str(d_start) + ' -e ' + str(d_end) + ' -y ' + str(int(y)) + \
                  ' -o ' + outdir + ' -v -p MOD10A1.006'

        print('** CMD ** ' + cmd)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
		    stderr=subprocess.PIPE,	shell=True)
        (stdout,stderr) = p.communicate()
        p.wait()
        if p.returncode != 0:
	        print(': get_modis failed: ' + str(stderr))
