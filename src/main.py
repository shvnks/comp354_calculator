from typing import Callable

import sys
import os
import re 

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Interpreter import Interpreter

COLOR_DARK     = '#191919'
COLOR_MEDIUM   = '#353535'
COLOR_MEDLIGHT = '#5A5A5A'
COLOR_LIGHT    = '#DDDDDD'
COLOR_ACCENT   = '#10a1a1'
COLOR_WRONG    = '#ff0000'

def helpStr():
    return 'Help String'

class CustomListViewItem(QWidget):

    deleteme = pyqtSignal(QListWidgetItem)

    def __init__(self, equation: str, result: str, parent: QListWidget, listItem: QListWidgetItem) -> None:
        super(CustomListViewItem, self).__init__(parent=parent)

        self.listItem = listItem

        self.equationText = QLabel(self)
        self.equationText.setText(equation)
        self.equationText.setSizePolicy(parent.sizePolicy())
        self.equationText.setAlignment(Qt.AlignRight)
        self.equationText.setStyleSheet('border: 1px solid ' + COLOR_MEDLIGHT)
        self.equationText.setTextFormat(Qt.RichText)

        self.deleteButton = QPushButton('X', self)
        self.deleteButton.pressed.connect(self.__deleteButtonPressed)

        self.answerLabel = QLabel(result, self)

        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.deleteButton)
        self.hBox.addStretch()
        self.hBox.addWidget(self.answerLabel)

        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.equationText)
        self.vBox.addItem(self.hBox)

        self.setLayout(self.vBox)

    def __deleteButtonPressed(self):
        self.deleteme.emit(self.listItem)

class HistoryWindow(QWidget):

    setEquationText = pyqtSignal(str)

    def __init__(self, parent: QWidget) -> None:
        super(HistoryWindow, self).__init__()
        
        self.setWindowTitle('ETERNITY History')
        self.setMinimumSize(450, 300)
        self.setSizePolicy(parent.sizePolicy())

        self.equationList = []

        # Restore the geometry of the History window from the settings
        settings = QSettings()
        self.restoreGeometry(settings.value('HistoryWindow/geometry', QByteArray()))

        self.listView = QListWidget(self)
        self.listView.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.listView.itemClicked.connect(self.itemClicked)

        # Get back the list of previous equations saved
        size = settings.beginReadArray('HistoryEquations')
        for i in range(size):
            settings.setArrayIndex(i)
            equation = settings.value('equation')
            answer = settings.value('answer')
            self.equationList.insert(0, (equation, answer))

        self.clearAllButton = QPushButton('Clear All', self)
        self.clearAllButton.pressed.connect(self.__clearAllPressed)

        self.hBox = QHBoxLayout()
        self.hBox.addStretch()
        self.hBox.addWidget(self.clearAllButton)

        label = QLabel('History:')
        label.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)

        self.vBox = QVBoxLayout()
        self.vBox.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.vBox.addWidget(label)
        self.vBox.addWidget(self.listView)
        self.vBox.addItem(self.hBox)

        self.setLayout(self.vBox)

        # Add the equations back to the list view
        for item in reversed(self.equationList):
            self.createNewListItem(item[0], item[1])

    def closeEvent(self, ev: QCloseEvent) -> None:

        settings = QSettings()
        settings.setValue('HistoryWindow/geometry', self.saveGeometry())

        settings.beginWriteArray('HistoryEquations')
        for i in range(len(self.equationList)):
            settings.setArrayIndex(i)
            settings.setValue('equation', self.equationList[i][0])
            settings.setValue('answer', self.equationList[i][1])
        settings.endArray()

        super().closeEvent(ev)

    def __clearAllPressed(self) -> None:
        self.listView.clear()
        self.equationList.clear()

    @pyqtSlot(QListWidgetItem)
    def removeItem(self, item: QListWidgetItem) -> None:
        row = self.listView.row(item)
        self.listView.takeItem(row)
        self.equationList.pop(row)

    def addEquation(self, equation: str, answer: str) -> None:
        self.createNewListItem(equation, answer)
        self.equationList.insert(0, (equation, answer))

    def createNewListItem(self, equation: str, answer: str) -> None:
        listViewItem = QListWidgetItem()
        listViewItem.setFlags(Qt.ItemFlag.NoItemFlags)

        itemWidget = CustomListViewItem(equation, answer, self.listView, listViewItem)
        itemWidget.deleteme.connect(self.removeItem)

        listViewItem.setSizeHint(itemWidget.sizeHint())

        self.listView.insertItem(0, listViewItem)
        self.listView.setItemWidget(listViewItem, itemWidget)

    def itemClicked(self, item: QListWidgetItem) -> None:
        row = self.listView.row(item)
        equation = self.equationList[row][0]
        self.setEquationText.emit(equation)

