# Create your views here.
#-*- coding:utf-8 -*-
#
from django.shortcuts import render_to_response
from django.http import HttpResponse
import telnetlib
import time
import IPy
import os
import commands
from cisco import cisco_telnet_info
from huawei_telnet import huawei_telnet_info
from huawei_ssh import huawei_ssh_info
from h3c_ssh import h3c_ssh_info
from h3c_telnet import h3c_telnet_info
from ruijie import ruijie_telnet_info
from fiberhome import fiberhome_telnet_info
from alert import alert_info
from BJ_area import bj_area
from SH_area import sh_area
from GD_area import gd_area

BJ_list = ['10.169.63.1','10.170.63.1','11.11.119.1','11.11.127.1','11.11.15.1','11.11.15.2','11.11.31.1','11.11.39.1','11.11.47.1','11.11.47.2','11.11.55.1','11.11.63.1','11.11.87.1','11.11.95.1','10.168.63.1','10.168.63.2']
SH_list = ['11.11.127.1','11.11.127.2','11.11.63.1','11.11.63.2','11.11.111.1','11.11.119.1','11.11.127.1','11.11.127.2','11.11.15.1','11.11.39.1','11.11.55.1','11.11.7.1','11.11.79.1','11.11.87.1']
GD_list = ['11.11.63.1','11.11.63.2','11.11.127.1','11.11.127.2','11.11.191.1','11.11.191.2','11.11.63.1','11.11.63.2','11.11.111.1','11.11.119.1','11.11.127.1','11.11.39.1','11.11.55.1','11.11.63.1','11.11.7.1','11.11.87.1','11.11.95.1','11.11.63.2']

