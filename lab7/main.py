from tkinter import * 
from datetime import datetime, date, time 
  
def saveChangeInFile():
	file = open('rasp.txt', 'w', encoding="utf-8")

	for lineItem in list.listItems:
		file.write(lineItem + '\n')

	file.close()

def addListItem():
	textInput = entryInput.entry.get()

	if (len(textInput) == 0):
		return

	list.list.insert(END, textInput)
	list.listItems.append(textInput)

	entryInput.entry.delete(0, END)
	saveChangeInFile()

def removeListItem():
	if (len(list.list.curselection()) == 0):
		return

	indexActive = list.list.curselection()[0]

	list.list.delete(indexActive)
	list.listItems.pop(indexActive)

	entryInput.entry.delete(0, END)

	saveChangeInFile()

def changeListItem():
	if (len(list.list.curselection()) == 0):
		return

	indexActive = list.list.curselection()[0]

	text = entryInput.entry.get()

	list.list.delete(indexActive)
	list.list.insert(indexActive, text)

	list.listItems[indexActive] = text

	entryInput.entry.delete(0, END)

	saveChangeInFile()

def onSelectListItem(e):
	indexActive = list.list.curselection()

	if (len(indexActive) == 0):
		return

	text = list.list.get(indexActive)

	entryInput.entry.delete(0, END)
	entryInput.entry.insert(0, text)

def onClickSort():
	file = open('rasp.txt', encoding='utf-8')
	sortArr = file.readlines()
	file.close()

	for i in range(len(sortArr) - 1):
		for j in range(len(sortArr) - i - 1):
			str1 = sortArr[j][0:16]
			date1 = datetime.strptime(str1, '%d/%m/%Y %H:%M')

			str2 = sortArr[j + 1][0:16]
			date2 = datetime.strptime(str2, '%d/%m/%Y %H:%M')

			if ((date1 - date2).total_seconds() > 0):
				sortArr[j], sortArr[j + 1] = sortArr[j + 1], sortArr[j]

	list.list.delete(0, END)
	entryInput.entry.delete(0, END)

	for line in sortArr:
		lineFormat = line.replace('\n', '')
		list.list.insert(END, lineFormat)

def onClickFilter():
	try:
		textInput = entryInput.entry.get()
		dateInput = datetime.strptime(textInput[0:16], '%d/%m/%Y %H:%M')

		filterArr = []

		for line in list.listItems:
			dateLine = datetime.strptime(line[0:16], '%d/%m/%Y %H:%M')

			if ((dateLine - dateInput).total_seconds() >= 0):
				filterArr.append(line)

		list.list.delete(0, END)

		for line in filterArr:
			lineFormat = line.replace('\n', '')
			list.list.insert(END, lineFormat)
	except ValueError:
		return

def onClickShowAll():
	list.list.delete(0, END)

	for line in list.listItems:
		list.list.insert(END, line)
	
class LabelRasp:
	def __init__(self):
		self.lbl = Label(root)

		self.lbl['text'] = 'Расписание электричек'
		self.lbl['fg'] = '#fff'
		self.lbl['bg'] = '#222'
		self.lbl['font'] = 'Arial 12'

		self.lbl.pack(side = 'top', fill = 'x', ipady=8)


class EntryInput:
	def __init__(self):
		self.entry = Entry(root)

		self.entry['width'] = 10

		self.entry.place(relx=.5, rely=.8, anchor="c", height=20, width=250)

class ButtonAdd:
	def __init__(self):
		self.btn = Button(root)  

		self.btn['text'] = 'Добавить'
		self.btn['command'] = addListItem

		self.btn.place(relx=.2, rely=.85, anchor="c", height=20, width=70)

class ButtonChange:
	def __init__(self):
		self.btn = Button(root)  

		self.btn['text'] = 'Изменить'
		self.btn['command'] = changeListItem

		self.btn.place(relx=.5, rely=.85, anchor="c", height=20, width=70)


class ButtonRemove:
	def __init__(self):
		self.btn = Button(root)  

		self.btn['text'] = 'Удалить'
		self.btn['command'] = removeListItem

		self.btn.place(relx=.8, rely=.85, anchor="c", height=20, width=70)

class List:
	def __init__(self):
		self.list = Listbox(root)

		file = open('rasp.txt', encoding='utf-8')
		lines = file.readlines()

		self.listItems = []
		for line in lines:
			lineFormat = line.replace('\n', '')
			self.listItems.append(lineFormat)

		file.close()


		self.list.bind('<<ListboxSelect>>', onSelectListItem)

		self.list['selectmode'] = 'EXTENDED'

		self.list['width'] = 28
		self.list['height'] = 16
		self.list['font'] = 'Arial 13'

		self.list.place(relx=.5, rely=.43, anchor="c")

		for line in self.listItems:
			self.list.insert(END, line)

class ButtonSort:
	def __init__(self):
		self.btn = Button(root)  

		self.btn['text'] = 'Сортировка по времени'
		self.btn['command'] = onClickSort

		self.btn.place(relx=.5, rely=.9, anchor="c", height=20, width=250)

class ButtonFilter:
	def __init__(self):
		self.btn = Button(root)  

		self.btn['text'] = 'Показать актуальные'
		self.btn['command'] = onClickFilter

		self.btn.place(relx=.33, rely=.95, anchor="c", height=20, width=150)

class ButtonShowAll:
	def __init__(self):
		self.btn = Button(root)  

		self.btn['text'] = 'Показать все'
		self.btn['command'] = onClickShowAll

		self.btn.place(relx=.765, rely=.95, anchor="c", height=20, width=90)


root = Tk()  
root.title("Расписание электричек")  
root.geometry('300x500')

labelRaspObj = LabelRasp()
entryInput = EntryInput()
btnAdd = ButtonAdd()
btnChange = ButtonChange()
btnRemove = ButtonRemove()
btnSort = ButtonSort()
btnFiler = ButtonFilter()
btnShowAll = ButtonShowAll()
list = List()

root.mainloop()