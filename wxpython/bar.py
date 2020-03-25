#!/usr/bin/env python

import wx
import wx.py.images as images
from wx.py.shell import ShellFrame
from wx.py.filling import FillingFrame


class ToolbarFrame(wx.Frame):

    def __init__(self,parent, id):
        wx.Frame.__init__(self,parent, id, "Toolbars", size=(300, 200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        statusBar = self.CreateStatusBar()
        toolbar = self.CreateToolBar()
        toolbar.AddTool(101, "New", images.getPyBitmap(),
                        "Long help for 'New'")
        toolbar.Bind(wx.EVT_TOOL, self.Ontoolbar)
        toolbar.Realize()

        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menuBar.Append(menu1,"&File")
        menu2 = wx.Menu()
        menu2.Append(wx.NewId(), "&Copy", "Copy in status bar")
        menu2.Append(wx.NewId(), "C&ut", "")
        menu2.Append(wx.NewId(), "Paste", "")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(), "&Options...", "Display Options")
        menuBar.Append(menu2, "&Edit")
        menu3 = wx.Menu()
        shell = menu3.Append(-1, "&wxPython shell", "Open wxPython shell frame")
        filling = menu3.Append(-1, "&Namespace viewer", "Open namespace viewer frame")
        menuBar.Append(menu3, "&Debug")

        self.Bind(wx.EVT_MENU, self.OnShell, shell)
        self.Bind(wx.EVT_MENU, self.OnFilling, filling)

        self.SetMenuBar(menuBar)


    def Ontoolbar(self, event):
        tmp = event.GetId()
        if tmp == 101:
            dlg = wx.SingleChoiceDialog(None, "Version?","Title",
                                        ["1.0", "2.0", "3.0"])
            if dlg.ShowModal() == wx.ID_OK:
                print(dlg.GetStringSelection())

    def OnShell(self, event):
        frame=ShellFrame(parent=self)
        frame.Show()

    def OnFilling(self, event):
        frame = FillingFrame(parent=self)
        frame.Show()

if __name__ == "__main__":
    app = wx.App()
    frame = ToolbarFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()