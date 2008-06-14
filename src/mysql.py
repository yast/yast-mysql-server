#!/usr/bin/env python

#
# File:	mysql-server/mysql.py
# Package:	Configuration of mysql-server
# Summary:	module description
# Authors:	Christian Kornacker <ckornacker@suse.de>
#		Jozef Uhliarik <juhliarik@suse.cz>
#
# $Id: mysql.py 43761 2008-01-21 10:01:31Z ckornacker $
#

from ycp import *
import gettext
from gettext import textdomain
textdomain('mysql')
init_ui('qt')

import_module('Progress')
import_module('Report')
import_module('CommandLine')
import_module('Path')

import  wizards
import  Mysql

from ycp import *



cmdline_description = {
    'id' 	: 'mysql',
    'help'		: 'Configuration of mysql',
    'guihandler'        : wizards.MysqlSequence,
    'initialize'        : Code(Mysql.Read),
    'finish'            : Code(Mysql.Write),
    'actions'           : {
    	'ports' : {
	    'help' : 'Ports used by MySQL Server',
	    'example' : [
		'ports show',
		'ports add=3306',
		'ports remove=3306',
	    ],
	}
    },
    'options'		: {    
        'show' : {
	     'help' : 'Show current settings'
	},
	'add' : {
	    'type' : 'string',
	    #// TRANSLATORS: CommandLine help
	    'help' : 'Add a new record',
	},
	'remove' : {
	    'type' : 'string',
	    #// TRANSLATORS: CommandLine help
	    'help' : 'Remove a record'
	}
    },
    'mappings'		: {
        'ports' : [
	    'show', 'add', 'remove'
	]
    }
}

#/* main ui function */

if __name__ == "__main__":
	

	ret = None
	ret = CommandLine.Run(cmdline_description);

	print ret


