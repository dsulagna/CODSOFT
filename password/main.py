from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import string, random
root=Tk()
root.geometry("500x350")
root.resizable(False, False)
def password_gen():
    try:
      pass_length=solid.get()
      small=string.ascii_lowercase
      capital=string.ascii_uppercase
      digits=string.digits
      special=string.punctuation
      all_list=[]
      all_list.extend(list(small))
      all_list.extend(list(capital))
      all_list.extend(list(digits))
      all_list.extend(list(special))
      random.shuffle(all_list)
      password.set("".join(all_list[0:pass_length]))
    except:
       messagebox.askretrycancel("A problem has occured","Please try again")
       

numbers={"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"10","11":"11","12":"12","13":"13","14":"14","15":"15","16":"16","17":"17","18":"18","19":"19","20":"20"}
root.title("Password Generator")
Title=Label(root, text="Password Generator",fg="black", font=("futura", 20, "bold"))
Title.pack(anchor="center", pady="30px")
length=Label(root, text="Select the length of your Password:", fg="blue",font=("ubuntu", 12, "bold"))
length.place(x="20px",y="80px")
solid=IntVar()
Selector=Combobox(root,textvariable=solid, state="readonly")
Selector['values']=[l for l in numbers.keys()]
Selector.current(7)
Selector.place(x="230px",y="80px")
gen=Button(root,text="Generate Password",bg="turquoise", fg="black",font=("ubuntu", 12),cursor="hand2",command= password_gen)
gen.pack(anchor="center",pady="40px")
result=Label(root, text="Generated Password Here:", fg="blue",font=("ubuntu", 12, "bold"))
result.place(x="20px",y="180px")
password = StringVar()
passwordf=Entry(root, textvariable=password, state="readonly", fg="black",font=("ubuntu", 15) )
passwordf.place(x="180px",y="180px")











root.mainloop()
