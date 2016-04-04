from PyQt5 import QtGui, QtWidgets, QtCore
from view import *
from dialog import *
from quiz import *
from model import *
from random import randint

import sys
app = QtWidgets.QApplication(sys.argv)

# Setting up main window
mainWindow = QtWidgets.QMainWindow()
ui = Ui_mainWindow()
ui.setupUi(mainWindow)

# Setting up AddDialogButtonBox window
addDialog = QtWidgets.QDialog()
uiAdd = Ui_Dialog()
uiAdd.setupUi(addDialog)

# Setting up EditDialogButtonBox window
editDialog = QtWidgets.QDialog()
uiEdit = Ui_Dialog()
uiEdit.setupUi(editDialog)

# Setting up QuizDialogButtonBox window
quiz = QtWidgets.QDialog(mainWindow)
uiQuiz = Ui_quiz()
uiQuiz.setupUi(quiz)


# Creating directory to save items
directory = Directory()  # Creating directory
directoryItemSize = 5  # Defining size of elements inside directory

# Setting horizontalHeaders to stretch to window size
header = ui.tableWidget.horizontalHeader()
header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


def refresh():
    '''
    Function to clear and renew table view for user.
    '''
    ui.tableWidget.clearContents()  # Clearing table content
    ui.tableWidget.setRowCount(0)  # Reinitializing table to 0 row
    ui.tableWidget.setSortingEnabled(False)  # Stopping sorting while printing table
    for a in range(0, directory.getSize()):
        ui.tableWidget.insertRow(ui.tableWidget.rowCount())  # Add row for every item in directory
        for b in range(0, directoryItemSize):
            cell = QtWidgets.QTableWidgetItem()  # Creating QTableWidgetItem
            cell.setText(directory.items[a][b])  # Adding string to QTableWidgetItem
            ui.tableWidget.setItem(a, b, cell)  # Printing QTableWidgetItem to QWidgetTable
    ui.tableWidget.setSortingEnabled(True)  # Sorting table
    ui.tableWidget.sortItems(0)  # Sort with first column
    print(directory.items)
    print("Refreshed")


def addLine():
    '''
    Function to add an item to table.
    '''
    # Getting text inputs
    eng = uiAdd.lineEn.text()
    fra = uiAdd.lineFr.text()
    esp = uiAdd.lineEs.text()
    ger = uiAdd.lineGer.text()
    jap = uiAdd.lineJap.text()
    # If no inputs -> exit function -> empty line is not added
    if eng == '' and fra == '' and esp == '' and ger == '' and jap == '':
        # Notifying user of failure
        ui.statusbar.showMessage("WARNING : Empty inputs, no row has been added.", 3000)
        return None
    # Creating list and adding inputs to it
    lineToAdd = list()
    lineToAdd.append(eng)
    lineToAdd.append(fra)
    lineToAdd.append(esp)
    lineToAdd.append(ger)
    lineToAdd.append(jap)
    # Resetting LineEdit lines to empty lines
    uiAdd.lineEn.setText('')
    uiAdd.lineEs.setText('')
    uiAdd.lineFr.setText('')
    uiAdd.lineGer.setText('')
    uiAdd.lineJap.setText('')
    # Adding list to directory
    directory.addItem(lineToAdd)
    # Calling refresh function to clear and renew table view of user
    print("*** Current Directory ***")
    refresh()
    # Notifying user of successful operation
    ui.statusbar.showMessage("New row has been added.", 2000)


