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
    Encoded= ToEncode.lower().replace("n", "[14]").replace("1", "[n1]").replace("2", "[n2]").replace("3", "[n3]").replace("4", "[n4]").replace("5", "[n5]").replace("6", "[n6]").replace("7", "[n7]").replace("8", "[n8]").replace("9", "[n9]").replace("a", "[1]").replace("b", "[2]").replace("c", "[3]").replace("d", "[4]").replace("e", "[5]").replace("f", "[6]").replace("g", "[7]").replace("h", "[8]").replace("i", "[9]").replace("j", "[10]").replace("k", "[11]").replace("l", "[12]").replace("m", "[13]").replace("o", "[15]").replace("p", "[16]").replace("q", "[17]").replace("r", "[18]").replace("s", "[19]").replace("t", "[20]").replace("u", "[21]").replace("v", "[22]").replace("w", "[23]").replace("x", "[24]").replace("y", "[25]").replace("z", "[26]").replace(" ", "[0]").replace(",", "[comma]").replace("\"", "[quotation]").replace("'", "[apostrophe]").replace(";", "semicolon").replace("?", "question").replace("!", "[exclamation]").replace(".", "[fullstop]").replace("#", "[octothorpe]").replace("~", "[tilde]").replace("`", "[backquote]").replace("^", "[caret]").replace("*", "[asterik]").replace("-", "[hyphen]").replace("{", "[leftcurlybrace]").replace("}", "[rightbrace]").replace("/", "[slash]").replace("\\", "[backslash]").replace("(", "[leftbrace]").replace(")", "[rightbrace]").replace("=", "[equals]")
    return Encoded

def DecodeText(ToDecode=TargetText()):
    Decoded=ToDecode.replace("[14]", "n").replace("[1]", "a").replace("[2]", "a").replace("[3]", "c").replace("[4]", "d").replace("[5]", "e").replace("[6]", "f").replace("[7]", "g").replace("[8]", "h").replace("[9]", "i").replace("[10]", "j").replace("[11]", "k").replace("[12]", "l").replace("[13]", "m").replace("[14]", "n").replace("[15]", "o").replace("[16]", "p").replace("[17]", "q").replace("[18]", "r").replace("[19]", "s").replace("[20]", "t").replace("[21]", "u").replace("[22]", "v").replace("[23]", "w").replace("[24]", "x").replace("[25]", "y").replace("[26]", "z").replace("[comma]", ",").replace("\"", "[quotation]").replace("[apostrophe]", "'").replace("[semicolon]", ";").replace("[question]", "?").replace("[exclamation]", "!").replace("[fullstop]", ".").replace("[0]", " ").replace("[n1]", "1").replace("[n1]", "1").replace("[n2]", "2").replace("[n3]", "3").replace("[n4]", "4").replace("[n5]", "5").replace("[n6]", "6").replace("[n7]", "7").replace("[n8]", "8").replace("[n9]", "9").replace("[octothorpe]", "#").replace("[tilde]", "~").replace("[backquote]", "`").replace("[caret]", "^").replace("[asterik]", "*").replace("[hyphen]", "-").replace("[leftcurlybrace]", "{").replace("[rightcurlybrace]", "}").replace("[slash]", "/").replace("[backslash]", "\\").replace("[leftbrace]", "(").replace("[rightbrace]", ")").replace("[equals]", "=")
    return Decoded

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
    MaintainerInfo("Tigran Khachatryan", "Discord: Tigran#2210, sorry for the crash =(\nHave you done any changes to plugins/base64.py?", "tigrank@mail.com")
