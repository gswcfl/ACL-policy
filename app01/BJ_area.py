#!/usr/bin/env python
#-*- coding:utf-8-*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath('__file__')))
import telnetlib
import time
import IPy
import commands
from cisco import cisco_telnet_info
from huawei_ssh import huawei_ssh_info
from huawei_telnet import huawei_telnet_info
from h3c_ssh import h3c_ssh_info
from h3c_telnet import h3c_telnet_info
from ruijie import ruijie_telnet_info
from fiberhome import fiberhome_telnet_info
from alert import alert_info
BJ_list = ['10.169.63.1','10.170.63.1','11.11.119.1','11.11.127.1','11.11.15.1','11.11.15.2','11.11.31.1','11.11.39.1','11.11.47.1','11.11.47.2','11.11.55.1','11.11.63.1','11.11.87.1','11.11.95.1','10.168.63.1','10.168.63.2']
#10.170.63.2
ip_list = {
	'11.11.55.1':['BJKJ-RJY','GigabitEthernet0/0','GigabitEthernet0/1','H3C','SSH','test','test','test'],
	'11.11.63.1':['BJQH-JY','Ethernet0/0/0','Ethernet0/0/1','H3C','SSH','test','test','test'],
	'11.11.87.1':['BJDX-XDCN2','GigabitEthernet1/0/0','GigabitEthernet2/0/0','HUAWEI','TELNET','test','test','test'],
	'11.11.95.1':['BJTL-XKZ','GigabitEthernet4/0/0','GigabitEthernet4/0/1','HUAWEI','SSH','test','+969_hxc','test'],
	'10.168.63.1':['BJDX-DJT163-2','XGigabitEthernet0/0/0','XGigabitEthernet0/0/1','HUAWEI','TELNET','test','2016@Ctsi.com.cn','null'],
	'10.168.63.2':['BJDX-DJT163-2','XGigabitEthernet0/0/0','XGigabitEthernet0/0/1','HUAWEI','TELNET','test','2016@Ctsi.com.cn','null'],
	'10.169.63.1':['BJDX169-DGC2','Ten-GigabitEthernet2/0/4','Ten-GigabitEthernet2/0/3','H3C','TELNET','h3c','admin1234','null'],
	'10.170.63.1':['BJYD-GJXXG','GigabitEthernet8/0/0','GigabitEthernet8/0/1','HUAWEI','TELNET','hsoft','hsoft123','null'],
	'11.11.119.1':['BJDX163-DJT','GigabitEthernet2/0/0','GigabitEthernet2/0/1','HUAWEI','TELNET','test','~ei3^5a5','test'],
	'11.11.127.1':['BJYD-DBL','GigaEthernet5/0','GigaEthernet0/3','Fiberhome','TELNET','hsoft123','Banner@2015','null'],
	'11.11.15.1':['BJLT169-SH','GigabitEthernet3/0/1','GigabitEthernet3/0/0','H3C','TELNET','test','test','test'],
	'11.11.15.2':['BJLT169-SH','Gi0/0/1','Gi0/0/2','RUIJIE','TELNET','test','test','test'],
	'11.11.31.1':['BJLT-CNCDB','Fa0/0','Fa0/1','CISCO','TELNET','test','test','test'],
	'11.11.39.1':['BJYD-IPZWST','GigabitEthernet1/0/0','GigabitEthernet2/0/0','HUAWEI','TELNET','test','test','test'],
	'11.11.47.1':['BJLT169-DGC','GigabitEthernet8/0','GigabitEthernet6/0','H3C','SSH','test','test','test'],
	'11.11.47.2':['BJLT169-DGC','Gi0/0/1','Gi0/0/2','RUIJIE','TELNET','test','test','test'],
	}

#def bj_area():
def bj_area(BJ_list,ip_list):
	os.system('> acl_info.txt')
	alert = ''
	for i in range(len(BJ_list)):
		address_info = ip_list[BJ_list[i]][0]
		port1_info = ip_list[BJ_list[i]][1]
		port2_info = ip_list[BJ_list[i]][2]
		changji = ip_list[BJ_list[i]][3]
		login_info = ip_list[BJ_list[i]][4]
		ip_info = BJ_list[i]
		user_info = ip_list[BJ_list[i]][5]
		passwd1_info = ip_list[BJ_list[i]][6]
		passwd2_info = ip_list[BJ_list[i]][7]
		#print address_info,port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info
		alert = alert_info(ip_info,ip_list)
		if alert == '':
			pass
		else:
			f = file('acl_info.txt','a+')
			f.write('ACL profile:' + address_info + ' ' + ip_info)
			f.write(alert)
			f.flush()
			f.close()
			continue
		if (changji == 'H3C') and (login_info =='SSH'):
			(r2,r3,r4) = h3c_ssh_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info)
		elif (changji == 'H3C') and (login_info =='TELNET'):
			(r2,r3,r4) = h3c_telnet_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info)
		elif changji == 'CISCO':
			(r2,r3,r4) = cisco_telnet_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info)
		elif (changji == 'HUAWEI') and (login_info == 'SSH'):
			(r2,r3,r4) = huawei_ssh_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info)
		elif (changji == 'HUAWEI') and (login_info =='TELNET'):
			(r2,r3,r4) = huawei_telnet_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info)
		elif changji == 'RUIJIE':
			(r2,r3,r4) = ruijie_telnet_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info)
		elif changji == 'Fiberhome':
			(r2,r3,r4) = fiberhome_telnet_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info)
		f = file('acl_info.txt','a+')
		f.write('ACL profile:' + address_info + ' ' + ip_info)
		f.write(r2)
		f.write(r3)
		f.write(r4)
		#f.write('\n')
		f.flush()
		#print ip_info,' 完成'
		f.close()
	#print '作业完成'
#if __name__ == '__main__':
#	bj_area()
