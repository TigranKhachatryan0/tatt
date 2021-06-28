#!/usr/bin/env python3
# Add the following lines to each plugin and do not edit them:
# BEGIN
import sys
sys.path.insert(0, '.')
from pluginsupport import *
# END

import base64

if NoParametersProvided():
    DisplayNoJobError()

def EncodeText(ToEncode=TargetText()):
    return base64.b32encode(bytes(ToEncode, "utf-8")).decode("utf-8")

def DecodeText(ToDecode=TargetText()):
    return base64.b32decode(bytes(ToDecode, "utf-8")).decode("utf-8")

if JobIsEncoding():
    print( EncodeText() )
elif JobIsDecoding():
    print( DecodeText() )
elif JobIsDaemon():
    pass
else:
    print("A bug has occurred. Please report the bug to TATT maintainers.")
    DebugInformation("ParseArguments(sys.argv)[0] is not equal to either \"encode\" or \"decode\"")
    DebugInformation("ParseArguments(sys.argv)[0] == " + ParseArguments(sys.argv)[0])
    MaintainerInfo("Tigran Khachatryan", "Discord: Tigran#2210, sorry for the crash =(\nHave you done any changes to plugins/base64.py?", "tigrank@mail.com")
