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
GD_list = ['10.185.63.1','10.185.63.2','11.11.127.1','10.186.127.2','10.186.191.1','10.186.191.2','10.186.63.1','10.186.63.2','11.11.111.1','10.53.119.1','10.53.127.1','10.53.39.1','10.53.55.1','10.53.63.1','10.53.7.1','10.53.87.1','10.53.95.1','10.53.63.2']
ip_list = {
	'10.185.63.1':['GZLT169-KXC2','Ten-GigabitEthernet2/0/3','Ten-GigabitEthernet2/0/4','H3C','TELNET','admin','H3c@123','null'],
	'10.185.63.2':['GZLT169-KXC2','Ten-GigabitEthernet2/0/3','Ten-GigabitEthernet2/0/4','H3C','TELNET','admin','H3c@123','null'],
	'11.11.127.1':['GZYD-NJ302','GigabitEthernet8/1/0','GigabitEthernet8/1/1','HUAWEI','TELNET','test','test123','null'],
	'11.11.127.2':['GZYD-NJ302','GigabitEthernet8/1/0','GigabitEthernet8/1/1','HUAWEI','TELNET','test','test123','null'],
	'11.11.191.1':['GZYD-NJ304','GigabitEthernet8/1/0','GigabitEthernet8/1/1','HUAWEI','TELNET','test','test123','null'],
	'11.11.191.2':['GZYD-NJ304','GigabitEthernet8/1/0','GigabitEthernet8/1/1','HUAWEI','TELNET','test','test123','null'],
	'11.11.63.1':['GZYD-SS','GigabitEthernet1/1/1','GigabitEthernet8/1/1','HUAWEI','TELNET','test','test123','null'],
	'11.11.63.2':['GZYD-SS','GigabitEthernet8/1/0','GigabitEthernet8/1/1','HUAWEI','TELNET','test','test123','null'],
	'11.11.63.2':['GZLT169-DG','Gi0/2/8','Gi0/2/9','RUIJIE','TELNET','test','test','test'],
	'11.11.111.1':['GZYD-QHD','GigabitEthernet1/0/0','GigabitEthernet2/0/1','HUAWEI','TELNET','test','d0h9q&~1','test'],
	'11.11.119.1':['GZDX163-TH','GigabitEthernet1/0/0','GigabitEthernet2/0/0','HUAWEI','TELNET','test','u5d73h<*','test'],
	'11.11.127.1':['GZYD-NFJD304','GigaEthernet2/0','GigaEthernet0/0','Fiberhome','TELNET','test','test','test'],
	'11.11.39.1':['GZYD-NFJD302','GigaEthernet2/0','GigaEthernet0/0','Fiberhome','TELNET','test','test','test'],
	'11.11.55.1':['GZLT-CNCKXC','Pos4/0/0','GigabitEthernet2/0/0','HUAWEI','TELNET','test','test','test'],
	'11.11.63.1':['GZLT169-DG','Gi0/2/8','Gi0/2/9','RUIJIE','TELNET','test','test','test'],
	'11.11.7.1':['GZDX163-TianHe','GigabitEthernet3/0/0','GigabitEthernet3/2/0','H3C','SSH','test','test','test'],
	'11.11.87.1':['GZDX-CN2TongHe','GigabitEthernet1/0/0','GigabitEthernet2/0/0','HUAWEI','TELNET','test','test','test'],
	'11.11.95.1':['GZTT-DS','GigabitEthernet4/0/0','GigabitEthernet2/0/1','HUAWEI','TELNET','test','test','test']
	}

def gd_area(GD_list,ip_list):
#def gd_area():
	os.system('> acl_info.txt')
	alert = ''
	for i in range(len(GD_list)):
		address_info = ip_list[GD_list[i]][0]
		port1_info = ip_list[GD_list[i]][1]
		port2_info = ip_list[GD_list[i]][2]
		changji = ip_list[GD_list[i]][3]
		login_info = ip_list[GD_list[i]][4]
		ip_info = GD_list[i]
		user_info = ip_list[GD_list[i]][5]
		passwd1_info = ip_list[GD_list[i]][6]
		passwd2_info = ip_list[GD_list[i]][7]
#		print address_info,port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info
		alert = alert_info(ip_info,ip_list)
		if alert == '':
			pass
		else:
			f = file('acl_info.txt','a+')
			f.write('ACL profile:' + address_info + ' ' + ip_info + '\n')
			f.write(alert + '\n')
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
		f.write('ACL profile:' + address_info + ' ' + ip_info + '\n')
		f.write(r2 + '\n')
		f.write(r3 + '\n')
		f.write(r4 + '\n')
		f.write('\n')
		f.flush()
#		print ip_info,' 完成'
		f.close()
#	print '作业完成'
#if __name__ == '__main__':
#	gd_area()
