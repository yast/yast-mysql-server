#!/usr/bin/env python

#
# File:	mysql-server/dialog.py
# Package:	Configuration of mysql-server
# Summary:	dialog
# Authors:	Christian Kornacker <ckornacker@suse.de>
#
# $Id: defaults.py 43761 2008-01-21 10:01:31Z ckornacker $
#

from ycp import *

import gettext
from gettext import textdomain

textdomain('mysql')

import_module('Label')
import_module('Wizard')
import_module('UI')

from ycp import *
import Mysql

from defaults import ServerTypeSettings
from defaults import DatabaseUsageSettings
from defaults import ServerConnectionSettings
from defaults import CharacterSetSettings
from defaults import ServerFeaturesSettings
from defaults import SecuritySettings

caption = gettext.gettext('MySQL Server Configuration')

# ShowSequenceDialog
# 	contents	=
#	values		= Button/TextBox/... values
#	help		= the dialog's help text
#	back		= show 'back' button or not

def ShowSequenceDialog(contents, values, help, back):
    	Wizard.SetContentsButtons(caption, contents, help, Label.BackButton(), Label.NextButton())
    	Wizard.SetTitleIcon('yast-mysql')


	for ID in values.keys():
		UI.ChangeWidget( id(ID), Symbol('Value'), values[ID])

	if not back:
    		Wizard.DisableBackButton()
		
    	ret = None;
    	while True :
		ret = UI.UserInput()

		#abort
		if ret.value == 'abort':
	    		break

		#next
		elif ret.value == 'next':
		  	break
       
                break

	return ret;

def ServerTypeDialog():
	# specify how the dialog should look like
    	contents = VBox(
	     Left(Term('Label','MySQL Server Type')),
	     VBox(
		VSpacing(1),
		Frame(
		    'Server Type',
		    RadioButtonGroup( id( 'ServerType' ),
			    VBox(
				Left( RadioButton( id( 'Developer Machine'), '&Developer Machine')),
				Left( RadioButton( id( 'Server'), '&Server Machine')),
				Left( RadioButton( id( 'Dedicated'), 'D&edicated Machine')),
				Left( RadioButton( id( 'Custom'), '&Custom'))
			    )
			)
		),
		VStretch()
	     )
	)

	# default values
	# need to be read from my.cnf
	values = {'Server':True}

	# help text for this dialog
	help = 'Server Configuration...'

	# bring it to the screen...
    	ret = ShowSequenceDialog(contents, values, help, False);

	# chose the settings depending on which button the user has pressed
	selection = ServerTypeSettings[UI.QueryWidget(id('ServerType'), Symbol('CurrentButton'))]

	return ret
	
def DatabaseUsageDialog(): 
    	contents = VBox(
	     Left(Term('Label','Database Usage')),
	     VBox(
		VSpacing(1),
		Frame(
		    'Server Features',
		    RadioButtonGroup( id( 'DatabaseUsage' ),
			    VBox(
				Left( RadioButton( id( 'Multifunctional'), 'Multifunctional Database')),
				Left( RadioButton( id( 'Transactional'), 'Transactional Database Only')),
				Left( RadioButton( id( 'Non-Transactional'), 'Non-Transactional Database Only'))
			    )
			)
		),
		VStretch()
	     )
	)

	values = {'Transactional':True}
    
	help = 'Server Configuration...'

    	ret = ShowSequenceDialog(contents, values, help, True);

	selection = DatabaseUsageSettings[UI.QueryWidget(id('DatabaseUsage'), Symbol('CurrentButton'))]

	return ret


def ServerConnectionsDialog(): 
    	contents = VBox(
	     Left(Term('Label','Concurrent connections to the Server')),
	     VBox(
		VSpacing(1),
		Frame(
		    'Server Features',
		    RadioButtonGroup( id( 'ServerConnections' ),
			    VBox(
				Left( RadioButton( id( 'Decision'), '&Decision Support (DSS)/OLAP')),
				Left( RadioButton( id( 'Online'), '&Online Transaction Processing (OLTP)')),
				Left( RadioButton( id( 'Manual'), '&Manual Setting')),
				VBox(
					Right( TextEntry( id( 'Connections'), '&Concurrent connections:')))
			    )
			)
		),
		VStretch()
	     )
	)
    
	values = {'Decision':True}
	
	help = 'Server Configuration...'

    	ret = ShowSequenceDialog(contents, values, help, True);

	selection = ServerConnectionSettings[UI.QueryWidget(id('ServerConnections'), Symbol('CurrentButton'))]

	return ret

def ServerNetworkingDialog():
    	contents = VBox(
	     Left(Term('Label','Networking Options')),
	     VBox(
		VSpacing(1),
		Frame(
		    'Server Features',
		    VBox(
			Left( CheckBox( id( 'TCPIP'), 'Enable &TCP/IP Networking')),
			Left( CheckBox( id( 'Strict'), 'Enable &Strict Mode'))
		    )
		),
		VStretch()
	     )
	)
    
	values = {'TCPIP':True, 'Strict':True}

	help = 'Server Configuration...'

    	ret = ShowSequenceDialog(contents, values, help, True);

	return ret

def CharacterSetDialog(): 
    	contents = VBox(
	     Left(Term('Label','Character Set')),
	     VBox(
		VSpacing(1),
		Frame(
		    'Server Features',
		    RadioButtonGroup( id( 'CharacterSet' ),
			    VBox(
				Left( RadioButton( id( 'Standard'), '&Standard Character Set')),
				Left( RadioButton( id( 'Multilingual'), '&Best for Multilingual Support')),
				Left( RadioButton( id( 'Manual'), '&Manually Selected Default Character Set')),
				VBox(
					Right( SelectionBox( id( 'charset'), 'Character Set:', [ 'latin1', 'utf8' ]))
				)
			    )
			)
		),
		VStretch()
	     )
	)

	values = {'Standard':True}
 
	help = 'Server Configuration...'

    	ret = ShowSequenceDialog(contents, values, help, True);

	selection = CharacterSetSettings[UI.QueryWidget(id('CharacterSet'), Symbol('CurrentButton'))]

	return ret

def SecurityConfigurationDialog(): 
    	contents = VBox(
	     Left(Term('Label','Security Options')),
	     VBox(
		VSpacing(1),
		Frame(
		    'Server Features',
		    VBox(
			Left( CheckBox( id( 'Modify'), '&Modify MySQL Security Settings')),
			VBox(
				Right( Password( id( 'OldPassword'), 'Current root Password:')),
				Right( Password( id( 'NewPassword'), 'New root Passsword:')),
				Right( Password( id( 'Confirm'), 'Confirm new Password:'))
			),
			Left( CheckBox( id( 'AnonymousAccount'), '&Create Anonymous Account')),
		    )
		),
		VStretch()
	     )
	)
    
	help = 'Server Configuration...'
	
	values = {'AnonymousAccount':True}

    	ret = ShowSequenceDialog(contents, values, help, True);

	return ret

