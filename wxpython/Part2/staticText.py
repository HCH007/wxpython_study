import wx

class StaticTextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Static Text", size=(400, 300))
        panel = wx.Panel(self, -1)

        wx.StaticText(panel, -1, "Basic Static Text", (100, 10))

        rev = wx.StaticText(panel, -1, "Static Text With Reversed Colors", (100, 10))
        rev.SetForegroundColour("white")
        rev.SetBackgroundColour("black")

        center = wx.StaticText(panel, -1, "align center", (100, 50), (160, -1), wx.ALIGN_CENTER)
        center.SetForegroundColour("white")
        center.SetBackgroundColour("black")

        right = wx.StaticText(panel, -1, "align right", (100, 70), (160, -1), wx.ALIGN_RIGHT)
        right.SetForegroundColour("white")
        right.SetBackgroundColour("balck")

        string = "You can also change the font."
        text = wx.StaticText(panel, -1, string, (20, 100))
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text.SetFont(font)

        wx.StaticText(panel, -1, "Multiple lines\nSupported\n""Nice", (20, 150))

        wx.StaticText(panel, -1, "Multiple lines\nSupported\n""Nice", (220, 150), style=wx.ALIGN_RIGHT)


if __name__ == "__main__":
    app = wx.App()
    frame = StaticTextFrame()
    frame.Show()
    app.MainLoop()