import wx
from example1 import SketchWindow
import _pickle as cPickle
import os
import controlpn
from aboutFrame import SketchAbout

class SketchFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Sketch Frame", size = (800, 600))
        self.filename = ""
        self.title = "Sketch Frame"
        self.sketch = SketchWindow(self, -1)
        self.sketch.Bind(wx.EVT_MOTION, self.OnSketchMotion)
        self.initStatusBar()
        self.createMenuBar()
        self.createPanel()

    def createPanel(self):
        controlPanel = controlpn.ControlPanel(self, -1, self.sketch)
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(controlPanel, 0, wx.EXPAND)
        box.Add(self.sketch, 1, wx.EXPAND)
        self.SetSizer(box)

    def SaveFile(self):
        if self.filename:
            data = self.sketch.GetLinesData()
            f = open(self.filename, "wb")
            cPickle.dump(data, f)
            f.close()

    def ReadFile(self):
        if self.filename:
            try:
                f = open(self.filename, "rb")
                data = cPickle.load(f)
                f.close()
                self.sketch.SetLinesData(data)
            except cPickle.UnpicklingError:
                wx.MessageBox("%s is not a sketch file." % self.filename, "Error", style=wx.OK|wx.ICON_EXCLAMATION)

    wildcard = "Sketch files (*.sketch)|*.sketch"

    def OnOpen(self, event):
        dlg = wx.FileDialog(self, "Open sketch file...", os.getcwd(),
                            style=wx.FD_OPEN, wildcard=self.wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.ReadFile()
            self.SetTitle(self.title + "--" + self.filename)
        dlg.Destroy()

    def OnSave(self, event):
        if not self.filename:
            self.OnSaveAs(event)
        else:
            self.SaveFile()

    def OnSaveAs(self, event):
        dlg = wx.FileDialog(self, "Save sketch as...", os.getcwd(),
                            style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT,
                            wildcard=self.wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            if not os.path.splitext(filename)[1]:
                filename = filename + ".sketch"
            self.filename = filename
            self.SaveFile()
            self.SetTitle(self.title + "--" + self.filename)
            dlg.Destroy()

    def OnAbout(self, event):
        dlg = SketchAbout(self)
        dlg.ShowModal()
        dlg.Destroy()

    def initStatusBar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -3])

    def OnSketchMotion(self, event):
        self.statusbar.SetStatusText("Pos: %s" %str(event.GetPosition()), 0)
        self.statusbar.SetStatusText("Current Pts: %s" %len(self.sketch.curLine), 1)
        self.statusbar.SetStatusText("Line Count: %s" %len(self.sketch.lines), 2)
        event.Skip()


    @property
    def menuData(self):
        return [("&File",(
                    ("&New", "New Sketch file", self.OnNew),
                    ("&Open", "Open sketch file", self.OnOpen),
                    ("&Save", "Save sketch file", self.OnSave),
                    ("", "", ""),
                    ("&Quit", "Quit", self.OnCloseWindow, wx.ITEM_NORMAL))
                 ),
                ("&Edit",(
                    [("&Color", (
                        ("(0, 0, 0)", "The color selected", None, wx.ITEM_NORMAL, 12345),
                        ("", "", ""),
                        ("&Black", "", self.OnColor, wx.ITEM_RADIO),
                        ("&Red", "", self.OnColor, wx.ITEM_RADIO),
                        ("&Green", "", self.OnColor, wx.ITEM_RADIO),
                        ("&Blue", "", self.OnColor, wx.ITEM_RADIO),
                        ("&Other...", "", self.OnOtherColor, wx.ITEM_RADIO)
                    ))]
                )
                ),
                ("&Others", (
                    ("about", "", self.OnAbout),
                    ("凑数", "凑数", None)
                )
                 )
                ]

    def OnOtherColor(self, event):
        #print("Color")
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)
        if dlg.ShowModal() == wx.ID_OK:
            self.sketch.SetColor(dlg.GetColourData().GetColour())
        #------------
        menubar = self.GetMenuBar()
        tmp = self.sketch.GetColor()
        s = "(" + str(tmp[0]) + ", " + str(tmp[1]) + ", " + str(tmp[2]) + ")"
        menubar.FindItemById(12345).SetText(s)
        dlg.Destroy()

    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenu in self.menuData:
            menuLabel = eachMenu[0]
            menuItems = eachMenu[1]
            #print(menuLabel)
            #print(menuItems)
            menuBar.Append(self.createMenu(menuItems), menuLabel)
        self.SetMenuBar(menuBar)

    def createMenu(self, menuData):
        menu = wx.Menu()
        for eachItem in menuData:
            #创建子菜单
            #print(len(eachItem))
            if len(eachItem) == 2:
                label = eachItem[0]
                subMenu = self.createMenu(eachItem[1])
                #print(label)
                #print(subMenu)
                menu.Append(wx.NewId(), label, subMenu)
            else:
                self.createMenuItem(menu, *eachItem)
        #print(menu)
        return menu

    def createMenuItem(self, menu, label, status, handler,
                       kind=wx.ITEM_NORMAL, id=-1):
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(id, label, status, kind)
        self.Bind(wx.EVT_MENU, handler, menuItem)

    def OnNew(self, event):pass

    def OnColor(self, event):
        menubar = self.GetMenuBar()
        itemId = event.GetId()
        item = menubar.FindItemById(itemId)
        color = item.GetLabel()
        self.sketch.SetColor(color)
        tmp = self.sketch.GetColor()
        s = "(" + str(tmp[0]) + ", " + str(tmp[1]) + ", " + str(tmp[2]) + ")"
        menubar.FindItemById(12345).SetText(s)
        #self.pixel = wx.Bitmap.FromRGBA(10, 10, *self.sketch.GetColor())
        #menubar.FindItemById(12345).SetBitmap(self.pixel)
        #menubar.FindItemById(12345).SetTextColour(wx.Colour(123,123,123))

        #print(self.sketch.GetColor())

    def OnCloseWindow(self, event):
        self.Destroy()

if __name__ == "__main__":
    app = wx.App()
    frame = SketchFrame(None)
    frame.Show(True)
    app.MainLoop()