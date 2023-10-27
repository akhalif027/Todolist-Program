# Custom tkinter(CTK) is a modern graphical user interface (GUI) framework. 
# CTKListBox is an add-on widget for CTK that provides listbox methods not avaliable in CTK. 
import customtkinter
from CTkListbox import * 

#Setting the backround color and theme. 
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

#Setting the size & title of the GUI app
window = customtkinter.CTk()
window.geometry('500x500')
window.title('Todolist App')

#Creating a frame to organize the GUI structure. 
frame = customtkinter.CTkFrame(window)
frame.pack(pady=20, padx =20, fill='both', expand=True)

#Setting program name
label = customtkinter.CTkLabel(frame, text='Todolist', font = ('ComicSans', 24))
label.pack(pady=10, padx=10)

#Placing a scrollable list that can append items onto it. 
list_box = CTkListbox(frame, font=('ComicSans', 24))
list_box.pack(pady=10, padx=10, fill='both', expand='True')

items = ['Wake up', 'Brush teeth', 'Get hired']

for item in items:
    list_box.insert('END',item)

#Creating a text box to add items into the scrollable list. 
entry = customtkinter.CTkEntry(frame, font= ('ComicSans', 24), width=470)
entry.pack(pady=10, padx=10)

#Defining functions that provide the insertion and deletion of items in the scrollable list. 
def add_item():
    item = entry.get()
    list_box.insert('END',item)
    entry.delete(0, 470)

def delete_item():
    selected_item = list_box.curselection()
    list_box.delete(selected_item)

#Creating buttons with their specific commands. 
add_button = customtkinter.CTkButton(frame, text='Add', command= add_item)
add_button.pack()

delete_button = customtkinter.CTkButton(frame, text='Delete', command =delete_item)
delete_button.pack()

exit_button = customtkinter.CTkButton(frame, text='Exit', command= window.destroy)
exit_button.pack()

#Initializing the GUI app. 
window.mainloop()