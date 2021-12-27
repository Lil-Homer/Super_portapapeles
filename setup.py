from distutils.core import setup # Need this to handle modules
import py2exe 
import pyperclip as pyp
from pynput import keyboard as kb
import time


setup(windows=['super_portapapeles.py']) # Calls setup function to indicate that we're dealing with a single console application
