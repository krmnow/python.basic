try:
    import tkinter
except ImportError:
        import Tkinter as tkinter

import os

mainWindow = tkinter.Tk()

mainWindow.title("Greed demo")
mainWindow.geometry('640x480+8+400')
mainWindow['padx'] = 8

label = tkinter.Label(mainWindow, text="Costamdemo")
label.grid(row=0, column=0, columnspan=3 )

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
mainWindow.columnconfigure(4, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')
for zone in os.listdir('/Windows/System32'):
    fileList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set

#frame for inter buttons

optionFrame = tkinter.LabelFrame(mainWindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()
rbValue.set(1)

#radio buttons

radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="Patch", value=1, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="Timestop", value=1, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

resultLabel = tkinter.Label(mainWindow, text="reuslt")
resultLabel.grid(row=2, column=2, sticky="sw")
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky="sw")

#frame for time spinners

timeFrame = tkinter.LabelFrame(mainWindow, text="time")
timeFrame.grid(row=3, column=0, sticky="new")
#time spinnwers

hourSpinner = tkinter.Spinbox(timeFrame, width=2, value=tuple(range(0,24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
hourSpinner.grid(row=0, column=1)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
secondSpinner.grid(row=0, column=4)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)

timeFrame['padx'] = 36

#frame for the date spinners

dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky="new")

#Date labels

dayLabel = tkinter.Label(dateFrame, text="day")
montLabel = tkinter.Label(dateFrame, text="month")
yearLabel = tkinter.Label(dateFrame, text="year")
dayLabel.grid(row=0, column=0, sticky='w')
montLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

#date spinners

daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, values = ("Jan", "feb", "mar", "apr", "may", "jun", "aug", "wrze", "paz", "list", "grud" ))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

# button

okButton = tkinter.Button(mainWindow, text="OK")
cancelButton = tkinter.Button(mainWindow, text="Cancel", command=mainWindow.destroy)
okButton.grid(row=4, column=3, sticky="e")
cancelButton.grid(row=4, column=4, sticky="w")


mainWindow.mainloop()
