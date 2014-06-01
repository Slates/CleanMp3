#!/usr/bin/env python
# buttons.py

import wx
import os

APP_SIZE_X = 400
APP_SIZE_Y = 300
   
class MyButtons(wx.Dialog):
	def __init__(self, parent, id, title):
		wx.Dialog.__init__(self, parent, id, title, size=(APP_SIZE_X, APP_SIZE_Y))

		wx.Button(self,1, label = 'Print Mp3s', pos = (150,130), size = (100,50))
		wx.Button(self,2, 'Random Move', pos = (0, 0), size = (1, 1))

		self.field = wx.TextCtrl(self,1,value="",pos = (100,80), size=(200,20))

		self.Bind(wx.EVT_BUTTON, self.OnPrintMp3s, id=1)
		self.Bind(wx.EVT_TEXT_ENTER, self.OnPrintMp3s)

		self.Centre()
		self.ShowModal()
		self.Destroy()

	def OnPrintMp3s(self, event):
		filedir = self.field.GetValue()
		os.system("python cleanmp3.py " + filedir)

app = wx.App(0)
MyButtons(None, -1, 'Clean Mp3')
app.MainLoop()