def deleteLine():
    '''
    Function to delete an item from directory via row selection on screen
    '''
    if ui.tableWidget.selectedItems():
        # Getting selected row words
        one = ui.tableWidget.item(ui.tableWidget.currentRow(), 0).text()
        two = ui.tableWidget.item(ui.tableWidget.currentRow(), 1).text()
        three = ui.tableWidget.item(ui.tableWidget.currentRow(), 2).text()
        four = ui.tableWidget.item(ui.tableWidget.currentRow(), 3).text()
        five = ui.tableWidget.item(ui.tableWidget.currentRow(), 4).text()
        # Deleting selected row item
        directory.deleteItem(one, two, three, four, five)
        # Calling refresh function to clear and renew table view of user
        print("*** Current Directory ***")
        refresh()
        # Notifying user of successful operation
        ui.statusbar.showMessage("Selected row has been deleted.", 2000)
    else:
        # Notifying user to click on a row
        ui.statusbar.showMessage("WARNING : Please select a row to delete.", 3000)


def importData():
    '''
    Function to import a text file.  /!\File must have a specific format/!\
    '''
    # Opening FileDialog to get file path
    openFile = QtWidgets.QFileDialog(mainWindow)
    fileToImportTuple = QtWidgets.QFileDialog.getOpenFileName(openFile, None, "", "Text files (*.txt)")
    # Extracting file path from tuple (fileToImportTuple = ('C:/Users/UserX/Desktop/Project/file.txt', ''))
    fileToImport = str(fileToImportTuple[0])
    if fileToImport != '':
        with open(fileToImport, 'r') as input_data:  # Opening file to import as read only
            directory.clearAll()  # Clearing existing directory
            row = list()  # Creating list for elements to add to directory
            for line in input_data:  # For each line in the file to import
                for word in line.split():  # For each word in line
                    if len(row) == directoryItemSize:  # If length is equal to row size
                        directory.addItem(row)  # Add row to directory
                        row = list()  # Clearing list for next row to import
                    if word == "DONE":  # If word is "DONE"
                        break  # Quit loop
                    row.append(word)  # Add word to row list
            # Calling refresh function to clear and renew table view of user
            print("*** New Directory ***")
            refresh()
        # Notifying user of successful operation
        ui.statusbar.showMessage("Data has been imported.", 2000)
    else:
        return


def exportData():
    '''
    Function to export directory to text file in specific format for possible importation.
    '''
    # Opening FileDialog to get file path
    saveFile = QtWidgets.QFileDialog(mainWindow)
    fileToExportTuple = QtWidgets.QFileDialog.getSaveFileName(saveFile, None, "", "Text files (*.txt)")
    # Extracting file path from tuple (fileToExportTuple = ('C:/Users/UserX/Desktop/Project/file.txt', ''))
    fileToExport = str(fileToExportTuple[0])
    if fileToExport != '':
        with open(fileToExport, "w") as output_data:  # Opening exporting file as write only
            for row in range(0, directory.getSize()):  # For every row in directory
                # Collecting words from row, if no word replace by "***" in output file to ensure proper importation
                if directory.items[row][0] == "":
                    a = "***" + " "
                else:
                    a = str(directory.items[row][0] + " ")
                if directory.items[row][1] == "":
                    b = "***" + " "
                else:
                    b = str(directory.items[row][1] + " ")
                if directory.items[row][2] == "":
                    c = "***" + " "
                else:
                    c = str(directory.items[row][2] + " ")
                if directory.items[row][3] == "":
                    d = "***" + " "
                else:
                    d = str(directory.items[row][3] + " ")
                if directory.items[row][4] == "":
                    e = "***" + " "
                else:
                    e = str(directory.items[row][4])

                output_string = a + b + c + d + e + "\n"  # Create row to export
                output_data.write(output_string)  # Write row into export file
            output_data.write("DONE")  # Writing format signature to ensure future file importation
        # Calling refresh function to clear and renew table view of user
        print("*** Exported Directory ***")
        refresh()
        # Notifying user of successful operation
        ui.statusbar.showMessage("Data has been exported.", 2000)
    else:
        return


