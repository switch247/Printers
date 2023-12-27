
# # import tkinter as tk
# # import win32print

# # def get_printers():
# #     printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)
# #     return [printer[2] for printer in printers]

# # def update_printer_list(printer_listbox):
# #     new_printers = get_printers()
# #     printer_listbox.delete(0, tk.END)  # Clear the current list
# #     for printer in new_printers:
# #         printer_listbox.insert(tk.END, printer)

# # def main():
# #     root = tk.Tk()
# #     root.title("Printer List")

# #     root.columnconfigure(0, weight=1)
# #     root.columnconfigure(1, weight=1)
# #     root.rowconfigure(0, weight=1)

# #     left_frame = tk.Frame(root)
# #     left_frame.grid(row=0, column=0, sticky="nsew")

# #     right_frame = tk.Frame(root)
# #     right_frame.grid(row=0, column=1, sticky="nsew")

# #     printer_label = tk.Label(right_frame, text="Available Printers:")
# #     printer_label.pack()

# #     printer_listbox = tk.Listbox(right_frame)
# #     printer_listbox.pack(fill="both", expand=True)

# #     def refresh_printer_list():
# #         update_printer_list(printer_listbox)

# #     refresh_button = tk.Button(left_frame, text="Refresh", command=refresh_printer_list)
# #     refresh_button.pack(pady=10)

# #     update_printer_list(printer_listbox)  # Initial update

# #     # Periodically update the printer list every 10 seconds
# #     root.after(10000, lambda: update_printer_list(printer_listbox))

# #     root.mainloop()

# # if __name__ == "__main__":
# #     main()

# import tkinter as tk
# import requests, json

# from server import get_intercepted_data

# def update_printer_list(printer_listbox):
#     new_printers = get_printers()
#     printer_listbox.delete(0, tk.END)  # Clear the current list
#     for printer in new_printers:
#         printer_listbox.insert(tk.END, printer)

# def get_printers():
#     # Replace this with your actual logic to fetch printers
#     return ["Printer 1", "Printer 2", "Printer 3"]

# def update_intercepted_data(intercepted_listbox):
#     intercepted_listbox.delete(0, tk.END)  # Clear the current list
#     for data in get_intercepted_data():
#         intercepted_listbox.insert(tk.END, json.dumps(data, indent=2))

# def main():
#     root = tk.Tk()
#     root.title("Printer List")

#     root.columnconfigure(0, weight=1)
#     root.columnconfigure(1, weight=1)
#     root.rowconfigure(0, weight=1)

#     left_frame = tk.Frame(root)
#     left_frame.grid(row=0, column=0, sticky="nsew")

#     right_frame = tk.Frame(root)
#     right_frame.grid(row=0, column=1, sticky="nsew")

#     intercepted_label = tk.Label(left_frame, text="Intercepted Data:")
#     intercepted_label.pack()

#     intercepted_listbox = tk.Listbox(left_frame)
#     intercepted_listbox.pack(fill="both", expand=True)

#     printer_label = tk.Label(right_frame, text="Available Printers:")
#     printer_label.pack()

#     printer_listbox = tk.Listbox(right_frame)
#     printer_listbox.pack(fill="both", expand=True)

#     def refresh_printer_list():
#         update_printer_list(printer_listbox)

#     def refresh_intercepted_data():
#         update_intercepted_data(intercepted_listbox)

#     refresh_button = tk.Button(left_frame, text="Refresh Intercepted Data", command=refresh_intercepted_data)
#     refresh_button.pack(pady=10)

#     update_printer_list(printer_listbox)  # Initial update

#     root.mainloop()

# if __name__ == "__main__":
#     main()


# import tkinter as tk
# import win32print

# def get_printers():
#     printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)
#     return [printer[2] for printer in printers]

# def update_printer_list(printer_dropdown):
#     new_printers = get_printers()
#     printer_dropdown['menu'].delete(0, 'end')  # Clear the current menu
#     for printer in new_printers:
#         printer_dropdown['menu'].add_command(label=printer, command=tk._setit(printer_dropdown, printer))

# def on_printer_select(*args):
#     selected_printer.set(printer_var.get())

# def main():
#     root = tk.Tk()
#     root.title("Printer List")

#     root.columnconfigure(0, weight=1)
#     root.columnconfigure(1, weight=1)
#     root.rowconfigure(0, weight=1)

#     left_frame = tk.Frame(root)
#     left_frame.grid(row=0, column=0, sticky="nsew")

