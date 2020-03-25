import wx


class SliderFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Slider Example", size=(300, 350))
        panel = wx.Panel(self, -1)
        self.count = 0
        slider = wx.Slider(panel, 100, 25, 1, 100, pos=(10, 10),
                           size=(250, -1), style=wx.SL_HORIZONTAL | wx.SL_LABELS)
        # slider.SetTickFreq(200)
        slider = wx.Slider(panel, 100, 25, 1, 100, pos=(125, 70),
                           size=(250, -1), style=wx.SL_VERTICAL | wx.SL_LABELS)
        # slider.SetTickFreq(20)


class SpinnerFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Spinnner Example", size=(100, 100))
        panel = wx.Panel(self, -1)
        sc = wx.SpinCtrl(panel, -1, "Nice", (10, 20), (50, 30))
        sc.SetRange(1, 100)
        # sc.SetValue(5)


class GaugeFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Gauge Example", size=(350, 150))
        panel = wx.Panel(self, -1)
        self.count = 0
        self.gauge = wx.Gauge(panel, -1, 50, (20, 50), (250, 25))
        self.Bind(wx.EVT_IDLE, self.on_idle)

    def on_idle(self, event):
        self.count += 1
        if self.count >= 50:
            self.count = 0
        self.gauge.SetValue(self.count)


if __name__ == "__main__":
    app = wx.App()
    frame = GaugeFrame()
    frame.Show()
    app.MainLoop()
