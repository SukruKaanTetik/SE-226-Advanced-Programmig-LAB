import mysql.connector
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='password',
                                     database='MarvelFilms')

cursor = connection.cursor(buffered=True)

def add_info_database():
    popup = tk.Toplevel(root)
    entry_popup = tk.Entry(popup, width=100)
    entry_popup.pack()

def update_text(event):
    id_selected = combo.get()
    cursor.execute("SELECT * FROM marvelmovies WHERE ID=%s", (id_selected,))
    result = cursor.fetchone()
    text_box.delete('1.0', tk.END)  # clear the textbox
    text_box.insert(tk.END, f"MOVIE: {result[1]} DATE: {result[2]} MCU_PHASE: {result[3]}")


    def ok():
        data = entry_popup.get().split(' ')
        if len(data) != 4:
            tk.messagebox.showerror("Plesase enter correct input")
            return
        id = data[0]
        movie = data[1]
        date = datetime.strptime(data[2], "%B%d,%Y").strftime("%Y-%m-%d")
        phase = data[3]
        sql = "INSERT INTO marvelmovies(ID, MOVIE, DATE, MCU_PHASE) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (id, movie, date, phase))
        connection.commit()
        cursor.execute("SELECT ID FROM marvelmovies")
        rows = cursor.fetchall()
        ids = [row[0] for row in rows]
        combo['values'] = ids
        popup.destroy()

    def cancel():
        popup.destroy()

    ok_button = tk.Button(popup, text="Ok", command=ok)
    ok_button.pack()
    cancel_button = tk.Button(popup, text="Cancel", command=cancel)
    cancel_button.pack()

def list_all():
    cursor.execute("SELECT * FROM marvelmovies")
    result = cursor.fetchall()
    text_box.delete('1.0', tk.END)  #for clearing the textbox
    for row in result:
        text_box.insert(tk.END, str(row) + "\n")

root = tk.Tk()

text_box = tk.Text(root, width=100)  
text_box.pack()

button1 = tk.Button(root, text="Add", command=add_info_database)
button1.pack()

button_list_all = tk.Button(root, text="LIST ALL", command=list_all)
button_list_all.pack()

cursor.execute("SELECT ID FROM marvelmovies ")
rows = cursor.fetchall()
ids = [row[0] for row in rows]

combo = ttk.Combobox(root, values=ids)
combo.bind("<<ComboboxSelected>>", update_text)
combo.pack()

root.mainloop()

cursor.close()
connection.close()
