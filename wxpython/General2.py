import wx
import wx.grid

class LineupEntry:

    def __init__(self, pos, first, last):
        self.pos = pos
        self.col1 = first
        self.col2 = last


class LineupTable(wx.grid.GridTableBase):

    colLabels = ("Col1", "Col2")
    colAttrs = ("col1", "col2")

    def __init__(self, entries):
        wx.grid.GridTableBase.__init__(self)
        self.entries = entries

    def GetNumberRows(self):
        return len(self.entries)

    def GetNumberCols(self):
        return 2

    def GetColLabelValue(self, col):
        return self.colLabels[col]

    def GetRowLabelValue(self, row):
        return self.entries[row].pos

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        entry = self.entries[row]
        return getattr(entry, self.colAttrs[col])

    def SetValue(self, row, col, value):
        pass

class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent, entries):
        wx.grid.Grid.__init__(self, parent, -1)
        tableBase = LineupTable(entries)
        self.SetTable(tableBase, True)

class TestFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "A Grid",
                          size=(275, 275))
        entries = [LineupEntry("Row1", "1", "1"), LineupEntry("Row2", "2", "2"), LineupEntry("Row3", "3", "3")]
        grid = SimpleGrid(self, entries)

if __name__ == "__main__":
    app = wx.App()
    frame = TestFrame(None)
    frame.Show(True)
    app.MainLoop()