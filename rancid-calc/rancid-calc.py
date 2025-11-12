import gi
import its
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Pango
Textor = ""
TextorDisplay = "Welcome"



def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)

    buttonsize = 2
    generalBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    labelBox = Gtk.Box()
    labelBox.set_margin_bottom(10)
    theLabel = Gtk.Label()
    theLabel.set_markup(f"<span font_size='24000'>{TextorDisplay}</span>")
    labelBox.append(theLabel)

    def results():
        global Textor
        global TextorDisplay
        Textor = its.magic(Textor)
        TextorDisplay = Textor
        theLabel.set_markup(f"<span font_size='24000'>{TextorDisplay}</span>")

    def onTextChange(value):
        global Textor
        global TextorDisplay

        if TextorDisplay == "Cleared" or TextorDisplay == "Welcome":
            TextorDisplay = ""


        if value == "":
            Textor = ""
            TextorDisplay = "Cleared"
            theLabel.set_markup(f"<span font_size='24000'>{TextorDisplay}</span>")

        elif value in '+-/*)(-':
            if value in "/":
                Textor = Textor +" "+ value +" "
                TextorDisplay = TextorDisplay +" "+ '÷' +" "
                theLabel.set_markup(f"<span font_size='24000'>{TextorDisplay}</span>")
            elif value in "*":
                Textor = Textor +" "+ value +" "
                TextorDisplay = TextorDisplay +" "+ 'X' +" "
                theLabel.set_markup(f"<span font_size='24000'>{TextorDisplay}</span>")
            elif value in ")(":
                Textor = Textor + value
                TextorDisplay = TextorDisplay + value
                theLabel.set_markup(f"<span font_size='24000'>{TextorDisplay}</span>")
            else:
                Textor = Textor +" "+ value +" " 
                TextorDisplay = TextorDisplay +" "+ value +" "
                theLabel.set_markup(f"<span font_size='24000'>{TextorDisplay}</span>")
        else:
            Textor = Textor + value
            TextorDisplay = TextorDisplay + value
            print(f"post val {Textor}")
            print(f"post val display {TextorDisplay}")
            theLabel.set_markup(f"<span font_size='24000'>{TextorDisplay}</span>")


    btn1 = Gtk.Button(label="1")
    btn2 = Gtk.Button(label="2")
    btn3 = Gtk.Button(label="3")
    btn4 = Gtk.Button(label="4")
    btn5 = Gtk.Button(label="5")
    btn6 = Gtk.Button(label="6")
    btn7 = Gtk.Button(label="7")
    btn8 = Gtk.Button(label="8")
    btn9 = Gtk.Button(label="9")
    btn0 = Gtk.Button(label="0")
    btnAC = Gtk.Button(label="AC")
    btnEQ = Gtk.Button(label="=")
    btnPlus = Gtk.Button(label="+")
    btnMinus = Gtk.Button(label="-")
    btnDiv = Gtk.Button(label="÷")
    btnMult = Gtk.Button(label="X")
    btnBracLeft = Gtk.Button(label="(")
    btnBracRight = Gtk.Button(label=")")
    
    btnAC.connect("clicked", lambda X : onTextChange(""))
    btn1.connect("clicked", lambda X : onTextChange("1"))
    btn2.connect("clicked", lambda X : onTextChange("2"))
    btn3.connect("clicked", lambda X : onTextChange("3"))
    btn4.connect("clicked", lambda X : onTextChange("4"))
    btn5.connect("clicked", lambda X : onTextChange("5"))
    btn6.connect("clicked", lambda X : onTextChange("6"))
    btn7.connect("clicked", lambda X : onTextChange("7"))
    btn8.connect("clicked", lambda X : onTextChange("8"))
    btn9.connect("clicked", lambda X : onTextChange("9"))
    btn0.connect("clicked", lambda X : onTextChange("0"))
    btnPlus.connect("clicked", lambda X : onTextChange("+"))
    btnMinus.connect("clicked", lambda X : onTextChange("-"))
    btnDiv.connect("clicked", lambda X : onTextChange("/"))
    btnMult.connect("clicked", lambda X : onTextChange("*"))
    btnBracLeft.connect("clicked", lambda X : onTextChange("("))
    btnBracRight.connect("clicked", lambda X : onTextChange(")"))
    btnEQ.connect("clicked", lambda X : results())


    grid = Gtk.Grid()

#    grid.attach(labelBox, 0, 0, 4, 1)
    grid.attach(btn1, 0, 1, 1, 1)
    grid.attach(btn2, 1, 1, 1, 1)
    grid.attach(btn3, 2, 1, 1, 1)
    grid.attach(btn4, 0, 2, 1, 1)
    grid.attach(btn5, 1, 2, 1, 1)
    grid.attach(btn6, 2, 2, 1, 1)
    grid.attach(btn7, 0, 3, 1, 1)
    grid.attach(btn8, 1, 3, 1, 1)
    grid.attach(btn9, 2, 3, 1, 1)
    grid.attach(btn0, 1, 4, 1, 1)
    grid.attach(btnAC, 0, 4, 1, 1)
    grid.attach(btnEQ, 2, 4, 1, 1)
    grid.attach(btnPlus, 4, 1, 1, 1)
    grid.attach(btnMinus, 4, 2, 1, 1)
    grid.attach(btnDiv, 4, 3, 1, 1)
    grid.attach(btnMult, 4, 4, 1, 1)
    grid.attach(btnBracLeft, 0, 6, 1, 1)
    grid.attach(btnBracRight, 2, 6, 1, 1)


    generalBox.append(labelBox)
    generalBox.append(grid)


    win.set_child(generalBox)
    win.present()





app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run(None)