def editDialogSetup():
    '''
    Function to set DialogButtonBox when 'Edit' button is clicked.
    '''
    if ui.tableWidget.selectedItems():  # If row has been selected:
        # DialogButtonBox user interface setup
        editDialog.setWindowTitle("Edit")
        uiEdit.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText("Save")
        editDialog.show()
        # Getting corresponding text of selected row from data directory
        one = ui.tableWidget.item(ui.tableWidget.currentRow(), 0).text()
        two = ui.tableWidget.item(ui.tableWidget.currentRow(), 1).text()
        three = ui.tableWidget.item(ui.tableWidget.currentRow(), 2).text()
        four = ui.tableWidget.item(ui.tableWidget.currentRow(), 3).text()
        five = ui.tableWidget.item(ui.tableWidget.currentRow(), 4).text()
        # Setting words of selected row to lines on DialogButtonBox
        uiEdit.lineEn.setText(one)
        uiEdit.lineFr.setText(two)
        uiEdit.lineEs.setText(three)
        uiEdit.lineGer.setText(four)
        uiEdit.lineJap.setText(five)
    else:
        # Notifying user to click on a row
        ui.statusbar.showMessage("WARNING : Please select a row to edit.", 3000)


def saveEdit():
    '''
    Function to change item which has been edited when 'save' button is clicked on DialogButtonBox.
    '''
    # Saving current row locally
    one = ui.tableWidget.item(ui.tableWidget.currentRow(), 0).text()
    two = ui.tableWidget.item(ui.tableWidget.currentRow(), 1).text()
    three = ui.tableWidget.item(ui.tableWidget.currentRow(), 2).text()
    four = ui.tableWidget.item(ui.tableWidget.currentRow(), 3).text()
    five = ui.tableWidget.item(ui.tableWidget.currentRow(), 4).text()
    currentRow = list()
    currentRow.append(one)
    currentRow.append(two)
    currentRow.append(three)
    currentRow.append(four)
    currentRow.append(five)
    # Deleting item
    directory.deleteItem(one, two, three, four, five)
    # Getting text inputs
    eng = uiEdit.lineEn.text()
    fra = uiEdit.lineFr.text()
    esp = uiEdit.lineEs.text()
    ger = uiEdit.lineGer.text()
    jap = uiEdit.lineJap.text()
    # If no inputs -> exit function -> empty line is not added
    if eng == '' and fra == '' and esp == '' and ger == '' and jap == '':
        # Notifying user of failure
        ui.statusbar.showMessage("WARNING : no inputs, row has been deleted.", 3000)
        return None
    # If no change made
    if eng == one and fra == two and esp == three and ger == four and jap == five:
        # Notifying user of failure
        ui.statusbar.showMessage("WARNING : no changes detected.", 3000)
        return None
    # Creating list and adding inputs to it
    lineToAdd = list()
    lineToAdd.append(eng)
    lineToAdd.append(fra)
    lineToAdd.append(esp)
    lineToAdd.append(ger)
    lineToAdd.append(jap)
    # Adding list to directory
    directory.addItem(lineToAdd)
    # Calling refresh function to clear and renew table view of user
    print("*** Current Directory ***")
    refresh()
    # Notifying user of successful operation
    ui.statusbar.showMessage("Row has been edited.", 2000)


