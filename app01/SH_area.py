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
SH_list = ['11.11.127.1','11.11.127.2','11.11.63.1','11.11.63.2','10.54.111.1','10.54.119.1','10.54.127.1','10.54.127.2','10.54.15.1','10.54.39.1','10.54.55.1','10.54.7.1','10.54.79.1','10.54.87.1']
#10.54.7.6
ip_list = {
	'11.11.127.1':['SHDX163-XXY2','XGigabitEthernet0/0/0','XGigabitEthernet0/0/1','HUAWEI','TELNET','test','2016@test.com.cn','null'],
	'11.11.127.2':['SHDX163-XXY2','XGigabitEthernet0/0/0','XGigabitEthernet0/0/1','HUAWEI','TELNET','test','2016@test.com.cn','null'],
	'11.11.63.1':['SHDX163-WS2','XGigabitEthernet0/0/1','XGigabitEthernet0/0/0','HUAWEI','TELNET','test','2016@test.com.cn','null'],
	'11.11.63.2':['SHDX163-WS2','XGigabitEthernet0/0/0','XGigabitEthernet0/0/1','HUAWEI','TELNET','test','2016@test.com.cn','null'],
	'10.54.111.1':['SHYD-WS','GigaEthernet2/0','GigaEthernet0/0','Fiberhome','TELNET','test','test','test'],
	'10.54.119.1':['SHDX163-XXY','GigabitEthernet1/0/0','GigabitEthernet2/0/0','HUAWEI','SSH','test','test','test'],
	'10.54.127.1':['SHLT169-JQSQ','Gi0/0/2','Gi0/0/1','RUIJIE','TELNET','test','test','test'],
	'10.54.127.2':['SHLT169-JQSQ','Gi0/0/1','Gi0/0/2','RUIJIE','TELNET','test','test','test'],
	'10.54.15.1':['SHLT169-TL','GigabitEthernet8/0','GigabitEthernet6/0','H3C','TELNET','test','test','test'],
	'10.54.39.1':['SHYD-YCL','GigabitEthernet1/0/0','GigabitEthernet2/0/1','HUAWEI','TELNET','test','test','test'],
	'10.54.55.1':['SHLT-CNCTL','GigabitEthernet1/0/0','GigabitEthernet2/0/0','HUAWEI','TELNET','test','%602kn<f','test'],
	'10.54.7.1':['SHDX163-WS','GigabitEthernet1/0/0','GigabitEthernet2/0/0','HUAWEI','TELNET','test','0t2q_+1p','test'],
	'10.54.79.1':['SHLT169-JQ','GigabitEthernet5/1','GigabitEthernet8/0','H3C','SSH','test','test','test'],
	'10.54.87.1':['SHDX-CN2MS','GigabitEthernet1/0/0','GigabitEthernet4/0/1','HUAWEI','TELNET','test','z&~57dm9','test'],
	}

def sh_area(SH_list,ip_list):
#def sh_area():
	os.system('> acl_info.txt')
	alert = ''
	for i in range(len(SH_list)):
		address_info = ip_list[SH_list[i]][0]
		port1_info = ip_list[SH_list[i]][1]
		port2_info = ip_list[SH_list[i]][2]
		changji = ip_list[SH_list[i]][3]
		login_info = ip_list[SH_list[i]][4]
		ip_info = SH_list[i]
		user_info = ip_list[SH_list[i]][5]
		passwd1_info = ip_list[SH_list[i]][6]
		passwd2_info = ip_list[SH_list[i]][7]
		#print address_info,port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info
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
		#print ip_info,' 完成'
		f.close()
	#print '作业完成'
#if __name__ == '__main__':
#	sh_area()
