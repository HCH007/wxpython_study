#!/usr/bin/env python

import wx
import sys


class Frame(wx.Frame):

	def __init__(self, parent, id, title, style):
		# print("Frame __init__")
		wx.Frame.__init__(self, parent=parent, id=id, title=title, style=style)


class App(wx.App):

	def __init__(self):
		# print("App __init___")
		wx.App.__init__(self)

	def OnInit(self):
		# print("OnInit")
		self.frame = Frame(parent=None, id=-1, title="Startup",
						   style=wx.SYSTEM_MENU)
		self.frame.Show()
		self.SetTopWindow(self.frame)
		# print(sys.stderr, "Something")
		return True

	def OnExit(self):
		print("OnExit")


if __name__ == '__main__':
	app = App()
	print("before MainLoop")
	app.MainLoop()
	print("after MainLoop")