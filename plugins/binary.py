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
    bits = bin(int.from_bytes(ToEncode.encode("utf-8", "surrogatepass"), 'big'))[2:]
    return " ".join(EachXCharacter(bits.zfill(8 * ((len(bits) + 7) // 8)), 8))

def DecodeText(ToDecode=TargetText()):
    n = int(ToDecode.replace(" ", "").replace("0b", ""), 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode("utf-8", "surrogatepass") or '\0'

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
