import tkinter as tk
import time
import winsound

def timeProcessor(add):
    currTimeR = list(time.localtime(time.time()+add*60)[3:5])
    for i in range(2):
        element = str(currTimeR[i])
        if len(element) == 1:
            currTimeR[i] = "0" + element
    return str(currTimeR[0])+":"+str(currTimeR[1])

def interface():
    root = tk.Tk()
    root.title("Pomodoro Timer")

    content = tk.Frame(root)
    frame = tk.Frame(content, borderwidth=5, width=500, height=250)

    global running
    running=True
    global labelList
    labelList = ["","5 MIN. BREAK #1","","5 MIN. BREAK #2","","5 MIN. BREAK #3","","25 MIN. BREAK"]


    previewIntro = tk.Label(content, text="Welcome to Pomodoro Timer.\n"
                                          "Your next Pomodoro will be as follows:")
    previewIntro.grid(column=0, row=0, columnspan=3, sticky='NW')
    taskFrame = tk.Frame(content, relief='ridge', borderwidth=1, width=250, height=170)

    currTimeText = tk.Label(content, text="{}".format(timeProcessor(0)), font='Arial 28 bold')
    currTimeText.grid(column=4, columnspan=3, row=0, rowspan=2, sticky='NSEW')

    preview1time = tk.Label(content,text="{} - {}".format(timeProcessor(0),timeProcessor(25)))
    break1time = tk.Label(content,text="{} - {}".format(timeProcessor(25),timeProcessor(30)))
    break1text = tk.Label(content,text="5 MIN. BREAK #1", font='Arial 9 bold')
    preview2time = tk.Label(content,text="{} - {}".format(timeProcessor(30),timeProcessor(55)))
    break2time = tk.Label(content,text="{} - {}".format(timeProcessor(55),timeProcessor(60)))
    break2text = tk.Label(content,text="5 MIN. BREAK #2", font='Arial 9 bold')
    preview3time = tk.Label(content,text="{} - {}".format(timeProcessor(60),timeProcessor(85)))
    break3time = tk.Label(content,text="{} - {}".format(timeProcessor(85),timeProcessor(90)))
    break3text = tk.Label(content,text="5 MIN. BREAK #3", font='Arial 9 bold')
    preview4time = tk.Label(content,text="{} - {}".format(timeProcessor(90),timeProcessor(115)))
    break4time = tk.Label(content,text="{} - {}".format(timeProcessor(115),timeProcessor(140)))
    break4text = tk.Label(content,text="25 MIN. BREAK", font='Arial 9 bold')

    preview1time.grid(column=0, row=1, sticky='NW')
    break1time.grid(column=0, row=2, sticky='NW')
    break1text.grid(column=1, row=2, sticky='NW')
    preview2time.grid(column=0, row=3, sticky='NW')
    break2time.grid(column=0, row=4, sticky='NW')
    break2text.grid(column=1, row=4, sticky='NW')
    preview3time.grid(column=0, row=5, sticky='NW')
    break3time.grid(column=0, row=6, sticky='NW')
    break3text.grid(column=1, row=6, sticky='NW')
    preview4time.grid(column=0, row=7, sticky='NW')
    break4time.grid(column=0, row=8, sticky='NW')
    break4text.grid(column=1, row=8, sticky='NW')

    def timeUpdate():
        currTimeText['text'] = timeProcessor(0)
        root.after(1000, timeUpdate)

    def textUpdate():
        preview1time['text'] = "{} - {}".format(timeProcessor(0),timeProcessor(25))
        preview2time['text'] = "{} - {}".format(timeProcessor(30),timeProcessor(55))
        preview3time['text'] = "{} - {}".format(timeProcessor(60),timeProcessor(85))
        preview4time['text'] = "{} - {}".format(timeProcessor(90),timeProcessor(115))

        break1time['text']="{} - {}".format(timeProcessor(25),timeProcessor(30))
        break2time['text']="{} - {}".format(timeProcessor(55),timeProcessor(60))
        break3time['text']="{} - {}".format(timeProcessor(85),timeProcessor(90))
        break4time['text']="{} - {}".format(timeProcessor(115),timeProcessor(140))
        if not running:
            root.after(1000,textUpdate) #update every 1000 ms

    textUpdate() #run for first time
    timeUpdate()

    def SaveTimes():
        runButton.config(state='disabled')
        stopButton.config(state='normal')
        global timeList, running, runningLabel, currentTask, count, runCount
        count = 0
        timeList=[timeProcessor(25),timeProcessor(30),timeProcessor(55),
                      timeProcessor(60),timeProcessor(85),timeProcessor(90),timeProcessor(115),
                      timeProcessor(140)]

        running=True
        runningLabel = tk.Label(taskFrame, text="Now doing:", foreground="#ff0000")
        runningLabel.place(x=85,y=5)
        currentTask = tk.Label(taskFrame,text="", foreground="#ff0000",font="Arial 16 bold")
        currentTask.place(x=30,y=30)
        winsound.PlaySound(r'start.wav',winsound.SND_FILENAME)
        Run()

    def Run():
        global count
        now = timeProcessor(0)
        currentTask['text']=labelList[count]
        if now in timeList:
            ind = timeList.index(now)
            if ind % 2 == 0:
                sendMessage("Take a break :)")
            else:
                sendMessage("Time to work!")
            winsound.PlaySound(r'alert.wav',winsound.SND_FILENAME)
            timeList[ind]=0
            count += 1
            print(count)

        if running:
            root.after(1000, Run)
        else:
            runningLabel.place_forget()
            currentTask.place_forget()
            textUpdate()
            runButton.config(state="normal")
            stopButton.config(state="disabled")
            winsound.PlaySound(r'end.wav',winsound.SND_FILENAME)
            return


    def sendMessage(mess):
        print(mess) #alternative for using pushBullet
        #apiKey = "KEY"
        #p = PushBullet(apiKey)
        #devices = p.getDevices()
        #p.pushNote(devices[1]["iden"],"Pomodoro", mess)
        #p.pushNote(devices[0]["iden"],"Pomodoro", mess)

    def Quit():
        global running
        running = False

    task1entry = tk.Entry(content, width=20)
    task1entry.insert(0,'Task 1')
    task1entry.grid(column=1, row=1, sticky='NW')
    task2entry = tk.Entry(content, width=20)
    task2entry.insert(0,'Task 2')
    task2entry.grid(column=1, row=3, sticky='NW')
    task3entry = tk.Entry(content, width=20)
    task3entry.insert(0,'Task 3')
    task3entry.grid(column=1, row=5, sticky='NW')
    task4entry = tk.Entry(content, width=20)
    task4entry.insert(0,'Task 4')
    task4entry.grid(column=1, row=7, sticky='NW')

    def updateEntries():
        labelList[0]=task1entry.get()
        labelList[2]=task2entry.get()
        labelList[4]=task3entry.get()
        labelList[6]=task4entry.get()
        root.after(1000,updateEntries)
    updateEntries()


    runButton = tk.Button(content, text='Run Pomodoro', command=SaveTimes)
    runButton.grid(column=0,columnspan=2, row=10, rowspan=2, sticky='NW')
    stopButton = tk.Button(content, text='Stop', command=Quit)
    stopButton.config(state='disabled')
    stopButton.grid(column=1, row=10,sticky='NW')


    content.grid(column=0, row=0, padx=10, pady=10)
    frame.grid(column=0, row=0, columnspan=8, rowspan=10)
    taskFrame.grid(column=2, columnspan=6, row=2, rowspan=8)
    root.wm_iconbitmap(r'tomato.ico')
    root.resizable(width=False, height=False)
    root.mainloop()

interface()