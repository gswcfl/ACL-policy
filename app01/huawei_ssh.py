#!/usr/bin/env python
import time
import pexpect
import sys

def huawei_ssh_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info):
	ssh = pexpect.spawn('ssh %s@%s' %(user_info,ip_info))
	i = ssh.expect(['password:','Are you sure you want to continue connecting (yes/no)?'],timeout=5)
	time.sleep(1)
	if i == 0:
		ssh.sendline(passwd1_info)
	elif i == 1:
		ssh.sendline('yes')
		ssh.expect('password:')
		ssh.sendline(passwd1_info)
	time.sleep(1)
	if passwd2_info != 'null':
		ssh.expect('>')
		time.sleep(1)
		ssh.sendline('super')
		ssh.sendline(passwd2_info)
	time.sleep(1)
	ssh.expect('>')
	ssh.sendline('display acl all')
	ssh.expect('display acl all')
	for i in range(15):
		ssh.sendline('\n')
	ssh.expect('>')
	r2 = ssh.before
	ssh.sendline('display cur interface ' + port1_info)
	ssh.expect('display cur interface ' + port1_info)
	ssh.expect('>')
	r3 = ssh.before
	ssh.sendline('display cur interface ' + port2_info)
	ssh.expect('display cur interface ' + port2_info)
	ssh.expect('>')
	r4 = ssh.before
	return r2,r3,r4
if __name__ == '__main__':
	port1_info = 'XGigabitEthernet 0/0/0'
	port2_info = 'XGigabitEthernet 0/0/1'
	changji = 'HUAWEI'
	login_info = 'SSH'
	ip_info = '11.11.63.1'
	user_info = 'test'
	passwd1_info = 'test'
	passwd2_info = 'null'
	huawei_ssh_info(port1_info,port2_info,changji,login_info,ip_info,user_info,passwd1_info,passwd2_info)