def quizSetup():
    '''
    Function to set DialogButtonBox when 'Quiz' button is clicked.
    '''
    if directory.getSize() < 5:
        ui.statusbar.showMessage("WARNING : Not enough rows to create a test (5 needed).", 3000)
        return None
    else:
        # Clearing screen to prevent cheating
        ui.tableWidget.clearContents()
        ui.tableWidget.setRowCount(0)
        # Writing info on table
        ui.tableWidget.setRowCount(1)
        message = ['Go back to your test', 'or click the refresh', 'button', '*ICON*']
        for x in range(0, 4):
            cell = QtWidgets.QTableWidgetItem()  # Creating QTableWidgetItem
            cell.setText(message[x])  # Adding string to QTableWidgetItem
            ui.tableWidget.setItem(0, x, cell)
        # Changing ok button text
        uiQuiz.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText("Submit")
        # Picking up random directory indexes for test
        v = randint(0, directory.getSize()-1)
        w = randint(0, directory.getSize()-1)
        while w == v:
            w = randint(0, directory.getSize()-1)
        x = randint(0, directory.getSize()-1)
        while x == w or x == v:
            x = randint(0, directory.getSize()-1)
        y = randint(0, directory.getSize()-1)
        while y == x or y == w or y == v:
            y = randint(0, directory.getSize()-1)
        z = randint(0, directory.getSize()-1)
        while z == y or z == x or z == w or z == v:
            z = randint(0, directory.getSize()-1)
        # Setting up first line of test
        uiQuiz.labelEN1.setText(directory.items[v][0])
        uiQuiz.labelES1.setText(directory.items[v][2])
        uiQuiz.labelGER1.setText(directory.items[v][3])
        uiQuiz.labelJAP1.setText(directory.items[v][4])
        # Setting up second line of test
        uiQuiz.labelEN2.setText(directory.items[w][0])
        uiQuiz.labelFR2.setText(directory.items[w][1])
        uiQuiz.labelES2.setText(directory.items[w][2])
        uiQuiz.labelGER2.setText(directory.items[w][3])
        # Setting up third line of test
        uiQuiz.labelFR3.setText(directory.items[x][1])
        uiQuiz.labelES3.setText(directory.items[x][2])
        uiQuiz.labelGER3.setText(directory.items[x][3])
        uiQuiz.labelJAP3.setText(directory.items[x][4])
        # Setting up fourth line of test
        uiQuiz.labelEN4.setText(directory.items[y][0])
        uiQuiz.labelFR4.setText(directory.items[y][1])
        uiQuiz.labelGER4.setText(directory.items[y][3])
        uiQuiz.labelJAP4.setText(directory.items[y][4])
        # Setting up fifth line of test
        uiQuiz.labelEN5.setText(directory.items[z][0])
        uiQuiz.labelFR5.setText(directory.items[z][1])
        uiQuiz.labelES5.setText(directory.items[z][2])
        uiQuiz.labelJAP5.setText(directory.items[z][4])
        # Show window
        quiz.show()


def quizSubmitted():
    '''
    Function to correct test and submit results.
    '''
    # Setting score to 0
    score = 0
    # Getting line1's row in directory in order to check if answer is correct
    one = uiQuiz.labelEN1.text()
    for v in range(0, directory.getSize()):
        if one == directory.items[v][0]:
            line1 = directory.items[v]
    # If answer1 is correct, add 20 to score
    if uiQuiz.lineAnswer1.text().lower() == line1[1].lower():
        print("Answer 1 is correct!")
        score += 20
    else:
        print("Answer 1 is false!")

    # Getting line2's row in directory in order to check if answer is correct
    two = uiQuiz.labelEN2.text()
    for w in range(0, directory.getSize()):
        if two == directory.items[w][0]:
            line2 = directory.items[w]
    # If answer2 is correct, add 20 to score
    if uiQuiz.lineAnswer2.text().lower() == line2[4].lower():
        print("Answer 2 is correct!")
        score += 20
    else:
        print("Answer 2 is false!")

    # Getting line3's row in directory in order to check if answer is correct
    three = uiQuiz.labelFR3.text()
    for x in range(0, directory.getSize()):
        if three == directory.items[x][1]:
            line3 = directory.items[x]
    # If answer3 is correct, add 20 to score
    if uiQuiz.lineAnswer3.text().lower() == line3[0].lower():
        print("Answer 3 is correct!")
        score += 20
    else:
        print("Answer 3 is false!")

    # Getting line4's row in directory in order to check if answer is correct
    four = uiQuiz.labelEN4.text()
    for y in range(0, directory.getSize()):
        if four == directory.items[y][0]:
            line4 = directory.items[y]
    # If answer4 is correct, add 20 to score
    if uiQuiz.lineAnswer4.text().lower() == line4[2].lower():
        print("Answer 4 is correct!")
        score += 20
    else:
        print("Answer 4 is false!")

    # Getting line5's row in directory in order to check if answer is correct
    five = uiQuiz.labelEN5.text()
    for z in range(0, directory.getSize()):
        if five == directory.items[z][0]:
            line5 = directory.items[z]
    # If answer5 is correct, add 20 to score
    if uiQuiz.lineAnswer5.text().lower() == line5[3].lower():
        print("Answer 5 is correct!")
        score += 20
    else:
        print("Answer 5 is false!")

    # Creating MessageBox to display score to user
    resultMessage = QtWidgets.QMessageBox()
    resultMessage.setWindowTitle("Quiz Result")
    print(score)
    if score > 50:
        resultMessage.setText("Good job, you passed the test!\nYour score :  " + str(score) + "/100")
        resultMessage.exec_()
    else:
        resultMessage.setText("Too bad, you failed the test.\nYour score : " + str(score) +
                              "/100")
        resultMessage.exec()
    # Refreshing tableWidget when test is finished.
    refresh()
    # Resetting lineEdit lines of test to ''
    uiQuiz.lineAnswer1.setText('')
    uiQuiz.lineAnswer2.setText('')
    uiQuiz.lineAnswer3.setText('')
    uiQuiz.lineAnswer4.setText('')
    uiQuiz.lineAnswer5.setText('')


