#!python3
#encoding:utf-8
from tkinter import Tk
# case python2: from Tkinter import Tk
import AuthList

username = 'github_username'
password = 'password'
auth = AuthList.AuthList()
# get one-time-password from clipboard
otp = Tk().clipboard_get()
auth.get(username, password, otp)
