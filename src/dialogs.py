#!/usr/bin/env python

#
# File:	mysql-server/dialog.py
# Package:	Configuration of mysql-server
# Summary:	dialog
# Authors:	Christian Kornacker <ckornacker@suse.de>
#
# $Id: defaults.py 43761 2008-01-21 10:01:31Z ckornacker $
#


import gettext
from gettext import textdomain

textdomain('mysql')

import ycp
ycp.import_module('UI')
from ycp import *
ycp.widget_names()
import Wizard
ycp.import_module('Label')


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
        
#        Wizard.SetContentsButtons(caption, contents, help, Label.BackButton(), Label.NextButton())
    	Wizard.SetContentsButtons(caption, contents, help, "back", "next")
#    	Wizard.SetTitleIcon('yast-mysql')


	for ID in values.keys():
		UI.ChangeWidget(Term('id',  ID), Symbol('Value'), values[ID])

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
        from ycp import *
        ycp.widget_names()

    	contents = VBox(
	     Left(Term('Label','MySQL Server Type')),
	     VBox(
		VSpacing(1),
		Frame(
		    'Server Type',
		    RadioButtonGroup(Term('id','ServerType' ),
			    VBox(
                Left( RadioButton(Term('id', 'Developer Machine'),  '&Developer Machine')),
				Left( RadioButton(Term('id', 'Server'),  '&Server Machine')),
				Left( RadioButton(Term('id', 'Dedicated'),  'D&edicated Machine')),
				Left( RadioButton(Term('id', 'Custom'),  '&Custom'))
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
	selection = ServerTypeSettings[UI.QueryWidget(Term('id', 'ServerType'), Symbol('CurrentButton'))]

	return ret
	
def DatabaseUsageDialog(): 
        from ycp import *
        ycp.widget_names()

    	contents = VBox(
	     Left(Term('Label','Database Usage')),
	     VBox(
		VSpacing(1),
		Frame(
		    'Server Features',
		    RadioButtonGroup( Term('id', 'DatabaseUsage' ),
			    VBox(
				Left( RadioButton(Term('id', 'Multifunctional'), 'Multifunctional Database')),
				Left( RadioButton(Term('id',  'Transactional'), 'Transactional Database Only')),
				Left( RadioButton( Term('id',  'Non-Transactional'), 'Non-Transactional Database Only'))
			    )
			)
		),
		VStretch()
	     )
	)

	values = {'Transactional':True}
    
	help = 'Server Configuration...'

    	ret = ShowSequenceDialog(contents, values, help, True);

	selection = DatabaseUsageSettings[UI.QueryWidget(Term('id', 'DatabaseUsage'), Symbol('CurrentButton'))]

	return ret


def ServerConnectionsDialog(): 
        from ycp import *
        ycp.widget_names()

    	contents = VBox(
	     Left(Term('Label','Concurrent connections to the Server')),
	     VBox(
		VSpacing(1),
		Frame(
		    'Server Features',
		    RadioButtonGroup(Term('id',  'ServerConnections' ),
			    VBox(
				Left( RadioButton(Term('id',  'Decision'), '&Decision Support (DSS)/OLAP')),
				Left( RadioButton(Term('id',  'Online'), '&Online Transaction Processing (OLTP)')),
				Left( RadioButton(Term('id',  'Manual'), '&Manual Setting')),
				VBox(
					Right( TextEntry(Term('id',  'Connections'), '&Concurrent connections:')))
			    )
			)
		),
		VStretch()
	     )
	)
    
	values = {'Decision':True}
	
	help = 'Server Configuration...'

    	ret = ShowSequenceDialog(contents, values, help, True);

	selection = ServerConnectionSettings[UI.QueryWidget(Term('id',  'ServerConnections'), Symbol('CurrentButton'))]

	return ret

def ServerNetworkingDialog():
        from ycp import *
        ycp.widget_names()

    	contents = VBox(
	     Left(Term('Label','Networking Options')),
	     VBox(
		VSpacing(1),
		Frame(
		    'Server Features',
		    VBox(
			Left( CheckBox(Term('id',   'TCPIP'), 'Enable &TCP/IP Networking')),
			Left( CheckBox(Term('id',  'Strict'), 'Enable &Strict Mode'))
		    )
		),
		VStretch()
	     )
	)
    
	values = {'TCPIP':True, 'Strict':True}

	help = 'Server Configuration...'

    	ret = ShowSequenceDialog(contents, values, help, True);
        tcpip=UI.QueryWidget(Term('id', 'TCPIP'),  Symbol('Value'))
        print tcpip
        CharacterSetSettings

	return ret

def CharacterSetDialog(): 
        from ycp import *
        ycp.widget_names()

    	contents = VBox(
	     Left(Term('Label','Character Set')),
	     VBox(
		VSpacing(1),
		Frame(
		    'Server Features',
		    RadioButtonGroup(Term('id',  'CharacterSet' ),
			    VBox(
				Left( RadioButton(Term('id',  'Standard'), '&Standard Character Set')),
				Left( RadioButton(Term('id',  'Multilingual'), '&Best for Multilingual Support')),
				Left( RadioButton( Term('id',  'Manual'), '&Manually Selected Default Character Set')),
				VBox(
					Right( SelectionBox(Term('id',  'charset'), 'Character Set:', [ 'latin1', 'utf8' ]))
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

	selection = CharacterSetSettings[UI.QueryWidget(Term('id',  'CharacterSet'), Symbol('CurrentButton'))]

	return ret

def SecurityConfigurationDialog(): 
        from ycp import *
        ycp.widget_names()

    	contents = VBox(
	     Left(Term('Label','Security Options')),
	     VBox(
		VSpacing(1),
		Frame(
		    'Server Features',
		    VBox(
			Left( CheckBox(Term('id',  'Modify'), '&Modify MySQL Security Settings')),
			VBox(
				Right( Password(Term('id',  'OldPassword'), 'Current root Password:')),
				Right( Password(Term('id', 'NewPassword'), 'New root Passsword:')),
				Right( Password(Term('id', 'Confirm'), 'Confirm new Password:'))
			),
			Left( CheckBox(Term('id',  'AnonymousAccount'), '&Create Anonymous Account')),
		    )
		),
		VStretch()
	     )
	)
    
	help = 'Server Configuration...'
	
	values = {'AnonymousAccount':True}

    	ret = ShowSequenceDialog(contents, values, help, True);

	return ret

