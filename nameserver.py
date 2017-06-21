#!/usr/bin/python

import vymgmt

def createnameserver(ip):
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
        vyos.set("system name-server %s" %(ip))
        vyos.commit()
        vyos.save()
        vyos.exit()
        vyos.logout()

def readnameserver():
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
	vyos.configure()
        print (vyos.run_conf_mode_command("show system name-server"))
        x = vyos.run_conf_mode_command("show system name-server")
	vyos.exit()
        vyos.logout()
        return x

def delnameserver(ip):
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
        vyos.delete("system name-server %s" %(ip))
        vyos.commit()
        vyos.save()
        vyos.exit()
        vyos.logout()

def updatenameserver(ip,ip1):
        vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
        vyos.delete("system name-server %s" %(ip))
        vyos.set("system name-server %s" %(ip1))
        vyos.commit()
        vyos.save()
        vyos.exit()
        vyos.logout()
