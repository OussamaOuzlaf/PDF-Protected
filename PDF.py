from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PyPDF2 import PdfWriter, PdfReader  # Updated to use PdfWriter and PdfReader
import os

root = Tk()
root.title("PDF Protector")
root.resizable(False, False)
root.geometry("600x430+300+100")
font = ("Tajwal", 20, "bold")

def browser():
    global fileName
    fileName = filedialog.askopenfile(mode='r', filetypes=[('PDF Files', '*.pdf')])
    if fileName:
        filePath = os.path.abspath(fileName.name)
        entry1.insert(0, str(filePath))

def Protecte():
    mainFile = source.get()
    protectFile = target.get()
    code = password.get()

    if not mainFile:
        messagebox.showinfo("Invalid", "Please Type Source PDF Filename")
    elif not protectFile:
        messagebox.showinfo("Invalid", "Please Type Target PDF Filename")
    elif not code:
        messagebox.showinfo("Invalid", "Please Type Password")
    else:
        try:
            out = PdfWriter()  # Use PdfWriter
            file = PdfReader(open(mainFile, "rb"))  # Use PdfReader
            num = len(file.pages)  # Use len(file.pages)

            for idx in range(num):
                page = file.pages[idx]  # Access pages using the updated method
                out.add_page(page)  # Use add_page instead of addPage

            out.encrypt(code)
            with open(protectFile, "wb") as f:
                out.write(f)

            messagebox.showinfo("Success", "PDF has been protected successfully!")
        except Exception as e:
            print("Error", f"An error occurred: {str(e)}")

F1 = Frame(root, width=600, height=80, bg="#f9765a")
F1.place(x=0, y=0)
Label(F1, bg="#f9765a", text="PDF Password Protector", font=font, fg="black").place(x=130, y=20)

F2 = Frame(root, width=580, height=330, relief=GROOVE, bd=5)
F2.place(x=10, y=90)

source = StringVar()
Label(F2, text="Source PDF File: ").place(x=30, y=50)
entry1 = Entry(F2, width=60, textvariable=source)
entry1.place(x=140, y=50)
Bopen = Button(F2, text="Open", cursor="hand2", command=browser)
Bopen.place(x=520, y=45)

target = StringVar()
Label(F2, text="Target PDF File: ").place(x=30, y=100)
entry2 = Entry(F2, width=60, textvariable=target)
entry2.place(x=140, y=100)

password = StringVar()
Label(F2, text="Set User Password: ").place(x=30, y=150)
entry3 = Entry(F2, width=60, textvariable=password)
entry3.place(x=140, y=150)

Btn = Button(F2, width=40, height=2, bg="#dbd8d5", text="Protect PDF File",
             cursor="hand2", font=("Tajwal", 13, "bold"), command=Protecte)
Btn.place(x=80, y=200)

root.mainloop()