#     right_frame = tk.Frame(root)
#     right_frame.grid(row=0, column=1, sticky="nsew")

#     printer_label = tk.Label(right_frame, text="Select Printer:")
#     printer_label.pack()

#     printer_var = tk.StringVar()
#     printer_dropdown = tk.OptionMenu(right_frame, printer_var, "")
#     printer_dropdown.pack()

#     selected_printer = tk.StringVar()
#     selected_printer_label = tk.Label(right_frame, textvariable=selected_printer)
#     selected_printer_label.pack()

#     update_printer_list(printer_dropdown)  # Initial update

#     printer_var.trace('w', on_printer_select)  # Call on_printer_select when the printer is selected

#     root.mainloop()

# if __name__ == "__main__":
#     main()



import win32print
import tkinter as tk
from tkinter import StringVar, OptionMenu
import ttkbootstrap as tb
import os
import sys

def main():
        
    def get_printers():
        printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)
        return [printer[2] for printer in printers]
    
    def update_printer_list(printer_combobox):
        new_printers = get_printers()
        printer_combobox['values'] = new_printers

    def restart():
        python = sys.executable
        os.execl(python, python, *sys.argv)
    def on_printer_select(*args):
        selected_printer.set(printer_var.get())
    
    def click_bind(e):
        selected_printer_label.config(text=printer_combobox.get())
    def click_bind_save():
        selected_printer_label.config(text=printer_combobox.get())

    def on_print_click():
        selected_printer = printer_var.get()
        if selected_printer:
            printer_handle = win32print.OpenPrinter(selected_printer)
            try:
                raw_data = b"hello"
                win32print.StartDocPrinter(printer_handle, 1, ("Hello", None, "RAW"))
                win32print.StartPagePrinter(printer_handle)
                win32print.WritePrinter(printer_handle, raw_data)
                win32print.EndPagePrinter(printer_handle)
                win32print.EndDocPrinter(printer_handle)
            finally:
                win32print.ClosePrinter(printer_handle)
    
    root = tb.Window()  # Initialize the root window with the 'superhero' theme
    root.geometry('550x300')
    root.title("Printer Agent v1.0.0")


    root.iconbitmap('./app/images/logo.ico')
    



    

    top_frame = tb.Frame(root)
    top_frame.pack(side=tk.TOP,fill="both", expand=True )
    # themename="pulse"

    title = tb.Label(top_frame, text="Retail Printer Agent", font=("Arial", 12,"bold") )
    title.pack(anchor="w",padx=5, pady=10)
    sub_title = tb.Label(top_frame, text="Lipton Sports and Casino")
    sub_title.pack(anchor="w",padx=5, pady=5)

    
    bottom_frame = tb.Frame(root)
    bottom_frame.pack(side=tk.BOTTOM, pady=5, fill="both", expand=True)

    printer_label = tk.Label(bottom_frame, text="Selected Printer:")
    printer_label.pack(anchor="w", padx=5, pady=1)

    printer_var = StringVar()
    printers =  get_printers()
    default_printer = printers[0]
    printer_var.set(default_printer)

    selected_printer = StringVar()
    selected_printer_label = tb.Label(bottom_frame,text = printer_var,  bootstyle="success")
    selected_printer_label.pack(anchor="w", padx=5)

    style = tb.Style()
    style.configure('Custom.TCombobox',  padding=(10, 10, 30, 10), font=('Arial', 12), anchor="n")

    printer_label_1 = tk.Label(bottom_frame, text="Change Printer:")
    printer_label_1.pack(anchor="w",pady=1, padx=5)
    printer_combobox = tb.Combobox( bottom_frame, values=printers , bootstyle="info", style='Custom.TCombobox', width='280')
    printer_combobox.bind("<<ComboboxSelected>>",click_bind)
    # printer_combobox = tb.OptionMenu(bottom_frame, printer_var, *printers)
    # printer_combobox.config(bootstyle="info")
    printer_combobox.pack(anchor="w", pady=3, padx=5)
    printer_combobox.current(0)

    click_bind_save()
    print_button = tb.Button(bottom_frame, text="Print", command=on_print_click, width='280')
    print_button.pack(anchor="w", padx=5)

    # refresh_button = tk.Button(root, text="Refresh App", command=restart)
    # refresh_button.pack()

    # update_printer_list(printer_combobox)
    printer_var.trace('w', on_printer_select)

    root.mainloop()

if __name__ == "__main__":
    main()
