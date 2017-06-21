#!/usr/bin/python

import vymgmt

def createuser(username,passwd,fname):
	vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
	vyos.login()
	vyos.configure()
        vyos.set("system login user %s full-name %s" %(username,fname))
        vyos.set("system login user %s  authentication plaintext-password %s" %(username,passwd))
        vyos.set("system login user %s level admin" %(username))
        vyos.commit()
        vyos.save()
        vyos.exit()
	vyos.logout()

def readuser():
	vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        print (vyos.run_op_mode_command("show system login users"))
	y = vyos.run_op_mode_command("show system login users")
        vyos.logout()
	return y

def deluser(username):
	vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
	vyos.delete("system login user %s" %(username))
	vyos.commit()
	vyos.save()
	vyos.exit()
	vyos.logout()

def updateuser(username,username1,passwd,fname):
	vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
	vyos.delete("system login user %s" %(username))
	vyos.set("system login user %s full-name %s" %(username1,fname))
        vyos.set("system login user %s  authentication plaintext-password %s" %(username1,passwd))
        vyos.set("system login user %s level admin" %(username1))
	vyos.commit()
	vyos.save()
	vyos.exit()
	vyos.logout()

def createssh(usr):
	vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
	vyos.login()
	vyos.configure()
	vyos.run_conf_mode_command("loadkey %s scp://marcella@192.168.0.2/home/marcella/.ssh/id_rsa.pub" %(usr))
	vyos.run_conf_mode_command("Passw0rd!")
	vyos.set("service ssh disable-password-authentication")
	vyos.commit()
	vyos.save()
	vyos.exit()
	vyos.logout()

def readssh(usr):
	vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
	vyos.login()
	vyos.configure()
	#print (vyos.run_conf_mode_command("show system login user %s" %(usr)))
	x = vyos.run_conf_mode_command("show system login user %s" %(usr))
	return x
	vyos.exit()
	vyos.logout()
	#return x

def delssh(usr):
	vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
	vyos.login()
	vyos.configure()
	vyos.delete("system login user %s authentication public-keys" %(usr))
	vyos.delete("service ssh disable-password-authentication")
	vyos.commit()
	vyos.save()
	vyos.exit()
	vyos.logout()

def updatessh(usr):
	vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
	vyos.login()
	vyos.configure()
	vyos.delete("system login user %s authentication public-keys" %(usr))
        vyos.delete("service ssh disable-password-authentication")
	vyos.run_conf_mode_command("loadkey %s scp://marcella@192.168.0.2/home/marcella/.ssh/id_rsa.pub" %(usr))
        vyos.run_conf_mode_command("Passw0rd!")
        vyos.set("service ssh disable-password-authentication")
	vyos.commit()
	vyos.save()
	vyos.exit()
	vyos.logout()
