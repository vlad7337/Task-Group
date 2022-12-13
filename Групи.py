from tkinter import *
import csv, os
from tkinter import ttk, messagebox
from tkinter import filedialog as fd

filename = None
action = True

def create_window():
       win = Tk()
       win.geometry("600x400")
       win['bg'] = "#737373"
       win.attributes('-alpha', 0.85)
       win.grid_columnconfigure(0, minsize=250)
       win.grid_columnconfigure(1, minsize=350)
       return win

def registration_window():
       global win
       def write_account():
              data.write(input_login.get())
              data.write(' ')
              data.write(input_pass.get())
              data.write(' ')
              data.write('\n')
              auth()
       data = open('D:/Doc_groups/Accounts.txt', 'a')
       win = create_window()
       win.resizable(width=False, height= False)
       label_registr = Label(win, text = "Регістрація", bg = "#737373", font=("Arial", 20), height= 3,anchor="n")
       label_registr.grid(row = 0, column=0, columnspan=2, sticky="we")
       label_login = Label(win, text = "Login", bg = "#737373", font=("Arial", 14))
       label_login.grid(row=1, column=0,sticky="e")
       label_pass = Label(win, text="Password", bg="#737373", font=("Arial", 14), height= 3)
       label_pass.grid(row=2, column=0, sticky="e")
       input_login = Entry(win)
       input_login.grid(row = 1, column = 1, sticky = "w")
       input_pass = Entry(win)
       input_pass.grid(row = 2, column = 1, sticky = "w")
       Button(win, text = "registr", padx=20, command=write_account).grid(row = 3, column=0, columnspan= 2)

def authorization_window():
       global win
       def check():
              act = True
              for i in range(len(data_accounts)):
                     if input_login.get() == data_accounts[i][0] and input_pass.get() == data_accounts[i][1]:
                            admin()
                     else:
                            act = False
              if not act:
                     messagebox.showerror(title='Error', message='Login or password are wrong')
       win = create_window()
       data = open('D:/Doc_groups/Accounts.txt', 'r').readlines()
       data_accounts = []
       for i in range(len(data)):
              data_accounts.append(data[i].split(' '))
       win.resizable(width=False, height=False)
       label_registr = Label(win, text="Авторизація", bg="#737373", font=("Arial", 20), height=3, anchor="n")
       label_registr.grid(row=0, column=0, columnspan=2, sticky="we")
       label_login = Label(win, text="Login", bg="#737373", font=("Arial", 14))
       label_login.grid(row=1, column=0, sticky="e")
       label_pass = Label(win, text="Password", bg="#737373", font=("Arial", 14), height=3)
       label_pass.grid(row=2, column=0, sticky="e")
       input_login = Entry(win)
       input_login.grid(row=1, column=1, sticky="w")
       input_pass = Entry(win)
       input_pass.grid(row=2, column=1, sticky="w")
       Button(win, text="Ввійти", padx=10, command=check).grid(row=3, column=0, sticky='e')
       Button(win, text="Ввійти як гість", command=guest).grid(row=3, column=1, sticky='w', padx=50)
       label_file = Label(win, text="""Якщо у вас вже є файл, який ви 
       хочете відкрити, натисніть кнопку:""", bg="#737373", font=("Arial", 10))
       label_file.grid(row = 4, column=0, sticky='e', pady=20)
       Button(win, text="Open file", padx=10, command=callback).grid(row=4, column=1, sticky='w', padx=55, pady=20)

def callback():
       global filename, action
       filename= fd.askopenfilename()
       action = False

