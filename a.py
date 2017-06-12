#!/usr/bin/env python
#-*- codeing:utf-8 -*-

from fabric.api import *

display local or remote host information
env.user = 'root'
env.hosts=['192.168.110.129']
env.password='111111'
@runs_once
def host_type():
	run('uname -s')

def remote_task():
	with cd('packets'):
		run('ls -l')
############################################################
dynamic obtain remote host directory list
env.user = 'root'
env.hosts=['192.168.110.129']
env.password='111111'
@runs_once
def input_raw():
	return prompt('please input diectory name:',default='/root')
def worktask(dirname):
	run('ls -l ' + dirname)
@task
def go():
	getdirname = input_raw()
	worktask(getdirname)

################################################################
#gateway mode put file and execute
from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm
env.user='root'
env.gateway='192.168.110.129'
env.hosts=['192.168.110.130','192.168.110.131']
env.passwords={
	'root@192.168.110.129:22':'111111',
	'root@192.168.110.130:22':'111111',
	'root@192.168.110.131:22':'111111',
}
lpackpath="/home/install/lnmp0.0.tar.gz"
rpackpath='/tmp/install'
@task
def put_task():
	run('mkdir -p /tmp/install')
	with settings(warn_only=True):
	result = put(lpackpath,rpackpath)
if result.failed and not confirm('put file failed,Continue[Y/N]?'):
	abort('Aborting file put task!')
@task
def run_task():
	with cd('/tmp/install'):
		run('tar -zxvf lnmp0.9.tar.gz')
		with cd('lnmp0.9/'):
			run('./centos.sh')
@task
def go():
	put_task()
	run_task()