class ArrayInputDialog(QDialog):
    def __init__(self, title : str, text : str, parent : QWidget = None) -> None:
        super(ArrayInputDialog, self).__init__(parent)

        self.setAttribute(Qt.WidgetAttribute.WA_QuitOnClose)
        self.setWindowTitle(title)

        # match any string composed of comma separated integer of float numbers 
        #self.regEx = r'^(\s*(\d+.\d+|\d+)\,\s*)*(\d+.\d+|\d+)$'
        self.regExVal = QRegExpValidator(QRegExp(r'^(\s*(\d+.\d+|\d+)\,\s*)*(\d+.\d+|\d+)$'))

        self.lineEdit = QLineEdit(self)
        self.lineEdit.textChanged.connect(self.validateText)
        self.lineEdit.setValidator(self.regExVal)

        self.buttonBox = QDialogButtonBox(self)
        self.okButton = self.buttonBox.__addButton('Ok', QDialogButtonBox.ButtonRole.AcceptRole)
        self.cancelButton = self.buttonBox.__addButton('Cancel', QDialogButtonBox.ButtonRole.RejectRole)

        self.vBox = QVBoxLayout()
        self.vBox.addWidget(QLabel(self.tr(text)))
        self.vBox.addWidget(self.lineEdit)
        self.vBox.addWidget(self.buttonBox)
        self.setLayout(self.vBox)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.validateText('')

    def validateText(self, newStr : str) -> None:
        if self.regExVal.validate(newStr, 0)[0] == QValidator.State.Acceptable:
            self.lineEdit.setStyleSheet('border: 1px solid ' + COLOR_MEDLIGHT)
            self.okButton.setDisabled(False)
        else:
            self.lineEdit.setStyleSheet('border: 1px solid ' + COLOR_WRONG)
            self.okButton.setDisabled(True)
        
    def getValue(self) -> str:
        return self.lineEdit.text()

class PushButton(QPushButton):
    def __init__(self, parent=None, text=None) -> None:
        if parent is not None:
            super().__init__(parent)
        else:
            super().__init__()
        
        self.__lbl = QLabel(self)
        if text is not None:
            self.__lbl.setText(text)
        
        self.__lyt = QHBoxLayout()
        self.__lyt.setContentsMargins(0, 0, 0, 0)
        self.__lyt.setSpacing(0)
        self.setLayout(self.__lyt)
        self.__lbl.setAttribute(Qt.WA_TranslucentBackground)
        self.__lbl.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.__lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.__lbl.setTextFormat(Qt.RichText)
        self.__lbl.setAlignment(Qt.AlignCenter)
        self.__lyt.addWidget(self.__lbl)
        return

    def setText(self, text) -> None:
        self.__lbl.setText(text)
        self.updateGeometry()
        return

    def sizeHint(self) -> QSize:
        s = QPushButton.sizeHint(self)
        w = self.__lbl.sizeHint()
        s.setWidth(w.width())
        s.setHeight(w.height())
        return s

