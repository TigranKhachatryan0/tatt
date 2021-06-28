#!/usr/bin/env python3

# TIGRAN'S ADVANCED TEXT TOOL TATT

import sys
import quopri
import os
import contextlib
import importlib
# quoted-printable support
#base64 enc, dec, enc_newline
#quoted-printable enc, dec
#url enc, full_enc, dec
#saml dec
#ascii->hex
#hex->ascii
#armscii->unicode
#unicode->armscii
#sha1
#sha224
#sha256
#sha384
#sha512

import glob
sys.path.insert(0, '.')

def isinteger(isinteger_target):
    try: int(isinteger_target); info_print_very_verbose("[isinteger] >> \"" + isinteger_target + "\" is an integer"); return True
    except: info_print_very_verbose("[isinteger] >> \"" + isinteger_target + "\" is not an integer"); return False

def info_print(info_print_target="Something was supposed to happen here"):
    if "--verbose" in sys.argv or "-v" in sys.argv or "--very-verbose" in sys.argv or "-vv" in sys.argv:
        print("[information] >> " + info_print_target)

def info_print_very_verbose(info_print_target="Something was supposed to happen here"):
    if "--very-verbose" in sys.argv or "-vv" in sys.argv:
        print("[information] >> " + info_print_target)

# Case insensitive, defaults to y and n
def choice(availablechoices="yn"):
    while True:
        choice_input= input("choice[" + ", ".join(str(availablechoices)) + "] ")
        if len(choice_input) == 1 and choice_input.lower() in availablechoices.lower():
            return choice_input
        else:
            continue

def encode_decode(mode, elist):
    print("(ENCODE/DECODE/STOP)? ")
    while True:
        encode_decode_choice = choice("eds")
        if encode_decode_choice == "e":
            print("Write \"\\n\" (without quotations) to put a new line")
            if not('do_not_use_backslash_n_for_new_line' in locals() and 'do_not_use_backslash_n_for_new_line' in globals()):
                encode_decode_string_to_encode = input("input:string_to_encode= ").replace("\\n", "\n")
            else:
                encode_decode_string_to_encode = input("input:string_to_encode= ")
            print("[confirmation] >> Are you sure?")
            # Because choice() defaults to y and n as available choices, we don't need to specify the options.
            if choice() == "y":
                @contextlib.contextmanager
                def redirect_argv():
                    sys._argv = sys.argv[:]
                    sys.argv=["--daemon"]
                    yield
                    sys.argv = sys._argv
                with redirect_argv():
                    ModuleFilename = elist[elist.index(str(mode)) + 1]
                    ModuleName=ModuleFilename[0:len(ModuleFilename)-3]
                    encodingplugin = __import__(ModuleName)
                    print(encodingplugin.EncodeText(encode_decode_string_to_encode))
            else:
                continue
        elif encode_decode_choice == "d":
            encode_decode_string_to_decode = input("input:string_to_decode= ")
            print("[confirmation] >> Are you sure?")
            if choice() == "y":
                @contextlib.contextmanager
                def redirect_argv():
                    sys._argv = sys.argv[:]
                    sys.argv=["daemon"]
                    yield
                    sys.argv = sys._argv
                with redirect_argv():
                    ModuleFilename = elist[elist.index(str(mode)) + 1]
                    ModuleName=ModuleFilename[0:len(ModuleFilename)-3]
                    decodingplugin = __import__(ModuleName)
                    print(decodingplugin.DecodeText(encode_decode_string_to_decode))
            else:
                continue
        elif encode_decode_choice == "s":
            break
        else:
            continue


def set_tatt_mode(mode_number, execlist):
    # Compatibility thing, probably will be removed soon
    execlist[execlist.index(str(mode_number)) + 1]
    encode_decode(mode_number, execlist)

def main():
    print("""================================
        Welcome to TATT
================================
       Interactive mode
================================
        """)
    os.chdir(os.path.dirname(os.path.realpath(__file__))+"/plugins")
    listlength=1
    executablelist=[]
    for i in glob.glob("./.*.info/name"):
        with open(i, 'r') as f:
            print("[" + str(listlength) + "]: " + f.read(), end="")
        with open("./." + i[3:len(i)-10] + ".info/description", 'r') as f:
            print(" " + len(str(listlength))*" " + "   " + f.read(), end="")
        executablelist.append(str(listlength))
        executablelist.append(i[3:len(i)-10])
        listlength=listlength+1
    print("[q]: Quit\n     Exit the program")
    while True:
        info_print_very_verbose("[while true loop] >> input str(tatt_mode)")
        tatt_mode = input("input:tatt_mode= ")
        info_print_very_verbose("checking if str(tatt_mode) is 'q' or an integer")
        if tatt_mode == "q" or isinteger(tatt_mode):
            info_print_very_verbose("starting to check for valid arguments...")
            info_print_very_verbose("checking if str(tatt_mode) is 'q'")
            if tatt_mode == "q":
                info_print_very_verbose("str(tatt_mode) == 'q'")
                break
            else:
                info_print_very_verbose("str(tatt_mode) is not equal to 'q'")
                info_print_very_verbose("str(tatt_mode) meets the requirements, but the TATT doesn't know how to handle it, launching file...")
                set_tatt_mode(int(tatt_mode), executablelist)
            break
        info_print("invalid input")
        info_print_very_verbose("[while true loop] >> restarting loop")

main()
