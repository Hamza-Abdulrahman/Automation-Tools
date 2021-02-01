#!/usr/bin/python3

import fbchat

from fbchat import Client

from fbchat.models import *

account = fbchat.Client('<Your Email>' , '<Your Password>')

account.sendMessage(message='Masseges',thread_id='<id target>',thread_type=ThreadType.USER)
