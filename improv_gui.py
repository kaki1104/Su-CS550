import wx
from improv import *
import pysynth as ps


class MyFrame(wx.Frame):

   def __init__(self):

      super().__init__(None, wx.ID_ANY, 'Jazz Improv Generator', size=(800, 600))

      self.CreateStatusBar()
      self.GetStatusBar().SetBackgroundColour(None)

      # creating class elements in the root panel
      root_panel = wx.Panel(self, wx.ID_ANY)
      cmdbutton_panel = CommandButtonPanel(root_panel)
      calcbutton_panel = ButtonPanel(root_panel)
      button_quit = wx.Button(root_panel, wx.ID_ANY, 'QUIT')
      button_quit.Bind(wx.EVT_BUTTON, self.OnClose)

      #laying out class elements using boxsizer
      root_layout = wx.BoxSizer(wx.VERTICAL)
      root_layout.Add(calcbutton_panel, 0, wx.GROW | wx.LEFT | wx.RIGHT, border=20)
      root_layout.Add(cmdbutton_panel, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=40)
      root_layout.AddStretchSpacer()
      root_layout.Add(button_quit, 0, wx.ALIGN_RIGHT| wx.ALL, border=40)
      root_panel.SetSizer(root_layout)
      root_layout.Fit(root_panel)

      #opens up the window in the center of the screen
      self.Centre()

   def OnClose (self, e) :

      self.Close(True)


class CommandButtonPanel(wx.Panel):
   #the buttons for command events
   def __init__(self, parent):

      super().__init__(parent, wx.ID_ANY)

      button_return = wx.Button(self, wx.ID_ANY, 'RETURN')
      button_play = wx.Button(self, wx.ID_ANY, 'PLAY')
      button_play.Bind (wx.EVT_BUTTON, audio_play)
      button_reset  = wx.Button(self, wx.ID_ANY, 'RESET')
      layout = wx.BoxSizer(wx.HORIZONTAL)
      layout.Add(button_return, wx.ALIGN_CENTER_HORIZONTAL)
      layout.Add(button_play, wx.ALIGN_CENTER_HORIZONTAL)
      layout.Add(button_reset, wx.ALIGN_CENTER_HORIZONTAL)
      self.SetSizer(layout)

   def audio_play (self, e):
      self.improv.playaudio ()


class ButtonPanel(wx.Panel):
#The class for button panels

   def __init__(self, parent):

      super().__init__(parent, wx.ID_ANY)

      button_collection = ('C', 'C#', 'D', 'D#',
         'E', 'F', 'F#', 'G',
         'G#', 'A', 'A#', 'B')

      layout = wx.GridSizer(3, 4, 5, 5)

      for i in button_collection:
         layout.Add(wx.Button(self, wx.ID_ANY, i, size=(30,55)), 1, wx.GROW)

         self.SetSizer(layout)


if __name__ == '__main__':

   application = wx.App()
   frame = MyFrame()
   frame.Show()
   application.MainLoop()