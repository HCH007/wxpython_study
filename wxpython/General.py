import wx
import wx.grid
import Grid2

data = (("1,1", "1,2"), ("2,1", "2,2"), ("3,1", "3,2"))
colLabels = ("Col1", "Col2")
rowLabels = ("row1", "row2", "row3")

class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        tableBase = Grid2.GenericTable(data, rowLabels, colLabels)
        self.SetTable(tableBase, True)

class TestFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "A Grid",
                          size=(275, 275))
        grid = SimpleGrid(self)

if __name__ == "__main__":
    app = wx.App()
    frame = TestFrame(None)
    frame.Show(True)
    app.MainLoop()