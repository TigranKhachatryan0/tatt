#!/usr/bin/env python3
# Add the following lines to each plugin and do not edit them:
# BEGIN
import sys
sys.path.insert(0, '.')
from pluginsupport import *
# END

if NoParametersProvided():
    DisplayNoJobError()

def EncodeText(ToEncode=TargetText()):
    return RotateRight(RotateRight(RotateRight(RotateRight(RotateRight(RotateRight(RotateRight(RotateRight(RotateRight(RotateRight(RotateRight(RotateRight(RotateRight(ToEncode)))))))))))))

def DecodeText(ToDecode=TargetText()):
    return RotateRight(RotateRight(RotateRight(RotateRight(RotateRight(RotateRight(RotateRight(RotateRight(RotateRight(RotateRight(RotateRight(RotateRight(RotateRight(ToDecode)))))))))))))

if JobIsEncoding():
    print(EncodeText(TargetText()))
elif JobIsDecoding():
    print(DecodeText(TargetText()))
elif JobIsDaemon():
    pass
else:
    print("A bug has occurred. Please report the bug to TATT maintainers.")
    DebugInformation("ParseArguments(sys.argv)[0] is not equal to either \"encode\" or \"decode\"")
    DebugInformation("ParseArguments(sys.argv)[0] == " + ParseArguments(sys.argv)[0])
    MaintainerInfo("Tigran Khachatryan", "Discord: Tigran#2210, sorry for the crash =(\nHave you done any changes to plugins/rot64.py?", "tigrank@mail.com")
