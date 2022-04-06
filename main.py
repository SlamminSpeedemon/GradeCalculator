import tkinter as tk
from tkinter import ttk
from tkinter import *
from Course import *

root = Tk()
# make course objects
programmingObj = Course("Programming", root)
artObj = Course("Art", root)
scienceObj = Course("Science", root)
mathObj = Course("Math", root)
historyObj = Course("History", root)


# define functions
def takeGrades():
    programmingObj.takeGUIGrade()
    artObj.takeGUIGrade()
    scienceObj.takeGUIGrade()
    mathObj.takeGUIGrade()
    historyObj.takeGUIGrade()


# Window functions (all codes are wrapped in functions)
def AddGrades():  # opens new window to add grades
    # Grade Adder GUI
    gradeWindow = Tk()

    gradeWindow.geometry('360x390')
    gradeWindow.configure(background='#F0F8FF')
    gradeWindow.title('1453 - Grade Program - Grade adder')

    # GUI variables
    xPos = 10
    yPos = 10
    yPosChanger = 50

    # instructions
    Label(gradeWindow, text="Enter more grades", bg='#F0F8FF', font=('arial', 16, 'bold')).place(x=xPos, y=yPos)

    # place entries
    programmingObj.gradeAddGUIstart(gradeWindow, xPos, yPos + 1 * yPosChanger)
    artObj.gradeAddGUIstart(gradeWindow, xPos, yPos + 2 * yPosChanger)
    scienceObj.gradeAddGUIstart(gradeWindow, xPos, yPos + 3 * yPosChanger)
    mathObj.gradeAddGUIstart(gradeWindow, xPos, yPos + 4 * yPosChanger)
    historyObj.gradeAddGUIstart(gradeWindow, xPos, yPos + 5 * yPosChanger)

    # Button to add scores
    Button(gradeWindow, text='Add', bg='#8B8378', font=('arial', 18, 'normal'), command=lambda: takeGrades()).place(
        x=xPos, y=yPos + 6 * yPosChanger)
    Button(gradeWindow, text='Clear', bg='#CD5B45', font=('arial', 18, 'normal'), command=lambda: takeGrades()).place(
        x=xPos + 240, y=yPos + 6 * yPosChanger)


def normalWindow():
    # This is the section of code which creates the main window
    root.geometry('826x504')
    root.configure(background='#F0F8FF')
    root.title('1453 - Grade Program')

    # GUI variables
    xStart = 65
    xAdd = 150
    yStart = 150
    yAdd = 50

    # Labels
    Label(root, text="Class Name: ", bg='#F0F8FF', font=('arial', 18, 'bold')).place(x=xStart - 45, y=20)
    Label(root, text="# of Scores ", bg='#F0F8FF', font=('arial', 16, 'bold')).place(x=xStart + 1 * xAdd, y=23)
    Label(root, text="Avg: ", bg='#F0F8FF', font=('arial', 16, 'bold')).place(x=xStart + 2 * xAdd, y=23)
    Label(root, text="High: ", bg='#F0F8FF', font=('arial', 16, 'bold')).place(x=xStart + 3 * xAdd, y=23)
    Label(root, text="Low: ", bg='#F0F8FF', font=('arial', 16, 'bold')).place(x=xStart + 4 * xAdd, y=23)

    # tell objects to display info
    programmingObj.GUIstart(xStart, yStart + 1 * yAdd)
    artObj.GUIstart(xStart, yStart + 2 * yAdd)
    scienceObj.GUIstart(xStart, yStart + 3 * yAdd)
    mathObj.GUIstart(xStart, yStart + 4 * yAdd)
    historyObj.GUIstart(xStart, yStart + 5 * yAdd)

    # Buttons
    Button(root, text='Add Grades', bg='#8B8378', font=('arial', 18, 'normal'), command=lambda: AddGrades()).place(
        x=227, y=443)

    root.mainloop()


normalWindow()
