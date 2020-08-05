import wx
from wx import *
app = App()
main  = Frame(None,1,title="Untitled - Notepad",size=(900,600))
p = Panel(main)

mb = MenuBar()

fileMenu = Menu()
new = MenuItem(fileMenu,1,text="New\tCtrl+N")
fileMenu.Append(new)

save = MenuItem(fileMenu,1,text="Save\tCtrl+S")
fileMenu.Append(save)


prints = MenuItem(fileMenu,1,text="Print\tCtrl+P")
fileMenu.Append(prints)

mb.Append(fileMenu,"&File")

edit = Menu()

copy = MenuItem(edit,1,text="Copy\tCtrl+C")
edit.Append(copy)

mb.Append(edit,"&Edit")

box = BoxSizer(VERTICAL)

text = TextCtrl(p,1,style=TE_MULTILINE)
box.Add(text,1,ALL|EXPAND)

p.SetSizer(box)
main.SetMenuBar(mb)
main.Show()
app.MainLoop()
