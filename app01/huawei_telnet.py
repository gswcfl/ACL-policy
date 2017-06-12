#!/usr/bin/env python
import telnetlib
import time
def huawei_telnet_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info):
	tn = telnetlib.Telnet(str(ip_info),timeout=5)
	#time.sleep(1)
	tn.read_until('Username:')
	tn.write(str(user_info) + '\n')
	time.sleep(1)
	tn.read_until("Password:",timeout=2)
	tn.write(str(passwd1_info) + "\r\n")
	if passwd2_info != 'null':
		tn.read_until('>')
		tn.write('super\n')
		tn.read_until('Password:')
		tn.write(str(passwd2_info) + '\n')
	time.sleep(1)
	r1 = tn.read_very_eager()
	tn.write('display acl all' + '\n')
	time.sleep(1)
	r2 = tn.read_very_eager()
	tn.write(' display current-configuration interface ' + str(port1_info) + '\n')
	time.sleep(1)
	r3 = tn.read_very_eager()
	tn.write(' display current-configuration interface ' + str(port2_info) + '\n')
	time.sleep(1)
	r4 = tn.read_very_eager()
	tn.close()
	#print r2
	#print r3
	#print r4
	return r2,r3,r4
if __name__ == '__main__':
	port1_info = 'XGigabitEthernet0/0/0'
	port2_info = 'XGigabitEthernet0/0/1'
	changji = 'HUAWEI'
	login_info = 'TELNET'
	ip_info = '11.11.127.2'
	user_info = 'test'
	passwd1_info = "test"
	passwd2_info = 'null'
	huawei_telnet_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info)
