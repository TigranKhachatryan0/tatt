import sys
import shlex
import logging

logging.basicConfig(filename='../logs.txt', level=logging.DEBUG)

def Info(message="Something was supposed to happen here"):
    print("[information] >> " + str(message))
    f = open("../logs/info.txt", "a")
    f.write(message + "\n")
    f.close()
def Error(message="Unknown error"):
    print("[\033[91merror\033[0m] >> " + str(message))
    f = open("../logs/errors.txt", "a")
    f.write(message + "\n")
    f.close()
def Warning(message="A warning was issued by the plug-in"):
    print("[\033[93mwarning\033[0m] >> " + message)
    f = open("../logs/warnings.txt", "a")
    f.write(message + "\n")
    f.close()
def DebugInformation(message="Plugin is still running"):
    print("[\033[93mdebug\033[0m] >> " + message)
    f = open("../logs/debug.txt", "a")
    f.write(message + "\n")
    f.close()

def MaintainerInfo(PluginMaintainerName,PluginMaintainerAdditionalNotes, PluginMaintainerEmail="<unknown>"):
    print("Maintainer of the plugin: " + PluginMaintainerName)
    print("Email of the maintainer: " + PluginMaintainerEmail)
    print("Additional notes from the maintainer:\n\n===========\n\n" + PluginMaintainerAdditionalNotes + "\n\n===========")

# Copy pasted from internet because I was lazy :P
# WARNING COPY PASTE BELOW
# BEGIN
def EachXCharacter(line, n=1):
    return [line[i:i+n] for i in range(0, len(line), n)]
# END

def ParseArguments(arguments=sys.argv):
    if "--encode" in arguments:
        return ["encode", str(arguments[arguments.index('--encode') + 1])]
    elif "--decode" in arguments:
        return ["decode", str(arguments[arguments.index('--decode') + 1])]
    elif "--daemon" in arguments:
        return "daemon"
    else:
        return "NOARGS"

def RotateLeft(text, alphabet="ZABCDEFGHIJKLMNOPQRSTUVWXYZzabcdefghijklmnopqrstuvwxyz00123456789  --++==``~~__[[]]\{\{\}\};;::\"\"''\\\\||<<>>??//!!@@##$$\%\%^^&&**(())\n\n"):
    alphabetlist=EachXCharacter(alphabet)[::-1]
    textlist=EachXCharacter(text)
    alphabetlist.append("\\n")
    alphabetlist.append("\\n")
    toReturn=""
    for i in textlist:
        toReturn=toReturn + alphabetlist[alphabetlist.index(i)+1]
    return toReturn

def RotateRight(text, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZAabcdefghijklmnopqrstuvwxyza01234567890  --++==``~~__[[]]\{\{\}\};;::\"\"''\\\\||<<>>??//!!@@##$$\%\%^^&&**(())\n\n"):
    alphabetlist=EachXCharacter(alphabet)
    textlist=EachXCharacter(text)
    alphabetlist.append("\\n")
    alphabetlist.append("\\n")
    toReturn=""
    for i in textlist:
        toReturn=toReturn + alphabetlist[alphabetlist.index(i)+1]
    return toReturn

def DisplayNoJobError(arguments=sys.argv):
    Error("Plugin has no job, quitting...")
    DebugInformation("ParseArguments(sys.argv)[0] is not equal to either \"encode\" or \"decode\"")
    DebugInformation("ParseArguments(sys.argv) == " + ParseArguments(arguments) + " =>")
    DebugInformation("=> ParseArguments(sys.argv)[0] == " + ParseArguments(arguments)[0])
    Info("Exitting with return code 1...")
    sys.exit(1)

def NoParametersProvided():
    return ParseArguments() == "NOARGS"

def JobIsEncoding():
    return ParseArguments(sys.argv)[0] == "encode"

def JobIsDecoding():
    return ParseArguments(sys.argv)[0] == "decode"

def TargetText():
    return ParseArguments()[1]

def JobIsDaemon():
    return ParseArguments(sys.argv) == "daemon"
