
# Create your views here.
#!/usr/bin/env python
#-*- coding:utf-8 -*-
#

import commands
import IPy

def alert_info(ip,ip_list):
	alert = ''
	try:
		IPy.IP(ip)
		pass
	except Exception as e:
		alert = ip + ' is invalid ip address.'
		return alert
	if ip_list.has_key(ip):
		pass
	else:
		alert = ip + ' does not exist.'
		return alert
	command = 'ping ' + ip + ' -c 3 -i 0.2 -w 0.2'
	(status,output) = commands.getstatusoutput(command)
	if status == 0:
		pass
	else:
		print status
		alert = ip + ' ping unreachable.'
		return alert
	return alert