ip_list = {
	'11.11.55.1':['BJKJ-RJY','GigabitEthernet0/0','GigabitEthernet0/1','H3C','SSH','test','test','test'],
	'11.11.63.1':['BJQH-JY','Ethernet0/0/0','Ethernet0/0/1','H3C','SSH','test','test','test'],
	'11.11.87.1':['BJDX-XDCN2','GigabitEthernet1/0/0','GigabitEthernet2/0/0','HUAWEI','TELNET','test','test','test'],
	'11.11.95.1':['BJTL-XKZ','GigabitEthernet4/0/0','GigabitEthernet4/0/1','HUAWEI','SSH','test','+969_hxc','test'],
	'10.168.63.2':['BJDX-DJT163-2','XGigabitEthernet0/0/0','XGigabitEthernet0/0/1','HUAWEI','TELNET','ctsi','2016@Ctsi.com.cn','null'],
	'11.11.55.1':['GZLT-CNCKXC','Pos4/0/0','GigabitEthernet2/0/0','HUAWEI','TELNET','test','test','test'],
	'11.11.63.1':['GZLT169-DG','Gi0/2/8','Gi0/2/9','RUIJIE','TELNET','test','test','test'],
	'11.11.7.1':['GZDX163-TianHe','GigabitEthernet3/0/0','GigabitEthernet3/2/0','H3C','SSH','test','test','test'],
	'11.11.87.1':['GZDX-CN2TongHe','GigabitEthernet1/0/0','GigabitEthernet2/0/0','HUAWEI','TELNET','test','test','test'],
	'11.11.95.1':['GZTT-DS','GigabitEthernet4/0/0','GigabitEthernet2/0/1','HUAWEI','TELNET','test','test','test'],
	'11.11.63.2':['GZLT169-DG','Gi0/2/8','Gi0/2/9','RUIJIE','TELNET','test','test','test'],
	'10.168.63.1':['BJYD-GJXXG','XGigabitEthernet0/0/0','XGigabitEthernet0/0/1','HUAWEI','SSH','ctsi','2016@Ctsi.com.cn','null'],
	'10.169.63.1':['BJDX169-DGC2','Ten-GigabitEthernet2/0/4','Ten-GigabitEthernet2/0/3','H3C','TELNET','h3c','admin1234','null'],
	'10.170.63.1':['BJYD-GJXXG','GigabitEthernet8/0/0','GigabitEthernet8/0/1','HUAWEI','TELNET','test','test123','null'],
	'11.11.119.1':['BJDX163-DJT','GigabitEthernet2/0/0','GigabitEthernet2/0/1','HUAWEI','TELNET','test','~ei3^5a5','test'],
	'11.11.127.1':['BJYD-DBL','GigaEthernet5/0','GigaEthernet0/3','Fiberhome','TELNET','test123','Banner@2015','null'],
	'11.11.15.1':['BJLT169-SH','GigabitEthernet3/0/1','GigabitEthernet3/0/0','H3C','SSH','test','test','test'],
	'11.11.15.2':['BJLT169-SH','Gi0/0/1','Gi0/0/2','RUIJIE','TELNET','test','test','test'],
	'11.11.31.1':['BJLT-CNCDB','Fa0/0','Fa0/1','CISCO','TELNET','test','test','test'],
	'11.11.39.1':['BJYD-IPZWST','GigabitEthernet1/0/0','GigabitEthernet2/0/0','HUAWEI','TELNET','test','test','test'],
	'11.11.47.1':['BJLT169-DGC','GigabitEthernet8/0','GigabitEthernet6/0','H3C','SSH','test','test','test'],
	'11.11.47.2':['BJLT169-DGC','Gi0/0/1','Gi0/0/2','RUIJIE','TELNET','test','test','test'],
	'11.11.127.1':['SHDX163-XXY2','XGigabitEthernet0/0/0','XGigabitEthernet0/0/1','HUAWEI','TELNET','test','2016@Ctsi.com.cn','null'],
	'11.11.127.2':['SHDX163-XXY2','XGigabitEthernet0/0/0','XGigabitEthernet0/0/1','HUAWEI','TELNET','test','2016@Ctsi.com.cn','null'],
	'11.11.63.1':['SHDX163-WS2','XGigabitEthernet0/0/1','XGigabitEthernet0/0/0','HUAWEI','TELNET','test','2016@Ctsi.com.cn','null'],
	'11.11.63.2':['SHDX163-WS2','XGigabitEthernet0/0/0','XGigabitEthernet0/0/1','HUAWEI','TELNET','test','2016@Ctsi.com.cn','null'],
	'11.11.111.1':['SHYD-WS','GigaEthernet2/0','GigaEthernet0/0','Fiberhome','TELNET','test','test','test'],
	'11.11.119.1':['SHDX163-XXY','GigabitEthernet1/0/0','GigabitEthernet2/0/0','HUAWEI','SSH','test','test','test'],
	'11.11.127.1':['SHLT169-JQSQ','Gi0/0/2','Gi0/0/1','RUIJIE','TELNET','test','test','test'],
	'11.11.127.2':['SHLT169-JQSQ','Gi0/0/1','Gi0/0/2','RUIJIE','TELNET','test','test','test'],
	'11.11.15.1':['SHLT169-TL','GigabitEthernet8/0','GigabitEthernet6/0','H3C','TELNET','test','test','test'],
	'11.11.39.1':['SHYD-YCL','GigabitEthernet1/0/0','GigabitEthernet2/0/1','HUAWEI','TELNET','test','test','test'],
	'11.11.55.1':['SHLT-CNCTL','GigabitEthernet1/0/0','GigabitEthernet2/0/0','HUAWEI','TELNET','test','%602kn<f','test'],
	'11.11.7.1':['SHDX163-WS','GigabitEthernet1/0/0','GigabitEthernet2/0/0','HUAWEI','TELNET','test','0t2q_+1p','test'],
	'11.11.79.1':['SHLT169-JQ','GigabitEthernet5/1','GigabitEthernet8/0','H3C','SSH','test','test','test'],
	'11.11.87.1':['SHDX-CN2MS','GigabitEthernet1/0/0','GigabitEthernet4/0/1','HUAWEI','TELNET','test','z&~57dm9','test'],
	'11.11.63.1':['GZLT169-KXC2','Ten-GigabitEthernet2/0/3','Ten-GigabitEthernet2/0/4','H3C','TELNET','admin','H3c@123','null'],
	'11.11.63.2':['GZLT169-KXC2','Ten-GigabitEthernet2/0/3','Ten-GigabitEthernet2/0/4','H3C','TELNET','admin','H3c@123','null'],
	'11.11.127.1':['GZYD-NJ302','GigabitEthernet8/1/0','GigabitEthernet8/1/1','HUAWEI','TELNET','test','test123','null'],
	'11.11.127.2':['GZYD-NJ302','GigabitEthernet8/1/0','GigabitEthernet8/1/1','HUAWEI','TELNET','test','test123','null'],
	'11.11.191.1':['GZYD-NJ304','GigabitEthernet8/1/0','GigabitEthernet8/1/1','HUAWEI','TELNET','test','test123','null'],
	'11.11.191.2':['GZYD-NJ304','GigabitEthernet8/1/0','GigabitEthernet8/1/1','HUAWEI','TELNET','test','test123','null'],
	'11.11.63.1':['GZYD-SS','GigabitEthernet1/1/1','GigabitEthernet8/1/1','HUAWEI','TELNET','test','test123','null'],
	'11.11.63.2':['GZYD-SS','GigabitEthernet8/1/0','GigabitEthernet8/1/1','HUAWEI','TELNET','test','test123','null'],
	'11.11.111.1':['GZYD-QHD','GigabitEthernet1/0/0','GigabitEthernet2/0/1','HUAWEI','TELNET','test','d0h9q&~1','test'],
	'11.11.119.1':['GZDX163-TH','GigabitEthernet1/0/0','GigabitEthernet2/0/0','HUAWEI','TELNET','test','u5d73h<*','test'],
	'11.11.127.1':['GZYD-NFJD304','GigaEthernet2/0','GigaEthernet0/0','Fiberhome','TELNET','test','test','test'],
	'11.11.39.1':['GZYD-NFJD302','GigaEthernet2/0','GigaEthernet0/0','Fiberhome','TELNET','test','test','test'],
	}
