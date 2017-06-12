#!/usr/bin/env python
import telnetlib
import time
def h3c_telnet_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info):
	tn = telnetlib.Telnet(ip_info,timeout=5)
	tn.write(user_info + '\n')
	tn.write(passwd1_info + '\n')
	time.sleep(1)
	tn.read_until('Password:')
	tn.write(passwd1_info + '\n')
	if passwd2_info != 'null':
		tn.read_until('>')
		tn.write('super\n')
		tn.read_until('Password:')
		tn.write(passwd2_info + '\n')
	time.sleep(1)
	r1 = tn.read_very_eager()
	tn.write('display acl all\n')
	time.sleep(1)
	r2 = tn.read_very_eager()
	tn.write(' display current-configuration interface ' + port1_info + '\n')
	time.sleep(1)
	r3 = tn.read_very_eager()
	tn.write(' display current-configuration interface ' + port2_info + '\n')
	time.sleep(1)
	r4 = tn.read_very_eager()
	tn.close()
	#print r2
	#print r3
	#print r4
	return r2,r3,r4
if __name__ == '__main__':
	port1_info = 'GigabitEthernet3/0/1'
	port2_info = 'GigabitEthernet3/0/0'
	changji = 'H3C'
	login_info = 'TELNET'
	ip_info = '11.11.15.1'
	user_info = 'test'
	passwd1_info = 'test'
	passwd2_info = 'test'
	h3c_telnet_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info)
