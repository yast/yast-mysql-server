#!/usr/bin/env python

#
# File:	mysql-server/defaults.py
# Package:	Configuration of mysql-server
# Summary:	default configuration settings
# Authors:	Christian Kornacker <ckornacker@suse.de>
#
# $Id: defaults.py 43761 2008-01-21 10:01:31Z ckornacker $
#

from ycp import *
import_module('UI')

# the settings dict consists of a list of values for the several my.cnf sections.
# the sections are: 	[0] => client
#			[1] => mysqld
#			[2] => mysqldump
#			[3] => isamchk
#			[4] => myisamchk
#
# i.e. if one has chosen 'Server', and the settings dict looks like this:
#	Settings = {
#		'Server' : [ { 'a_client_var' : 'a_client_var_value',
#			       'another_client_var' : 'another_value' },
#			     { 'a_mysqld_var' : 'a_mysqld_value' },
#			     {},
#			     {},
#			     { 'a_myisamchk_var' : 'a_myisamchk_value' }
#			   ]
#		   }
#
#	the values can now be grabbed like this:
#		my_choice = Settings['Server']
#		client_values = my_choice[0]
#		print client_values['another_client_var']
#		>>> another_value
#

ServerTypeSettings = {
	'Developer Machine' : [ {},
				{ 'key_buffer' : '16k',
				  'table_cache' : '4',
				  'sort_buffer_size' : '64k',
				  'read_rnd_buffer_size' : '2k' },
				{},
				{ 'key_buffer' : '4M' },
				{}
			      ],

	'Server' :            [ {},
				{ 'key_buffer' : '16M',
				  'table_cache' : '64',
				  'sort_buffer_size' : '512k',
				  'read_buffer_size' : '256k',
				  'read_rnd_buffer_size' : '512k',
				  'bdb_cache_size' : '4M',
				  'innodb_data_file_path' : 'ibdata1:10M:autoextend',
				  'innodb_buffer_pool_size' : '16M',
				  'innodb_log_file_size' : '5M' },
				{},
				{ 'key_buffer' : '4M' },
				{}
			      ],

	'Dedicated' :         [ {},
				{ 'key_buffer' : '256M',
				  'table_cache' : '256',
				  'sort_buffer_size' : '1M',
				  'read_buffer_size' : '1M',
				  'read_rnd_buffer_size' : '4M',
				  'query_cache_size' : '16M',
				  'bdb_cache_size' : '64M',
				  'innodb_data_file_path' : 'ibdata1:1000:autoextend',
				  'innodb_buffer_pool_size' : '256M',
				  'innodb_log_file_size' : '64M' },
				{},
				{ 'key_buffer' : '4M' },
				{}
			      ],
	'Custom' :            [ {},
				{},
				{},
				{},
				{}
		              ]
	}


DatabaseUsageSettings = {
	'Multifunctional' :  [ {},
				{ 'key_buffer' : '16k',
				  'read_rnd_buffer_size' : '2k' },
				{},
				{ 'key_buffer' : '4M' },
				{}
			      ],

	'Transactional' :     [ {},
				{ 'key_buffer' : '16M',
				  'innodb_log_file_size' : '5M' },
				{},
				{ 'key_buffer' : '4M' },
				{}
			      ],

	'Non-Transactional' : [ {},
				{ 'key_buffer' : '256M',
				  'innodb_log_file_size' : '64M' },
				{},
				{ 'key_buffer' : '4M' },
				{}
			      ]
	}


ServerConnectionSettings = {
	'Decision' :  [ {},
				{ 'key_buffer' : '16k',
				  'read_rnd_buffer_size' : '2k' },
				{},
				{ 'key_buffer' : '4M' },
				{}
			      ],

	'Online' :     [ {},
				{ 'key_buffer' : '16M',
				  'innodb_log_file_size' : '5M' },
				{},
				{ 'key_buffer' : '4M' },
				{}
		      ],

	'Manual' : [ {},
				{ 'key_buffer' : UI.QueryWidget(Term('id', 'Connections'), Symbol('Value')),
				  'innodb_log_file_size' : '64M' },
				{},
				{ 'key_buffer' : '4M' },
				{}
			      ]
	}


CharacterSetSettings = {
	'Standard' :          [ {},
				{ 'key_buffer' : '16k',
				  'read_rnd_buffer_size' : '2k' },
				{},
				{ 'key_buffer' : '4M' },
				{}
			      ],

	'Multilingual' :      [ {},
				{ 'key_buffer' : '16M',
				  'innodb_log_file_size' : '5M' },
				{},
				{ 'key_buffer' : '4M' },
				{}
			      ],

	'Manual' :            [ {},
				{ 'key_buffer' : UI.QueryWidget(Term('id', 'charset'), Symbol('Value')),
				  'innodb_log_file_size' : '64M' },
				{},
				{ 'key_buffer' : '4M' },
				{}
			      ]
	}

ServerFeaturesSettings = {
	'all' :               [ {},
				{ 'TCPIP' : UI.QueryWidget(Term('id', 'TCPIP'), Symbol('CurrentButton')),
		                  'Strict' : UI.QueryWidget(Term('id', 'Strict'), Symbol('CurrentButton')) },
				{},
				{}
			      ]
	}

SecuritySettings = {
	'all' :		      [ {},
				{ 'Password' : UI.QueryWidget(Term('id', 'NewPassword'), Symbol('Value')),
				  'Anonymous' : UI.QueryWidget(Term('id', 'AnonymousAccount'), Symbol('Value')) },
				{},
				{}
			      ]
	}
