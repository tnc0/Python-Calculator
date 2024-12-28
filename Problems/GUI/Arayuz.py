 
from tkinter import *
 
from tkinter import messagebox
 
pencere = Tk()
 
pencere.title("Yusufd:")
pencere.geometry("400x300")
 
#grid form çizdirme
uygulama = Frame(pencere)
uygulama.grid()
 
 
chek1=Checkbutton(uygulama, text = "Erkek", onvalue = 1, offvalue = 0, height=5, width = 20)
chek1.grid(padx=110, pady=10)
 
chek2=Checkbutton(uygulama, text = "Kadın", onvalue = 1, offvalue = 0, height=5, width = 20)
chek2.grid(padx=110, pady=5)
 
#formu çiz
pencere.mainloop()
 