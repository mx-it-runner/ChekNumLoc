from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
import pandas as pd
import openpyxl #Негде не используется, НО без него не читает xlsx and csv файлы :)))))




def open_file_xlsx():
    filename = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])

    non_number = 0
    complit_number = 0
    empty_string = 0
    mapped_data = []
    print(mapped_data)
    error_data = []
    
    if filename:
        df = pd.read_excel(filename, header=None)
        def_data = pd.read_excel('Data.xlsx')
        numbers = df.iloc[0:, 0].tolist()
        #numbers_listbox.delete(0, tk.END)
        numbers_listbox.config(text="")
        mapped_data.clear()
        error_data.clear()
             

        for number in numbers:
            #numbers_listbox.insert(tk.END, mapped_data)
            numbers_listbox.config(text=mapped_data) 
            str_num = str(number)
            if str_num != "" and str_num != "nan":
                digits = "".join(filter(str.isdigit, str_num))
                if (len(digits)) == 11:
                    kod_operatora = digits[1:4]
                    nomer =  digits[4:11]
                    match = def_data[(def_data['АВС/ DEF'] == int(kod_operatora)) & (def_data['От'] <= int(nomer)) & (def_data['До'] >= int(nomer))]
                    
                    if not match.empty:
                        operator = match['Оператор'].iloc[0]
                        region = match['Регион'].iloc[0]
                        complit_number += 1
                        mapped_data.append([str_num, operator, region])
            
                    else:
                        non_number += 1
                        error_data.append([str_num])
                elif (len(digits)) == 10:
                    
                    digits = "7" + digits
                        
                    kod_operatora = digits[1:4]
                    nomer =  digits[4:11]
                        
                    match = def_data[(def_data['АВС/ DEF'] == int(kod_operatora)) & (def_data['От'] <= int(nomer)) & (def_data['До'] >= int(nomer))]
                        
                    if not match.empty:
                        operator = match['Оператор'].iloc[0]
                        region = match['Регион'].iloc[0]
                        complit_number += 1
                            
                        mapped_data.append([str_num, operator, region])
                
                else:
                    non_number += 1
                    error_data.append([str_num])
            else:
                empty_string += 1

def open_file_csv():
    filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    
    
root = tk.Tk()
root.geometry("400x250+400+200")
root.title("ChekNum")
icon = PhotoImage(file = "icon.png")
root.iconphoto(False, icon)

button = tk.Button(root, text="Загрузить файл .xlsx", command=open_file_xlsx)
button.pack()

button = tk.Button(root, text="Загрузить файл .csv", command=open_file_csv)
button.pack()


    
numbers_listbox = ttk.Label(root, wraplength=450)
numbers_listbox.pack()
 
root.mainloop()