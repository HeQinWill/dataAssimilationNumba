# -*- coding:utf-8 -*-
import os
import glob
import numba
from numba import jit
import h5py
import numpy as np
from math import radians, cos, sin, asin, sqrt 
from netCDF4 import Dataset

@jit
def haversine(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）  
    """ 
    Calculate the great circle distance between two points  
    on the earth (specified in decimal degrees) 
    """  
    # 将十进制度数转化为弧度  
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])  
  
    # haversine公式  
    dlon = lon2 - lon1   
    dlat = lat2 - lat1   
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
    c = 2 * asin(sqrt(a))   
    r = 6371 # 地球平均半径，单位为公里  
    return c * r * 1000 # 最终单位为米
    
@jit
def distanceFalse(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）  
    dlon = lon2 - lon1   
    dlat = lat2 - lat1   
    a = dlat**2 + dlon**2  
    return a

fileWRF = '/home/heqin/Documents/dataAssimilationNumbaBigFile/wrfout_d02_2015-12-26_00_00_00'
with Dataset(fileWRF,'r') as readWRF:  
    lat_wrf = readWRF.variables['XLAT'][0]
    lon_wrf = readWRF.variables['XLONG'][0]

with open('SATE.txt','r') as readSATE:
    #for line in readSATE:
         #print (line)
    s=readSATE.read()
    #print(s)
    #print(s.split()) 
    #print(len(s.split())/5) #len是分割后总的个数，每行5个，除以5得到行数
    for line in range(int(len(s.split())/5)):
        #print(s.split()[2+5*line],s.split()[3+5*line],s.split()[4+5*line])
        lat_sate = float(s.split()[2+5*line])
        lon_sate = float(s.split()[3+5*line])
        value_sate = s.split()[4+5*line]
        dis = np.zeros((84,96))
        for i in range(96):
            for j in range(84):
                # 对于第x个卫星像元，所有的WRF网格与它的距离
                #dis[j][i] = haversine(110.68455, 30.036022, lon_wrf[j][i], lat_wrf[j][i])
                #print(i,j)
                dis[j][i] = distanceFalse(lon_sate, lat_sate, lon_wrf[j][i], lat_wrf[j][i])
        print(dis.min(),np.where(dis==np.min(dis))[0][0],np.where(dis==np.min(dis))[1][0],value_sate)
