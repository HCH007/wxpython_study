import wx


class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Text Entry Example", size=(300, 100))
        panel = wx.Panel(self, -1)
        basiclabel = wx.StaticText(panel, -1, "Basic Control:")
        basictext = wx.TextCtrl(panel, -1, "I've entered some text!", size=(175, -1))
        basictext.SetInsertionPoint(0)
        pwdlabel = wx.StaticText(panel, -1, "Password:")
        pwdtext = wx.TextCtrl(panel, -1, "password", size=(175, -1), style=wx.TE_PASSWORD)
        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([basiclabel, basictext, pwdlabel, pwdtext])
        panel.SetSizer(sizer)


class MulFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "TextEntry Example", size=(300, 250))
        panel = wx.Panel(self, -1)
        multilabel = wx.StaticText(panel, -1, "Multi-Line")
        self.multitext = wx.TextCtrl(panel, -1, "Here is a loooooooooooooong line of text set in the control.\n\n"
                                                "See that is wrapped, and that this line is after a blank",
                                     size=(200, 100), style=wx.TE_MULTILINE)
        self.multitext.SetInsertionPoint(6)

        richlabel = wx.StaticText(panel, -1, "Rich Text")
        richtext = wx.TextCtrl(panel, -1, "If supported by the native control, "
                                          "this is reversed, and this is a different font.",
                               size=(200, 100), style=wx.TE_MULTILINE | wx.TE_RICH2)
        richtext.SetInsertionPoint(1)
        richtext.SetStyle(1, 2, wx.TextAttr("white", "black"))
        points = richtext.GetFont().GetPointSize()
        f = wx.Font(points + 5, wx.ROMAN, wx.ITALIC, wx.BOLD, True)
        richtext.SetStyle(68, 82, wx.TextAttr("blue", wx.NullColour, f))
        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([multilabel, self.multitext, richlabel, richtext])
        panel.SetSizer(sizer)

        self.Bind(wx.EVT_TEXT, self.ontext, self.multitext)

    def ontext(self, event):
        self.multitext.SetValue("就是不让你改，嘻嘻")


if __name__ == "__main__":
    app = wx.App()
    frame = MulFrame()
    frame.Show()
    app.MainLoop()
