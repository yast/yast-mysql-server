#!/usr/bin/env python

#
# File:	mysql-server/Mysql.py
# Package:	Configuration of mysql-server
# Summary:	SCR.Read() and SCR.Write()
# Authors:	Christian Kornacker <ckornacker@suse.de>
#		Jozef Uhliarik <juhliarik@suse.cz>
#
# $Id: Mysql.py 43761 2008-01-21 10:01:31Z ckornacker $
#

from ycp import *
import gettext
from gettext import textdomain
textdomain('mysql')

import_module('Progress')
import_module('Report')
import_module('Message')
import_module('Wizard')


import time
from ycp import *

# This values are going to be read
client_vars	=  ('port', '')
mysqld_vars	=  ('key_buffer', 'table_cache', 'sort_buffer_size', 
		   'read_buffer_size', 'read_rnd_buffer_size', 
		   'query_cache_size', 'bdb_cache_size', 
		   'innodb_data_file_path', 'innodb_buffer_pool_size', 
		   'innodb_log_file_size', '')
mysqldump_vars	=  ('')
isamchk_vars	=  ('key_buffer', 'sort_buffer_size', '')
myisamchk_vars	=  ('key_buffer', 'sort_buffer_size', '')
client = {}
mysqld = {}
isamchk = {}
myisamchk = {}

def Read() :

    	#/* MySQL read dialog caption */
    	caption = 'Initializing the MySQL Configuration'

    	steps = 2

    	Progress.New( caption, ' ', steps, [
		'Read the current MySQL configuration',
		'Read the current MySQL state'
	  ], [

		"Reading the current MySQL configuration...",

	    	"Reading the current MySQL state...",

	    	Message.Finished()
	  ],
	  ''
    	)

	for var in client_vars:
		client[var] = SCR.Read(Path('.etc.my.value.client.' + var))

	for var in mysqld_vars:
		mysqld[var] = SCR.Read(Path('.etc.my.value.mysqld.' + var))

	for var in mysqldump_vars:
		mysqldump[var] = SCR.Read(Path('.etc.my.value.mysqldump.' + var))

	for var in isamchk_vars:
		isamchk[var] = SCR.Read(Path('.etc.my.value.isamchk.' + var))

	for var in myisamchk_vars:
		myisamchk[var] = SCR.Read(Path('.etc.my.value.myisamchk.' + var))

    	if False: 
	    return False
    	Progress.NextStage()
    	#/* Error message */
    	if False: 
	    Report.Error(Message.CannotReadCurrentSettings())
    	time.sleep(1)

    	if False: 
	    return False
    
    	Progress.NextStep()
    	#/* Error message */
    	if False:
	     Report.Error('Cannot read the current MySQL state.')
    	time.sleep(1)

    	if False: 
	    return False
    
    	Progress.NextStage ()
    	time.sleep(1)
   
    	return True



#def Write(mysqld, client, mysqld_settings, client_settings) :
def Write() :
    	#/* MySQL read dialog caption */
    	caption = 'Saving the MySQL Configuration'

    	steps = 2
    
    	Progress.New(caption, ' ', steps, [
	    	#/* Progress stage 1/2 */
	    	'Write the MySQL settings',
	    	#/* Progress stage 2/2 */
	    	'Adjust the MySQL service'
	   ], [
	    	#/* Progress step 1/2 */
	    	'Writing the MySQL settings...',
	    	#/* Progress step 2/2 */
	    	'Adjusting the MySQL service...',
	    	Message.Finished()	
	   ],
	   ''
    	)

#	for var in client_vars:
#		SCR.Write(Path('.etc.my.value.client.' + var), client_vars[var])
#
#	for var in mysqld_vars:
#		SCR.Write(Path('.etc.my.value.mysqld.' + var), mysqld_vars[var])
#
#	for var in mysqldump_vars:
#		SCR.Write(Path('.etc.my.value.mysqldump.' + var), mysqldump_vars[var])
#
#	for var in isamchk_vars:
#		SCR.Write(Path('.etc.my.value.isamchk.' + var), isamchk_vars[var])
#
#	for var in myisamchk_vars:
#		SCR.Write(Path('.etc.my.value.myisamchk.' + var), myisamchk_vars[var])

    	time.sleep(1)

    	if False: 
		return False
    	Progress.NextStage()
    	#/* Error message */
    	if False: 
		Report.Error ('Cannot write the MySQL settings.')
    	time.sleep(1)

    	if False: 
		return False
    	Progress.NextStage ()
    	#/* Error message */
    	if False: 
		Report.Error (Message.CannotAdjustService('mysql'))
    	time.sleep(1)

    	Progress.NextStage ()
    	time.sleep(1)

    	return True


def ReadDialog():
	
#	Wizard.RestoreHelp('Any text for help')
#	Wizard.SetTitleIcon('yast-mysql')
	ret = Read()
	if ret:
		return Symbol('next')
	else:
		return Symbol('abort')


def WriteDialog() :
#	Wizard.RestoreHelp('Any text for help 2')
#	Wizard.SetTitleIcon('yast-mysql')
	ret = Write()
	if ret:
		return Symbol('next')
	else:
		return Symbol('abort')

