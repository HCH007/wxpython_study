#!/usr/bin/env python
"""A Sample for learning wxpython"""

import wx

class Frame(wx.Frame):
	"""Frame that displays an image."""

	def __init__(self, image, parent=None, id=-1, pos=wx.DefaultPosition, title="image-display"):
		tmp = image.ConvertToBitmap()
		size = tmp.GetWidth(), tmp.GetHeight()
		wx.Frame.__init__(self, parent, id, title, pos, size)
		self.bmp = wx.StaticBitmap(parent=self, bitmap=tmp)


class App(wx.App):

	def OnInit(self):
		image = wx.Image("img/1.jpg", wx.BITMAP_TYPE_JPEG)
		self.frame = Frame(image)

		self.frame.Show()
		self.SetTopWindow(self.frame)
		return True

if __name__ == '__main__':
	app = App()
	app.MainLoop()