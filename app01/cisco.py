#!/usr/bin/env python
import telnetlib
import time

def cisco_telnet_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info):
	command1 = 'show access-lists'
	command2 = 'show running-config interface ' + port1_info
	command3 = 'show running-config interface ' + port2_info
	tn = telnetlib.Telnet(ip_info)
	tn.read_until('Username:')
	tn.write(user_info + '\n')
	tn.read_until('Password:')
	tn.write(passwd1_info + '\n')
	tn.read_until('>')
	tn.write('enable\n')
	tn.read_until('Password:')
	tn.write(passwd2_info + '\n')
	time.sleep(1)
	r1 = tn.read_very_eager()
	tn.write(command1 + '\n')
	time.sleep(1)
	r2 = tn.read_very_eager()
	tn.write(command2 + '\n')
	time.sleep(1)
	r3 = tn.read_very_eager()
	tn.write(command3 + '\n')
	time.sleep(1)
	r4 = tn.read_very_eager()
	tn.close()
	return r2,r3,r4