#
def index(request):
	return render_to_response('index.html')
def query(request):
	ip = request.GET['address']
	address_info = ip_list[ip][0]
	port1_info = ip_list[ip][1]
	port2_info = ip_list[ip][2]
	changji = ip_list[ip][3]
	login_info = ip_list[ip][4]
	ip_info = ip
	user_info = ip_list[ip][5]
	passwd1_info = ip_list[ip][6]
	passwd2_info = ip_list[ip][7]
	if  (changji == 'HUAWEI') and (login_info == 'TELNET'):
		(r2,r3,r4) = huawei_telnet_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info)
	elif (changji == 'H3C') and (login_info == 'SSH'):
		(r2,r3,r4) = h3c_ssh_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info)
	elif changji == 'CISCO':
		(r2,r3,r4) = cisco_telnet_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info)
	elif (changji == 'HUAWEI') and (login_info == 'SSH'):
		(r2,r3,r4) = huawei_ssh_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info)
	elif (changji == 'H3C') and (login_info == 'TELNET'):
		(r2,r3,r4) = h3c_telnet_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info)
	elif changji == 'RUIJIE':
		(r2,r3,r4) = ruijie_telnet_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info)
	elif changji == 'Fiberhome':
		(r2,r3,r4) = fiberhome_telnet_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info)
	return render_to_response('index.html',{'r2':r2,'r3':r3,'r4':r4,'address_info':address_info,'ip_info':ip_info})

def area_query(request):
	area = request.GET['area']
	os.system('> acl_info.txt')
	text = []
	if area == 'Beijing':
		bj_area(BJ_list,ip_list)
	elif area == 'Shanghai':
		sh_area(SH_list,ip_list)
	elif area == 'Guangdong':
		gd_area(GD_list,ip_list)
	f = file('acl_info.txt','r')
	lines = f.readlines()
	for line in lines:
		text.append(line.strip('\n'))
		#text.append(line)
	return render_to_response('index.html',{'text':text,'area':area})
