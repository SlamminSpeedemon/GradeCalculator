from tkinter import *
class Course:
    def __init__(self, courseName, window):
        self.name = courseName
        self.scoreList = []
        self.root = window
        self.courseString = StringVar()

    def addScore(self, score):
        try:
            self.scoreList.append(round(int(score)))
        except:
            print("Invalid entry for",self.name)

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

            return self.getSummation()/len(self.scoreList)

    def GUIstart(self, xPos,yPos):
        self.GUIUpdate()
        Label(self.root, textvariable=self.courseString,bg='#F0F8FF', font=('arial', 16, 'normal')).place(x=xPos, y=yPos)

    def GUIUpdate(self):
        if (len(self.scoreList) == 0):
            self.courseString.set(self.name + "\t" + "no info")
        else:
            self.courseString.set(self.name +"\t"+str(len(self.scoreList))+"\t"+str(self.getAverage()+"\t"+str(self.getMax())+"\t"+str(self.getMin())))

    def gradeAddGUIstart(self, window, xPos, yPos):
        Label(window, text = self.name, bg='#F0F8FF', font=('arial', 16, 'normal')).place(x=xPos, y=yPos)
        self.tempEntry = Entry(window)
        self.tempEntry.place(x=xPos + 200,y=yPos + 8)

    def takeGUIGrade(self):
        print(self.tempEntry.get())
        self.addScore(self.tempEntry.get())