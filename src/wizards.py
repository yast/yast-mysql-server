#!/usr/bin/env python

#
# File:	mysql-server/wizards.py
# Package:	Configuration of mysql-server
# Summary:	Dialog Sequence
# Authors:	Christian Kornacker <ckornacker@suse.de>
#		Jozef Uhliarik <juhliarik@suse.cz>
#
# $Id: wizards.py 43761 2008-01-21 10:01:31Z ckornacker $
#

from ycp import *
import gettext
from gettext import textdomain
textdomain('mysql')


import_module('Sequencer')
import_module('Wizard')
import_module('UI')


from ycp import *
import dialogs
import Mysql


def MainSequence():
	

    	aliases = {
	   	'server_type' : Code(dialogs.ServerTypeDialog),
	   	'server_usage' : Code(dialogs.DatabaseUsageDialog),
	   	'server_connections' : Code(dialogs.ServerConnectionsDialog),
	   	'server_networking' : Code(dialogs.ServerNetworkingDialog),
	   	'server_characterset' : Code(dialogs.CharacterSetDialog),
	   	'server_security' : Code(dialogs.SecurityConfigurationDialog)
    	}

    	sequence = {
		'ws_start' : 'server_type',
		'server_type' : {
	    		Symbol('abort')	: Symbol('abort'),
	    		Symbol('next')	: 'server_usage'
		},
		'server_usage' : {
	    		Symbol('abort')	: Symbol('abort'),
	    		Symbol('next')	: 'server_connections'
		},
		'server_connections' : {
	    		Symbol('abort')	: Symbol('abort'),
	    		Symbol('next')	: 'server_networking'
		},
		'server_networking' : {
	    		Symbol('abort')	: Symbol('abort'),
	    		Symbol('next')	: 'server_characterset'
		},
		'server_characterset' : {
	    		Symbol('abort')	: Symbol('abort'),
	    		Symbol('next')	: 'server_security'
		},
		'server_security' : {
	    		Symbol('abort')	: Symbol('abort'),
	    		Symbol('next')	: Symbol('next')
		}
	}
    
	#Wizard.CreateDialog()
    	#Wizard.SetTitleIcon('yast-mysql')
    	ret = Sequencer.Run(aliases, sequence)
	#UI.CloseDialog()
    	return ret



def MysqlSequence() :

    	aliases = {
		'read'	: [Code(Mysql.ReadDialog), True],
		'main'	: Code(MainSequence),
		'write'	: Code(Mysql.WriteDialog)
    	}

    	sequence = {
		'ws_start' : 'read',
		'read' 	: {
	    		Symbol('abort')	: Symbol('abort'),
	    		Symbol('next')	: 'main'
		},
		'main' : {
	    		Symbol('abort')	: Symbol('abort'),
	    		Symbol('next')	: 'write'
		},
		'write' : {
	    		Symbol('abort')	: Symbol('abort'),
	    		Symbol('next')	: Symbol('next')
		}
    	}

    	Wizard.CreateDialog()
    	Wizard.SetTitleIcon('yast-mysql')

    	ret = Sequencer.Run(aliases, sequence)

    	UI.CloseDialog()
    	return ret
