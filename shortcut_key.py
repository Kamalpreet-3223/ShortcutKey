# This script is for setting custom hot-keys to open applications.
# Please make use of comments before adding any sort of code, for understanding.

from pynput.keyboard import Key,KeyCode,Listener
import subprocess as sp

extproc = None

def function_1():
    print("Hello World!")

def function_2():
    print("Hello 2!!")

# Here it is the patten of the keys
combination_to_function={
    frozenset([Key.ctrl_l, Key.alt_l, KeyCode(75)]): function_1,  #75 -> K
    frozenset([Key.ctrl_l, Key.alt_l, KeyCode(80)]): function_1   #80 -> P
}

