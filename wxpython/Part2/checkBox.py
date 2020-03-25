import wx


class CheckBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Checkbox Example", size=(150, 200))
        panel = wx.Panel(self, -1)
        wx.CheckBox(panel, -1, "α", (35, 40), (150, 20))
        wx.CheckBox(panel, -1, "β", (35, 60), (150, 20))
        wx.CheckBox(panel, -1, "γ", (35, 80), (150, 20))


class RadioButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Radio Example", size=(200, 200))
        panel = wx.Panel(self, -1)
        radio1 = wx.RadioButton(panel, -1, "George", pos=(20, 50), style=wx.RB_GROUP)
        radio2 = wx.RadioButton(panel, -1, "William", pos=(20, 80))
        radio3 = wx.RadioButton(panel, -1, "Peter", pos=(20, 110))

        text1 = wx.TextCtrl(panel, -1, "", pos=(90, 50))
        text2 = wx.TextCtrl(panel, -1, "", pos=(90, 80))
        text3 = wx.TextCtrl(panel, -1, "", pos=(90, 110))
        self.texts = {"George": text1, "William": text2,
                      "Peter": text3}
        for each_text in [text2, text3]:
            each_text.Enable(False)
        for each_radio in [radio1, radio2, radio3]:
            self.Bind(wx.EVT_RADIOBUTTON, self.on_radio, each_radio)
        self.selctedText = text1

    def on_radio(self, event):
        if self.selctedText:
            self.selctedText.Enable(False)
        radio_selected = event.GetEventObject()
        text = self.texts[radio_selected.GetLabel()]
        text.Enable(True)
        self.selctedText = text


class RadioBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "RadioBox Example", size=(350, 200))
        panel = wx.Panel(self, -1)
        samplelist = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
        wx.RadioBox(panel, -1, "A Radio Box", (10, 10), wx.DefaultSize, samplelist, 2, wx.RA_SPECIFY_COLS)
        wx.RadioBox(panel, -1, "", (150, 10), wx.DefaultSize, samplelist, 3, wx.RA_SPECIFY_COLS)


class ListBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "RadioBox Example", size=(250, 200))
        panel = wx.Panel(self, -1)
        samplelist = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight', 'nine', 'ten',
                      'eleven', 'twelve', 'thirteen', 'fourteen']
        listbox = wx.ListBox(panel, -1, (20, 20), (80, 120), samplelist, wx.LB_SINGLE)
        listbox.SetSelection(3)


if __name__ == "__main__":
    app = wx.App()
    frame = ListBoxFrame()
    frame.Show()
    app.MainLoop()
