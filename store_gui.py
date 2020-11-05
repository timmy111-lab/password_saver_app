from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
root = Tk()
root.title('Password Saver')
image_one = ImageTk.PhotoImage(Image.open('backg.jpg'))
image_label = Label(root, image = image_one)	
image_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
my_frame = LabelFrame(root, text = '', padx = 20, pady = 20)
my_frame.pack(padx = 20, pady = 20)

# connection = sqlite3.connect('users.db')

# c = connection.cursor()

# c.execute("CREATE TABLE IF NOT EXISTS timmy(First_Name TEXT, Last_Name TEXT, Account TEXT, Password VARCHAR)")

# connection.commit()
# connection.close()


firstname = Label(my_frame, text = 'First Name')
firstname.grid(row = 1, column = 0, padx = 10, pady = 15)
f_name = Entry(my_frame)
f_name.grid(row = 1,column = 1, padx = 10, pady = 15)


lastname = Label(my_frame, text = 'Last Name')
lastname.grid(row = 3, column = 0, padx = 10, pady = 15) 
l_name = Entry(my_frame)
l_name.grid(row = 3,column = 1, padx = 10, pady = 15)

account = Label(my_frame, text = 'Insert Account')
account.grid(row = 9 , column = 0, padx = 10, pady = 15)
acct = Entry(my_frame)
acct.grid(row = 9, column = 1, padx = 10, pady = 15)

delete_box = Label(my_frame, text = 'Data Number ')
delete_box.grid(row = 14, column = 0, padx = 10, pady = 15)
del_box = Entry(my_frame)
del_box.grid(row = 14, column = 1, padx = 10, pady =15)


# choices = {'Facebook','Instagram','Email', 'Viber', 'Github', 'python anywhere', 'Twitter', 'Snapchat'}
# opvar.set('Facebook')

# popupMenu = OptionMenu(my_frame,textvariable = opvar, *choices)
# options = Label(my_frame, text = 'Select Account').grid(row = 9, column = 0)
# popupMenu.grid(row = 9, column = 1)
# popupMenu.config(width = 14)



password = Label(my_frame, text = 'Password')
password.grid(row = 7, column = 0, padx = 10, pady = 15) 
pas = Entry(my_frame)
pas.grid(row = 7,column = 1, padx = 10, pady = 15)

def save():
	messagebox.showinfo('Hello', 'Data successfully saved')
	btn  = Button(my_frame, text = 'ok', command = save)
	# pop_up = Label(my_frame, text = 'Data saved successful')
	# pop_up.grid(row = 0, column = 0, columnspan = 2, padx = 50, pady = 15, )
	connection = sqlite3.connect('users.db')

	c = connection.cursor()

	c.execute("INSERT INTO timmy(First_Name, Last_Name, Account, Password) VALUES(?,?,?,?)", (f_name.get(),l_name.get(),acct.get(),pas.get()))
	
	connection.commit()
	print('successful')
	connection.close()

# def view():

# 	connection = sqlite3.connect('users.db')
# 	c = connection.cursor()
# 	c.execute("SELECT *, oid FROM timmy")
# 	data = c.fetchall()

# 	sec_data = ''
# 	for datas in data:
# 		sec_data += str(datas[0]) + " " + str(datas[1]) + " " +str(datas[2])+ " " +str(datas[3])+ " " +"\n"

# 	query_label = Label(my_frame, text = sec_data)
# 	query_label.grid(row =16, column = 0, columnspan = 2)
	

# 	connection.commit()
# 	print('successful')
# 	connection.close()

# def view():
# 	view_query = Tk()
# 	view_query.title("Saved Data")
# 	connection = sqlite3.connect('users.db')
# 	c = connection.cursor()
# 	c.execute("SELECT *, oid  FROM timmy")
# 	data = c.fetchall()
# 	my_info =''
# 	for datas in data:
# 		btn = Button(view_query, text = 'Delete')
# 		btn.grid(row = 0, column = 5)
# 		my_info+= f'{datas[0]}  {datas[1]}  {datas[2]}  {datas[3]}  {datas[4]}  {datas[5]}{btn}  \n'
# 		my_data = Label(view_query, text = my_info, padx = 20, pady = 20)
# 		my_data.grid(row = 0, column = 0)


# 	connection.commit()
# 	print('successful')
# 	connection.close()


def view():
	view_query = Tk()
	view_query.title("Saved Data")
	connection = sqlite3.connect('users.db')
	c = connection.cursor()
	c.execute("SELECT *, oid  FROM timmy")
	data = c.fetchall()
	for index, datas in enumerate(data):
		num = 0
		for datas2 in datas:
			my_data = Label(view_query, text = datas2, padx = 20, pady = 20)
			my_data.grid(row = index, column = num)
			num +=1
			# print(index)



	connection.commit()
	print('successful')
	connection.close()


def delete():
	connection = sqlite3.connect('users.db')

	c = connection.cursor()
	c.execute("DELETE  FROM timmy WHERE oid = " + del_box.get())
	del_box.delete(0, END)

	connection.commit()
	print('successful')
	connection.close()



btn_save = Button(my_frame, text = 'Save Credentials', padx = 50, pady = 15, borderwidth = 3, width = 17, command = save)
btn_save.grid(row = 11, column = 0, columnspan = 2)

btn_view = Button(my_frame, text = 'View Credentials', padx = 50, pady = 15, borderwidth = 3, width = 17, command = view)
btn_view.grid(row = 13, column = 0, columnspan = 2)

btn_delete = Button(my_frame, text = 'Delete Data', padx = 50, pady = 15, borderwidth = 3, width = 17, command = delete)
btn_delete.grid(row = 15, column = 0, columnspan = 2)

root.mainloop()