def guest_window(filename):
       global win
       if 'Exel.csv' not in os.listdir('D:/Doc_groups'):
              with open('D:/Doc_groups/Exel.csv', 'a', newline='') as file:
                     csv.writer(file)

       if action:
              filename = 'D:/Doc_groups'

              if 'Exel.csv' in os.listdir(filename):
                     file = open(filename + '/Exel.csv', 'r')
       else:
              file = open(filename, 'r')
       list = []
       reader = csv.reader(file)
       for row in reader:
              list.append(row)
       win = create_window()
       win.attributes('-alpha', 1)
       win.geometry('800x600')
       heads = ['№', 'ПІБ', 'Середній бал', 'Форма навчання', 'group']
       exel = ttk.Treeview(win, show='headings')
       exel['columns'] = heads
       exel.column('№', width=1, anchor=CENTER)
       exel.column('ПІБ', width=150, anchor=CENTER)
       exel.column('Середній бал', width=50, anchor=CENTER)
       exel.column('Форма навчання', width=60, anchor=CENTER)
       exel.column('group', width=40, anchor=CENTER)

       for header in heads:
              exel.heading(header, text=header, anchor='center')
              exel.column(header, anchor='center')

       for row in list:
              exel.insert('', END, values=row)

       scroll_pane = ttk.Scrollbar(win, command=exel.yview)
       exel.configure(yscrollcommand=scroll_pane.set)
       scroll_pane.pack(side=RIGHT, fill=Y)
       exel.pack(expand=YES, fill=BOTH)