class MainWindow(QMainWindow):
    def __init__(self, app, parent=None) -> None:
        super(MainWindow, self).__init__(parent)

        self.cursorPosition = 0
        self.equationString = ''
        self.isDegree = False
        
        self.app = app
        self.history = HistoryWindow(self)
        self.history.setEquationText.connect(self.setEquationText)

        settings = QSettings()
        self.restoreGeometry(settings.value('geometry', QByteArray()))
        self.restoreState(settings.value('state', QByteArray()))

        # Get the light and dark mode stylesheet
        self.lightStylesheet = self.app.styleSheet()
        darkStylesheetFile = QFile(QFileInfo(os.path.realpath(__file__)).absolutePath() + '/darkstyle.qss')
        darkStylesheetFile.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(darkStylesheetFile)
        self.darkStylesheet = stream.readAll()
        
        # Set the style to the previous setting
        if str(settings.value('AppStyle')) == 'light':
            self.app.setStyleSheet(self.lightStylesheet)
        else:
            self.app.setStyleSheet(self.darkStylesheet)

        # Set the minimum window size possible
        self.setMinimumSize(450, 500)
        
        # Create the Layout
        self.mainLayout = QGridLayout()
        self.mainLayout.setObjectName('mainLayout')
        self.mainLayoutWidget = QWidget(self)
        self.mainLayoutWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainLayoutWidget)
        
        # Create the MenuBar
        self.menuBar = QMenuBar(self)

        self.helpMenu = QMenu('H&elp', self.menuBar)
        aboutAction = self.helpMenu.addAction('&About')
        aboutAction.triggered.connect(self.__onAboutActionTriggered)
        helpAction = self.helpMenu.addAction('&Help')
        helpAction.triggered.connect(self.__onHelpActionTriggered)
        
        self.styleMenu = QMenu('&Style', self.menuBar)
        lightStyleAction = self.styleMenu.addAction('&Light')
        lightStyleAction.triggered.connect(self.__onLightStyleActionTriggered)
        darkStyleAction = self.styleMenu.addAction('&Dark')
        darkStyleAction.triggered.connect(self.__onDarkStyleActionTriggered)

        self.menuBar.addMenu(self.styleMenu)
        self.menuBar.addMenu(self.helpMenu)

        historyAction = self.menuBar.addAction('&History')
        historyAction.triggered.connect(self.__onHistoryActionTriggered)

        self.mainLayout.setMenuBar(self.menuBar)
        
        # Create the UI elements
        self.sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Row 0
        row = 0
        self.equationText = QLabel(self)
        self.equationText.setText('_')
        self.equationText.setSizePolicy(self.sizePolicy)
        self.equationText.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.equationText.setStyleSheet('border: 1px solid ' + COLOR_MEDLIGHT)
        self.equationText.setTextFormat(Qt.RichText)
        self.mainLayout.addWidget(self.equationText, row, 0, 1, 5)
        row += 1
        
        self.errorMessageLabel = QLabel(self)
        self.errorMessageLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.mainLayout.addWidget(self.errorMessageLabel, row, 0, 1, 4)
        self.degButton = self.__addButton('RAD', 'DegRad', '', row, 4, slot=self.switchDegRad)
        row += 1

        # Create the buttons
        # Row 1
        self.__addButton('&lt;&lt;', 'leftButton', '', row, 0, slot=self.cursorLeft, shortcut=QKeySequence(Qt.Key_Left))
        self.__addButton('&gt;&gt;', 'rightButton', '', row, 1, slot=self.cursorRight, shortcut=QKeySequence(Qt.Key_Right))
        self.__addButton(u'\u2190', 'backButton', '<-', row, 2, slot=self.backspace, shortcut=QKeySequence(Qt.Key_Backspace))
        self.__addButton('Del', 'deleteButton', '->', row, 3, slot=self.delete, shortcut=QKeySequence(Qt.Key_Delete))
        self.__addButton('AC', 'clearButton', 'AC', row, 4, slot=self.clearText)
        row += 1
        
        # Row 2 
        self.__addButton(u'\U0001D745', 'piButton', u'\U0001D745', row, 0)
        self.__addButton('<i>e</i>', 'eButton', 'e', row, 1, shortcut=QKeySequence('e'))
        self.__addButton('x<sup>2</sup>', 'squareButton', '^2', row, 2)
        self.__addButton('x<sup>3</sup>', 'cubeButton', '^3', row, 3)
        self.__addButton('x<sup>y</sup>', 'expoButton', '^', row, 4, shortcut=QKeySequence('^'))
        row += 1
        
        # Row 3
        self.__addButton('sin(x)', 'sinButton', 'sin()', row, 0)
        self.__addButton('cos(x)', 'cosButton', 'cos()', row, 1)
        self.__addButton('tan(x)', 'tanButton', 'tan()', row, 2)
        self.__addButton('x!', 'factButton', '!', row, 3, shortcut=QKeySequence('!'))
        self.__addButton(u'\u221a', 'Button', 'sqrt()', row, 4)
        row += 1

        # Row 4
        self.__addButton('sin<sup>-1</sup>(x)', 'arcsinButton', 'arcsin()', row, 0)
        self.__addButton('cos<sup>-1</sup>(x)', 'arccosButton', 'arccos()', row, 1)
        self.__addButton('tan<sup>-1</sup>(x)', 'arctanButton', 'arctan()', row, 2)
        self.__addButton('log<sub>b</sub>(x)', 'logButton', 'log()', row, 3)
        self.__addButton(u'\u0393(x)', 'gammaButton', u'\u0393()', row, 4)
        row += 1

        # Row 5
        self.__addButton('sinh(x)', 'sinhButton', 'sinh()', row, 0)
        self.__addButton('cosh(x)', 'coshButton', 'cosh()', row, 1)
        self.__addButton('tanh(x)', 'tanhButton', 'tanh()', row, 2)
        self.__addButton('MAD(x)',  'madButton', 'MAD()', row, 3, slot = lambda: self.addArrayFunctionToEquation('MAD'))
        self.__addButton(u'\u03c3(x)', 'stddevButton', u'\u03c3()', row, 4, slot = lambda: self.addArrayFunctionToEquation('\u03c3'))
        row += 1
        
        # Row 6
        self.vSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.mainLayout.addItem(self.vSpacer, row, 0, 1, 5)
        row += 1
                
        # Row 7
        self.__addButton('1', 'oneButton', '1', row, 0, shortcut=QKeySequence('1'))
        self.__addButton('2', 'twoButton', '2', row, 1, shortcut=QKeySequence('2'))
        self.__addButton('3', 'threeButton', '3', row, 2, shortcut=QKeySequence('3'))
        self.__addButton('(', 'leftParButton', '(', row, 3, shortcut=QKeySequence('('))
        self.__addButton(')', 'rightParButton', ')', row, 4, shortcut=QKeySequence(')'))
        row += 1

        # Row 8
        self.__addButton('4', 'fourButton', '4', row, 0, shortcut=QKeySequence('4'))
        self.__addButton('5', 'fiveButton', '5', row, 1, shortcut=QKeySequence('5'))
        self.__addButton('6', 'sixButton', '6', row, 2, shortcut=QKeySequence('6'))
        self.__addButton(u'\u00d7', 'multButton', '*', row, 3, shortcut=QKeySequence('*'))
        self.__addButton(u'\u00f7', 'divButton', '/', row, 4, shortcut=QKeySequence('/'))
        row += 1

        # Row 
        self.__addButton('7', 'sevenButton', '7', row, 0, shortcut=QKeySequence('7'))
        self.__addButton('8', 'eightButton', '8', row, 1, shortcut=QKeySequence('8'))
        self.__addButton('9', 'nineButton', '9', row, 2, shortcut=QKeySequence('9'))
        self.__addButton('+', 'plusButton', '+', row, 3, shortcut=QKeySequence('+'))
        self.__addButton('-', 'minusButton', '-', row, 4, shortcut=QKeySequence('-'))
        row += 1

        # Row 
        self.__addButton('0', 'zeroButton', '0', row, 0, shortcut=QKeySequence('0'))
        self.__addButton('.', 'dotButton', '.', row, 1, shortcut=QKeySequence('.'))
        self.__addButton('+/-', 'plusminusButton', '-', row, 2)
        self.equalButton = self.__addButton('=', 'equalButton', '=', row, 3, 1, 2, slot=self.compute, shortcut=QKeySequence('='))
        row += 1
        
    # overwrite close event
    def closeEvent(self, ev: QCloseEvent) -> None:
        self.history.close()

        settings = QSettings()
        settings.setValue('geometry', self.saveGeometry())
        settings.setValue('state', self.saveState())
        
        super().closeEvent(ev)

    # add a button to the layout
    def __addButton(self, text: str, name: str, equation: str, row: int, col: int, rowSpan: int = 1, colSpan: int = 1, slot: Callable = None, shortcut: QKeySequence = None) -> QPushButton:
        
        # create the button object
        newButton = PushButton(self, text)
        newButton.setObjectName(name)
        newButton.setSizePolicy(self.sizePolicy)
        
        # if a function is not passed as the action, create a defaut action of what to do
        if slot == None:
            slot = lambda: self.addTextToEquation(equation)
        
        # attach the function to when the button is pressed
        newButton.pressed.connect(slot)
        
        # if a shortcut is set, assign it to the button
        if shortcut != None:
            newButton.setShortcut(shortcut)
        
        # add the button to the given position in the layout
        self.mainLayout.addWidget(newButton, row, col, rowSpan, colSpan)
        
        return newButton
        
    # menu->about shown
    def __onAboutActionTriggered(self) -> None:
        msb = QMessageBox(self)
        msb.setWindowTitle('About')
        msb.setText('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce sollicitudin dui pulvinar ante rutrum pretium et non dolor. Quisque pretium sodales nulla, non dapibus magna mollis quis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Maecenas id sodales felis. Mauris nec finibus orci, et vehicula sapien. Cras id nibh mauris. Praesent nec ante vel diam molestie dictum ut in augue. Suspendisse consectetur lacus non odio faucibus tempus. Proin quis eros sodales, condimentum leo non, blandit turpis. Nullam suscipit semper malesuada. Donec massa orci, fermentum ac dignissim sit amet, iaculis sed magna. Nulla ullamcorper efficitur dui, sit amet consequat ligula.')
        msb.setStandardButtons(QMessageBox.Ok)
        msb.exec_()
        
    # menu->help shown
    def __onHelpActionTriggered(self) -> None:
        msb = QMessageBox(self)
        msb.setWindowTitle('Help')
        msb.setText(helpStr())
        msb.setStandardButtons(QMessageBox.Ok)
        msb.exec_()
        
    def __onLightStyleActionTriggered(self) -> None:
        self.app.setStyleSheet(self.lightStylesheet)
        settings = QSettings()
        settings.setValue('AppStyle', 'light')

    def __onDarkStyleActionTriggered(self) -> None:
        self.app.setStyleSheet(self.darkStylesheet)
        settings = QSettings()
        settings.setValue('AppStyle', 'dark')
    
    def __onHistoryActionTriggered(self) -> None:
        self.history.show()

    # overwrite mouse presses
    def mousePressEvent(self, event: QMouseEvent) -> None:
            # ignore mouse presses on the main window itself so that focus is not lost
            event.ignore()
            return

    # check wether the equation is valid or not
    def validateEquation(self) -> None:
    
        valid, error = Interpreter(self.equationString).isValid()
        if valid:
            self.equationText.setStyleSheet('border: 1px solid ' + COLOR_MEDLIGHT)
            self.equalButton.setEnabled(True)
        else:
            self.equationText.setStyleSheet('border: 1px solid ' + COLOR_WRONG)
            self.equalButton.setEnabled(False)
        
    # add element to the equation
    def addTextToEquation(self, functionStr: str) -> None:

        # add the string to the current location of the cursor
        self.equationString = self.equationString[:self.cursorPosition] + functionStr + self.equationString[self.cursorPosition:]
        
        # calculate the new cursor position
        self.cursorPosition += len(functionStr)
        
        # if the parameter is a function, sets the cursor to inside the parenthesis
        if len(functionStr) > 1 and functionStr[-1] == ')':
            self.cursorPosition -= 1
        
        #update the equation shown
        self.writeEquation()

    def addArrayFunctionToEquation(self, functionStr: str) -> None:
        
        #arrayInput = QInputDialog.getText(self, 'Input values', 'Enter a list of numbers, separated by commas:', inputMethodHints=Qt.ImhFormattedNumbersOnly)[0]
        arrayInput = ArrayInputDialog('Input values', 'Enter a list of numbers, separated by commas:', self)
        if arrayInput.exec():
            arrayInputValues = arrayInput.getValue().strip()
            self.addTextToEquation(functionStr + '(' + arrayInputValues + ')')

    def switchDegRad(self) -> None:
        if self.isDegree:
            self.degButton.setText('RAD')
        else:
            self.degButton.setText('DEG')
        self.isDegree = not self.isDegree

    # move the cursor 1 step to the left
    def cursorLeft(self) -> None:
        self.cursorPosition -= 1
        if self.cursorPosition < 0:
            self.cursorPosition = 0
        self.writeEquation()
        
    # move the cursor 1 step to the right
    def cursorRight(self) -> None:
        self.cursorPosition += 1
        if self.cursorPosition > len(self.equationString):
            self.cursorPosition = len(self.equationString)
        self.writeEquation()
    
    # write the equation to the label, adding the cursor to the correct location
    def writeEquation(self) -> None:

        # Remove error message
        self.errorMessageLabel.setText('')

        # write a _ character under the cursor position
        if self.cursorPosition == len(self.equationString):
            tmpStr = self.equationString + '_'
        else:
            tmpStr = self.equationString[:self.cursorPosition] + '<u>' + self.equationString[self.cursorPosition] + '</u>' + self.equationString[self.cursorPosition+1:]

        self.equationText.setText(tmpStr)
        self.validateEquation()
        
    # remove the character before the cursor position
    def backspace(self) -> None:
        back = self.cursorPosition - 1
        if back < 0:
            back = 0
        self.equationString = self.equationString[:back] + self.equationString[self.cursorPosition:]
        self.cursorLeft()
        self.writeEquation()
        
    # remove the character on the cursor position
    def delete(self) -> None:
        front = self.cursorPosition + 1
        if front > len(self.equationString):
            front = len(self.equationString)
        self.equationString = self.equationString[:self.cursorPosition] + self.equationString[front:]
        self.writeEquation()

    # clear the equation
    def clearText(self) -> None:
        self.equationText.setText('_')
        self.equationString = ''
        self.cursorPosition = 0
        
    # computer the equation
    def compute(self) -> None:

        answer, valid, error = Interpreter(self.equationString).evaluateEquation()
        if valid:
            self.history.addEquation(self.equationString, str(answer))
            self.clearText()
            self.addTextToEquation(str(answer))
        else:
            self.errorMessageLabel.setText(error)

    def setEquationText(self, equation: str) -> None:
        self.clearText()
        self.addTextToEquation(equation)
        
def main(argv):

    app = QApplication(argv)
    app.setOrganizationName('comp354')
    app.setApplicationName('ETERNITY')

    # increase the foot size
    font = app.font()
    font.setPixelSize(22)
    app.setFont(font)
    
    # create the main window
    window = MainWindow(app)
    window.setWindowTitle('ETERNITY Calculator')
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)