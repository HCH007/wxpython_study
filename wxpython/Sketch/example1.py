import wx

class SketchWindow(wx.Window):
    def __init__(self, parent, ID):
        wx.Window.__init__(self, parent, ID)
        self.SetBackgroundColour("White")
        self.color = "Black"
        self.thickness = 3
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)
        self.lines = []
        self.curLine = []
        self.pos = (0, 0)
        self.InitBuffer()
        self.reInitBuffer = True


        #-----------------
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMotion)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def InitBuffer(self):
        size = self.GetClientSize()

        #创建设备上下文
        self.buffer = wx.Bitmap(size.width, size.height)
        dc = wx.BufferedDC(None, self.buffer)

        #使用设备上下文
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        #print("66666")
        self.Refresh()
        self.DrawLines(dc)
        self.reInitBuffer = False

    def GetLinesData(self):
        return self.lines[:]

    def SetLinesData(self, lines):
        self.lines = lines[:]
        self.InitBuffer()
        self.Refresh()

    def OnLeftDown(self, event):
        self.curLine = []
        self.pos = event.GetPosition()
        #print(self.pos)
        #print(self.reInitBuffer)
        self.CaptureMouse()

    def OnLeftUp(self, event):
        #print(self.curLine)
        #print(self.reInitBuffer)
        if self.HasCapture():
            self.lines.append((self.color, self.thickness, self.curLine))
            self.curLine = []
            self.ReleaseMouse()

    def OnMotion(self, event):
        if event.Dragging() and event.LeftIsDown():
            #创建缓存上下文
            dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
            self.drawMotion(dc, event)
        event.Skip()

    #绘制到设备上下文
    def drawMotion(self, dc, event):
        dc.SetPen(self.pen)
        newPos = event.GetPosition()
        coords = (self.pos, newPos)
        self.curLine.append(coords)
        #print(self.curLine)
        dc.DrawLine(*coords)
        #print("draw")
        self.pos = newPos
        #print(self.reInitBuffer)

    def OnSize(self, event):
        self.reInitBuffer = True
        #print(self.reInitBuffer)


    def OnIdle(self, event):
        #print(self.reInitBuffer)
        if self.reInitBuffer:
            self.InitBuffer()
            self.Refresh(False)
            #print("Refresh")

    def OnPaint(self, event):
        dc = wx.BufferedPaintDC(self, self.buffer)

    #绘制所有线条
    def DrawLines(self, dc):
        for colour, thickness, line in self.lines:
            pen = wx.Pen(colour, thickness, wx.SOLID)
            dc.SetPen(pen)
            for coords in line:
                dc.DrawLine(*coords)
    def GetColor(self):
        tmp = self.pen.GetColour()
        tmp = tmp.Get()
        return tmp

    def SetColor(self, color):
        self.color = color
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)

    def SetThickness(self, num):
        self.thickness = num
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)

class SketchFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Sketch Frame", size=(800, 600))
        self.sketch = SketchWindow(self, -1)

if __name__ == "__main__":
    app = wx.App()
    frame = SketchFrame(None)
    frame.Show(True)
    app.MainLoop()