def new():
    '''
    Function to clear directory in order create a new directory.
    '''
    directory.clearAll()
    print("*** New Directory ***")
    refresh()


def searchFor():
    '''
    Function to enable searching.
    '''
    directorySearch = Directory()
    research = ui.lineSearch.text()
    length = len(research)
    # If there is no search, refresh directory
    if research == '':
        refresh()
    else:
        # For every item in directory
        for item in enumerate(directory.items):
            for i in range(0, directoryItemSize):
                # If research is found, add item to search directory
                if research.lower() == directory.items[item[0]][i][:length].lower():
                    directorySearch.addItem(directory.items[item[0]])
                    break  # To avoid appending the same line multiple times if multiple words start with "research"
        print('*** Search directory ***')
        print(directorySearch.items)
        # "Refresh()" of directorySearch
        ui.tableWidget.clearContents()  # Clearing table content
        ui.tableWidget.setRowCount(0)  # Reinitializing table to 0 row
        ui.tableWidget.setSortingEnabled(False)  # Stopping sorting while printing table
        for m in range(0, directorySearch.getSize()):
            ui.tableWidget.insertRow(ui.tableWidget.rowCount())  # Add row for every item in directory
            for n in range(0, directoryItemSize):
                cell = QtWidgets.QTableWidgetItem()  # Creating QTableWidgetItem
                cell.setText(directorySearch.items[m][n])  # Adding string to QTableWidgetItem
                ui.tableWidget.setItem(m, n, cell)  # Printing QTableWidgetItem to QWidgetTable
                # Setting background color to let user know he is using the search tool
                ui.tableWidget.item(m, n).setBackground(QtGui.QColor(217, 241, 247))
        ui.tableWidget.setSortingEnabled(True)  # Sorting table
    # End of directorySearch "Refresh()


# CONNECTORS
ui.buttonAdd.clicked.connect(addDialog.show)
uiAdd.buttonBox.accepted.connect(addLine)
ui.buttonDelete.clicked.connect(deleteLine)
ui.buttonExport.clicked.connect(exportData)
ui.buttonImport.clicked.connect(importData)
ui.buttonEdit.clicked.connect(editDialogSetup)
uiEdit.buttonBox.accepted.connect(saveEdit)
ui.buttonQuiz.clicked.connect(quizSetup)
uiQuiz.buttonBox.accepted.connect(quizSubmitted)
uiQuiz.buttonBox.rejected.connect(refresh)
ui.buttonNew.clicked.connect(new)
ui.lineSearch.textChanged.connect(searchFor)
ui.buttonRefresh.clicked.connect(refresh)
# quiz.aboutToQuit.connect(refresh)
# quiz.closeEvent()


mainWindow.show()
sys.exit(app.exec_())