def admin_window(filename):
       global win, file
       file = filename
       text = ''
       list = []

       def update_table():
              for i in exel.get_children():
                     exel.delete(i)
              if 'Exel.csv' not in os.listdir('D:/Doc_groups'):
                     with open('D:/Doc_groups/Exel.csv', 'a', newline='', encoding='utf8') as file:
                            csv.writer(file)
              if action:
                     filename = 'D:/Doc_groups'

                     if 'Exel.csv' in os.listdir(filename):
                            file = open(filename + '/Exel.csv', 'r', encoding='utf8')
              else:
                     file = open(file, 'r', encoding='utf8')
              reader = csv.reader(file, delimiter=';')
              for row in reader:
                     if row != []:
                            list.append(row)
              for row in list:
                     exel.insert('', END, values=row)

       def add():
              def overwriting():
                     if 'Exel.csv' not in os.listdir('D:/Doc_groups'):
                            with open('D:/Doc_groups/Exel.csv', 'w', newline='') as file:
                                   csv.writer(file)
                     if action:
                            filename = 'D:/Doc_groups'

                            if 'Exel.csv' in os.listdir(filename):
                                   file = open(filename + '/Exel.csv', 'w')
                     else:
                            file = open(file, 'w')
                     line = [len(list)+1,name_in.get(),point_in.get(),form_in.get(),'PA']
                     list.append(line)
                     csv.writer(file, delimiter = ';').writerows(list)
                     temp_win.destroy()
                     update_table()
              temp_win = create_window()
              temp_win.geometry('300x200')
              temp_win.resizable(width=False, height=False)
              empty_lb = Label(temp_win, text='', bg="#737373", font=("Arial", 10), height=3)
              name_lb = Label(temp_win, text='Введіть ПІБ абітурієнта', bg="#737373", font=("Arial", 10))
              point_lb = Label(temp_win, text='Введіть середній бал', bg="#737373", font=("Arial", 10))
              form_lb = Label(temp_win, text='Введіть форму навчання', bg="#737373", font=("Arial", 10))
              name_in = Entry(temp_win)
              point_in = Entry(temp_win)
              form_in = Entry(temp_win)
              temp_win.grid_columnconfigure(0, minsize=150)
              temp_win.grid_columnconfigure(1, minsize=150)
              empty_lb.grid(row=0, column=0)
              name_lb.grid(row=1, column=0, sticky='w')
              point_lb.grid(row=2, column=0, sticky='w')
              form_lb.grid(row=3, column=0, sticky='w')
              name_in.grid(row=1, column=1, sticky='w')
              point_in.grid(row=2, column=1, sticky='w')
              form_in.grid(row=3, column=1, sticky='w')
              Button(temp_win, text='Confirm', command=overwriting).grid(row=4, column=0, columnspan=2, pady=10)

       def edit():
              def change_text():
                     global cor_x, cor_y
                     if column_in.get() == 'ПІБ':
                            cor_x = 1
                     elif column_in.get() == 'Середній бал':
                            cor_x = 2
                     elif column_in.get() == 'Форма навчання':
                            cor_x = 3
                     cor_y = int(row_in.get()) - 1
                     text = list[cor_y][cor_x]
                     cell = Label(toolbar, text=text, font=("Arial", 14))
                     cell.grid(row=1, column=0, columnspan=3, sticky='we')
                     temp_win.destroy()
              temp_win = create_window()
              temp_win.geometry('300x200')
              temp_win.resizable(width=False, height=False)
              empty_lb = Label(temp_win, text='', bg="#737373", font=("Arial", 10), height=4)
              row_lb = Label(temp_win, text='Введіть номер строки', bg="#737373", font=("Arial", 10))
              column_lb = Label(temp_win, text='Введіть назву стовпчика', bg="#737373", font=("Arial", 10))
              row_in = Entry(temp_win)
              column_in = Entry(temp_win)
              temp_win.grid_columnconfigure(0, minsize=150)
              temp_win.grid_columnconfigure(1, minsize=150)
              empty_lb.grid(row=0, column=0)
              row_lb.grid(row=1, column=0, sticky='w')
              row_in.grid(row=1, column=1, sticky='w')
              column_lb.grid(row=2, column=0, sticky='w')
              column_in.grid(row=2, column=1, sticky='w')
              Button(temp_win, text='Confirm', command=change_text).grid(row=3, column=0, columnspan=2, pady=10)

       def update_data(list_of_groups):
              list=[]
              print(list)
              for i in range(len(list_of_groups)):
                     for n in range(len(list_of_groups[i])):
                            list_of_groups[i][n][4] += '-' + str(i+1)
              for i in range(len(list_of_groups)):
                     for n in range(len(list_of_groups[i])):
                            list.append(list_of_groups[i][n])
              if 'Exel.csv' not in os.listdir('D:/Doc_groups'):
                     with open('D:/Doc_groups/Exel.csv', 'w', newline='') as file:
                            csv.writer(file)
              if action:
                     filename = 'D:/Doc_groups'

                     if 'Exel.csv' in os.listdir(filename):
                            file = open(filename + '/Exel.csv', 'w')
              else:
                     file = open(file, 'w')
              csv.writer(file, delimiter=';').writerows(list)
              update_table()

       def sort():
              list_of_groups = []
              def create_groups():
                     for i in range(int(num_in.get())):
                            list_of_groups.append([])
                     for i in range(len(list)):
                            for j in range(0, len(list) - i - 1):
                                   if list[j + 1][2] != '-':
                                          if list[j][2] == '-':
                                                 list[j][2], list[j + 1][2] = list[j + 1][2].split(',')[0], list[j][2].split(',')[0]
                                          elif list[j][2] > list[j + 1][2]:
                                                 list[j][2], list[j + 1][2] = list[j + 1][2], list[j][2]
                     k=0
                     for t in range(len(list)):
                            if k == int(num_in.get()):
                                   k = 0
                            list_of_groups[k].append(list[t])
                            k+=1
                     update_data(list_of_groups)
                     temp_win.destroy()
              temp_win = create_window()
              temp_win.geometry('300x200')
              temp_win.resizable(width=False, height=False)
              empty_lb = Label(temp_win, text='', bg="#737373", font=("Arial", 10), height=4)
              num_lb = Label(temp_win, text='Введіть кількість груп', bg="#737373", font=("Arial", 10))
              num_in = Entry(temp_win)
              temp_win.grid_columnconfigure(0, minsize=150)
              temp_win.grid_columnconfigure(1, minsize=150)
              empty_lb.grid(row=0, column=0)
              num_lb.grid(row=1, column=0, sticky='w')
              num_in.grid(row=1, column=1, sticky='w')
              Button(temp_win, text='Confirm', command=create_groups).grid(row=4, column=0, columnspan=2, pady=10)

       def save():
              list[cor_y][cor_x] = cell_input.get()
              if 'Exel.csv' not in os.listdir('D:/Doc_groups'):
                     with open('D:/Doc_groups/Exel.csv', 'w', newline='') as file:
                            csv.writer(file)
              if action:
                     filename = 'D:/Doc_groups'

                     if 'Exel.csv' in os.listdir(filename):
                            file = open(filename + '/Exel.csv', 'w')
              else:
                     file = open(file, 'w', encoding='utf8')
              csv.writer(file, delimiter=';').writerows(list)
              text = ''
              cell = Label(toolbar, text=text, font=("Arial", 14))
              cell.grid(row=1, column=0, columnspan=3, sticky='we')
              update_table()

       if 'Exel.csv' not in os.listdir('D:/Doc_groups'):
              with open('D:/Doc_groups/Exel.csv', 'a', newline='', encoding='utf8') as file:
                     csv.writer(file)
       if action:
              filename = 'D:/Doc_groups'

              if 'Exel.csv' in os.listdir(filename):
                     file = open(filename + '/Exel.csv', 'r', encoding='utf8')
       else:
              file = open(filename, 'r', encoding='utf8')
       reader = csv.reader(file, delimiter = ';')
       for row in reader:
              if row != []:
                     list.append(row)
       win = create_window()
       win.attributes('-alpha', 1)
       win.geometry('800x600')

       toolbar = Frame(win)
       toolbar.pack(fill = 'x')
       Button(toolbar, text='Редагувати', command=edit).grid(row = 0, column =0)
       Button(toolbar, text='Сортувати', command=sort).grid(row = 0, column =1)
       Button(toolbar, text='Регістрація', command=reg).grid(row = 0, column =2)
       Button(toolbar, text='Зберегти', command=save).grid(row=1, column=4)
       Button(toolbar, text='Додати інформацію', command=add).grid(row=0, column=3, sticky='w')
       cell = Label(toolbar, text = text, font=("Arial", 14))
       cell.grid(row = 1, column = 0, columnspan= 3, sticky='we')
       cell_input = Entry(toolbar)
       cell_input.grid(row = 1, column=3)

       heads = ['№', 'ПІБ', 'Середній бал', 'Форма навчання', 'group']
       exel = ttk.Treeview(win, show='headings')
       exel['columns'] = heads
       exel.column('№', width=1, anchor=CENTER)
       exel.column('ПІБ', width=100, anchor=CENTER)
       exel.column('Середній бал', width=50, anchor=CENTER)
       exel.column('Форма навчання', width=60, anchor=CENTER)
       exel.column('group', width=40, anchor=CENTER)
       for header in heads:
              exel.heading(header, text=header, anchor='center')
              exel.column(header, anchor='center')
       for row in list:
              exel.insert('', END, values=row)
       scroll_pane = ttk.Scrollbar(win, command=exel.yview)
       exel.configure(yscrollcommand=scroll_pane.set)
       scroll_pane.pack(side=RIGHT, fill=Y)
       exel.pack(expand=YES, fill=BOTH)

def auth():
       win.destroy()
       authorization_window()

def reg():
       win.destroy()
       registration_window()

def guest():
       win.destroy()
       guest_window(filename)

def admin():
       win.destroy()
       admin_window(filename)

if 'Doc_groups' not in os.listdir('D:/'):
       os.makedirs(os.path.join('D:/', 'Doc_groups'))

if "Accounts.txt" in os.listdir('D:/Doc_groups'):
       if open('D:/Doc_groups/Accounts.txt', 'r').readlines()[0][0] != ' ':
              authorization_window()
       else:
              registration_window()
else:
       registration_window()

mainloop()