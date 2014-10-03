#!/usr/bin/env python

# This is a quick script that allows execution of ssh commands
# list of machines and list of commnads

import paramiko
import os

hostname = [
]
port = 22
user =
password = 'xxxxxx'

log_path = '/var/tmp/ssh.log'

commands = ['chmod -R g+rx /opt/jboss-eap-6.1/standalone/log', 'ls -la /opt/jboss-eap-6.1/standalone/', 'ls -la /opt/jboss-eap-6.1/standalone/log']

# log file of executions
logs = open(log_path, 'w')

if __name__ == "__main__":
#       key = paramiko.RSAKey.from_private_key_file(pkey_file)
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.load_system_host_keys
        for host in hostname:
                s.connect(host,username=user,password=password)
                logs.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\n')
                logs.write('hostname: ' + host + '\n')
                for cmd in commands:        
                        stdin, stdout, sterr = s.exec_command(cmd)
                           print(sterr.read() + '\n')
                        logs.write('Command exec: ' + cmd + '\n')
                        logs.write(stdout.read() + '\n')
                logs.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\n')
                s.close
        logs.close
