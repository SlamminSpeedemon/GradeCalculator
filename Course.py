from tkinter import *
class Course:
    def __init__(self, courseName, window):
        self.name = courseName
        self.scoreList = []
        self.root = window
        self.courseString = StringVar()

    def setList(self, newList): #using an append statement messes stuff up
        self.scoreList = newList
        self.GUIUpdate()

    def getList(self):
        return self.scoreList

    def getMax(self):
        return max(self.scoreList)

    def getMin(self):
        return min(self.scoreList)

    def getSummation(self):
        counter = 0
        for i in range(len(self.scoreList)):
            counter += self.scoreList[i]
        return counter

    def getAverage(self):
            return round(self.getSummation()/len(self.scoreList),3)

    def GUIstart(self, xPos,yPos):
        self.GUIUpdate()
        Label(self.root, textvariable=self.courseString,bg='#F0F8FF', font=('arial', 16, 'normal')).place(x=xPos, y=yPos)

    def GUIUpdate(self):
        print(self.scoreList)
        if len(self.scoreList) == 0:
            self.courseString.set(self.name + "\t\t" + "no info")
        else:
            self.courseString.set(self.name +"\t\t"+str(len(self.scoreList))+"\t\t"+str(self.getAverage())+"\t\t"+str(self.getMax())+"\t\t"+str(self.getMin()))

    def gradeAddGUIstart(self, window, xPos, yPos):
        Label(window, text = self.name, bg='#F0F8FF', font=('arial', 16, 'normal')).place(x=xPos, y=yPos)
        self.tempEntry = Entry(window)
        self.tempEntry.place(x=xPos + 200,y=yPos + 8)

    def takeGUIGrade(self):
        return self.tempEntry.get()

    def getName(self):
        return self.name

    def clearInput(self):
        self.tempEntry.delete(0,999)