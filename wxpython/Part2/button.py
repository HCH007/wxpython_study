import wx
import wx.lib.buttons as buttons


class ButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'ButtonExample', size=(300, 100))
        panel = wx.Panel(self, -1)
        self.button = wx.Button(panel, -1, 'Hello', pos=(50, 20))
        self.Bind(wx.EVT_BUTTON, self.on_click, self.button)
        self.button.SetDefault()

    def on_click(self, event):
        self.button.SetLabel("Clicked")


class BitmapButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Bitmap Button Example',
                          size=(500, 300))
        panel = wx.Panel(self, -1)
        bmp = wx.Image("img/button-off.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, bmp, pos=(10, 20))
        self.status = False
        self.Bind(wx.EVT_BUTTON, self.on_click, self.button)
        self.button.SetDefault()

    def on_click(self, event):
        if not self.status:
            bmp = wx.Image("img/button-on.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
            self.button.SetBitmap(bmp)
            self.status = not self.status
        else:
            bmp = wx.Image("img/button-off.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
            self.button.SetBitmap(bmp)
            self.status = not self.status


class GenericButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Generic Button Example",
                          size=(500, 350))
        panel = wx.Panel(self, -1)

        sizer = wx.FlexGridSizer(3, 3, 20, 20)
        b = wx.Button(panel, -1, "A wx.Button")
        b.SetDefault()
        sizer.Add(b)

        b = wx.Button(panel, -1, "non-default wx.Button")
        sizer.Add(b)

        b = buttons.GenButton(panel, -1, "Generic Button")
        sizer.Add(b)

        b = buttons.GenButton(panel, -1, "disabled Generic")
        b.Enable(False)
        sizer.Add(b)

        b = buttons.GenButton(panel, -1, "bigger")
        b.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.BOLD))
        b.SetBezelWidth(5)
        b.SetBackgroundColour("Navy")
        b.SetForegroundColour("white")
        b.SetToolTip("This is a BIG button!")
        sizer.Add(b)

        bmp = wx.Image("img/button-off.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()

        b = buttons.GenBitmapButton(panel, -1, bmp)
        sizer.Add(b)

        b = buttons.GenBitmapToggleButton(panel, -1, bmp)
        sizer.Add(b)

        b = buttons.GenBitmapTextButton(panel, -1, bmp, "Bitmap Text",
                                        size=(175, 75))
        b.SetUseFocusIndicator(False)
        sizer.Add(b)

        b = buttons.GenToggleButton(panel, -1, "Toggle Button")
        sizer.Add(b)

        panel.SetSizer(sizer)


if __name__ == "__main__":
    app = wx.App()
    frame = GenericButtonFrame()
    frame.Show()
    app.MainLoop()
