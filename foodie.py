import wx
from wx import *


app  = App()
main = Frame(None,title="foodie",size=(700,350))
p = Panel(main)

#main Box with 1) header 2) body
mainbox = BoxSizer(VERTICAL)

#first box of main box
header = StaticText(p,1,label="FOODIE",style=ALIGN_CENTER)
font = Font(20,FONTFAMILY_DECORATIVE,FONTSTYLE_NORMAL,FONTWEIGHT_BOLD)

header.SetBackgroundColour("red")
header.SetForegroundColour("white")
header.SetFont(font)
mainbox.Add(header,1,EXPAND)

#second box of mainbox
body = BoxSizer(HORIZONTAL)

#body box has two part 1) for recipie and 2) for amount details and button
recipe = GridSizer(6,2,5,5) #(x,y,xgap,ygap)

#recipe labels
samosa_label = StaticText(p,-1,label="samosa")
kachori_label = StaticText(p,-1,label="Kachori")
dosa_label = StaticText(p,-1,label="Dosa")
roll_label = StaticText(p,-1,label="Egg Role")
pizza_label = StaticText(p,-1,label="Pizza")
chowmin_label = StaticText(p,-1,label="Chowmin")

#recipe textCtrls
samosa = TextCtrl(p,-1)
kachori = TextCtrl(p,-1)
dosa = TextCtrl(p,-1)
roll = TextCtrl(p,-1)
pizza = TextCtrl(p,-1)
chowmin = TextCtrl(p,-1)




def setDefault():
    samosa.SetValue('0')
    kachori.SetValue('0')
    dosa.SetValue('0')
    roll.SetValue('0')
    chowmin.SetValue('0')
    pizza.SetValue('0')


setDefault()

def Order(event):
    samosa_value = int(samosa.GetValue()) * 7
    dosa_value = int(dosa.GetValue()) * 70
    roll_value = int(roll.GetValue()) * 15
    chowmin_value = int(chowmin.GetValue()) * 25
    pizza_value = int(pizza.GetValue()) * 99
    kachori_value = int(kachori.GetValue()) * 10

    total = samosa_value + dosa_value + roll_value + pizza_value + kachori_value + chowmin_value
    tax = round(total*0.18)
    payable = round(total + tax)

    total_amount.SetValue(str(total))
    
    total_tax.SetValue(str(tax))
    
    total_payable.SetValue(str(payable))
    

samosa.Bind(EVT_TEXT,Order)
roll.Bind(EVT_TEXT,Order)
kachori.Bind(EVT_TEXT,Order)
dosa.Bind(EVT_TEXT,Order)
pizza.Bind(EVT_TEXT,Order)
chowmin.Bind(EVT_TEXT,Order)

#now adding on recipe grid Sizer
recipe.Add(samosa_label,0,ALL|EXPAND)
recipe.Add(kachori_label,0,ALL|EXPAND)

recipe.Add(samosa,1,ALL|EXPAND)
recipe.Add(kachori,1,ALL|EXPAND)

recipe.Add(dosa_label,0,ALL|EXPAND)
recipe.Add(chowmin_label,0,ALL|EXPAND)

recipe.Add(dosa,1,ALL|EXPAND)
recipe.Add(chowmin,1,ALL|EXPAND)

recipe.Add(pizza_label,0,ALL|EXPAND)
recipe.Add(roll_label,0,ALL|EXPAND)

recipe.Add(pizza,1,ALL|EXPAND)
recipe.Add(roll,1,ALL|EXPAND)


#details box
details = GridSizer(6,1,5,5)

total_amount_label = StaticText(p,-1,label="Total Amount")
total_tax_label = StaticText(p,-1,label="Total Tax")
total_payable_label = StaticText(p,-1,label="Total Payable")


total_amount = TextCtrl(p,-1)
total_tax = TextCtrl(p,-1)
total_payable = TextCtrl(p,-1)

details.Add(total_amount_label,1,ALL|EXPAND)
details.Add(total_amount,1,ALL|EXPAND)
details.Add(total_tax_label,1,ALL|EXPAND)
details.Add(total_tax,1,ALL|EXPAND)
details.Add(total_payable_label,1,ALL|EXPAND)
details.Add(total_payable,1,ALL|EXPAND)

#recipe and details adding on body section
body.Add(recipe,4,ALL|EXPAND,border=10)
body.Add(details,1,ALL|EXPAND,border=10)

#now body adding on main box
mainbox.Add(body,5,ALL|EXPAND,border=10)

p.SetBackgroundColour('#00aeff')
p.SetSizer(mainbox)
main.Show()
app.MainLoop()
