import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

COLOR_DARK     = '#191919'
COLOR_MEDIUM   = '#353535'
COLOR_MEDLIGHT = '#5A5A5A'
COLOR_LIGHT    = '#DDDDDD'
COLOR_ACCENT   = '#10a1a1'
COLOR_WRONG    = '#ff0000'

def helpStr():
  return 'Help String'

class PushButton(QPushButton):
  def __init__(self, parent=None, text=None):
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

  def setText(self, text):
    self.__lbl.setText(text)
    self.updateGeometry()
    return

  def sizeHint(self):
    s = QPushButton.sizeHint(self)
    w = self.__lbl.sizeHint()
    s.setWidth(w.width())
    s.setHeight(w.height())
    return s

class MainWindow(QWidget):
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)

    self.cursorPosition = 0
    self.equationString = ''
    
    # Set the minimum window size possible
    self.setMinimumSize(QSize(450, 500))
    
    # Create the Layout
    self.mainLayout = QGridLayout(self)
    self.mainLayout.setObjectName('mainLayout')
    self.setLayout(self.mainLayout)
    
    # Create the MenuBar
    self.menuBar = QMenuBar(self)
    self.helpMenu = QMenu('Help')
    aboutAction = self.helpMenu.addAction('About')
    aboutAction.triggered.connect(self.on_aboutAction_triggered)
    helpAction = self.helpMenu.addAction('Help')
    helpAction.triggered.connect(self.on_helpAction_triggered)
    
    self.menuBar.addMenu(self.helpMenu)
    self.mainLayout.setMenuBar(self.menuBar)
    
    # Create the UI elements
    self.sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    
    # Row 0
    self.equationText = QLabel(self)
    self.equationText.setText('_')
    self.equationText.setSizePolicy(self.sizePolicy)
    self.equationText.setAlignment(Qt.AlignRight)
    self.equationText.setStyleSheet('border: 1px solid ' + COLOR_MEDLIGHT)
    self.equationText.setTextFormat(Qt.RichText)
    self.mainLayout.addWidget(self.equationText, 0, 0, 1, 5)
    
    # Create the buttons
    # Row 1
    self.addButton('&lt;&lt;', 'leftButton', '', 1, 0, slot=self.cursorLeft, shortcut=QKeySequence(Qt.Key_Left))
    self.addButton('&gt;&gt;', 'rightButton', '', 1, 1, slot=self.cursorRight, shortcut=QKeySequence(Qt.Key_Right))
    self.addButton(u'\u2190', 'backButton', '<-', 1, 2, slot=self.backspace, shortcut=QKeySequence(Qt.Key_Backspace))
    self.addButton('Del', 'deleteButton', '->', 1, 3, slot=self.delete, shortcut=QKeySequence(Qt.Key_Delete))
    self.addButton('AC', 'clearButton', 'AC', 1, 4, slot=self.clearText)
    
    # Row 2
    self.addButton(u'\u03c0', 'piButton', '3.14159', 2, 0)
    self.addButton('e', 'eButton', '2.71828', 2, 1, shortcut=QKeySequence('e'))
    self.addButton('x<sup>2</sup>', 'squareButton', '^2', 2, 2)
    self.addButton('x<sup>3</sup>', 'cubeButton', '^3', 2, 3)
    self.addButton('x<sup>y</sup>', 'expoButton', '^', 2, 4, shortcut=QKeySequence('^'))
    
    # Row 3
    self.addButton('sin(x)', 'sinButton', 'sin()', 3, 0)
    self.addButton('cos(x)', 'cosButton', 'cos()', 3, 1)
    self.addButton('tan(x)', 'tanButton', 'tan()', 3, 2)
    self.addButton('x!', 'factButton', '!', 3, 3, shortcut=QKeySequence('!'))
    self.addButton(u'\u221a', 'Button', 'sqrt()', 3, 4)

    # Row 4
    self.addButton('sin<sup>-1</sup>(x)', 'arcsinButton', 'arcsin()', 4, 0)
    self.addButton('cos<sup>-1</sup>(x)', 'arccosButton', 'arccos()', 4, 1)
    self.addButton('tan<sup>-1</sup>(x)', 'arctanButton', 'arctan()', 4, 2)
    self.addButton('log<sub>b</sub>(x)', 'logButton', 'log()', 4, 3)
    self.addButton(u'\u0393(x)', 'gammaButton', u'\u0393()', 4, 4)

    # Row 5
    self.addButton('sinh(x)', 'sinhButton', 'sinh()', 5, 0)
    self.addButton('cosh(x)', 'coshButton', 'cosh()', 5, 1)
    self.addButton('tanh(x)', 'tanhButton', 'tanh()', 5, 2)
    self.addButton('MAD(x)',  'madButton', 'MAD()', 5, 3)
    self.addButton(u'\u03c3(x)', 'stddevButton', u'\u03c3()', 5, 4)
    
    #Row 6
    self.vSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
    self.mainLayout.addItem(self.vSpacer, 6, 0, 1, 5)
        
    self.addButton('1', 'oneButton', '1', 7, 0, shortcut=QKeySequence('1'))
    self.addButton('2', 'twoButton', '2', 7, 1, shortcut=QKeySequence('2'))
    self.addButton('3', 'threeButton', '3', 7, 2, shortcut=QKeySequence('3'))
    self.addButton('4', 'fourButton', '4', 8, 0, shortcut=QKeySequence('4'))
    self.addButton('5', 'fiveButton', '5', 8, 1, shortcut=QKeySequence('5'))
    self.addButton('6', 'sixButton', '6', 8, 2, shortcut=QKeySequence('6'))
    self.addButton('7', 'sevenButton', '7', 9, 0, shortcut=QKeySequence('7'))
    self.addButton('8', 'eightButton', '8', 9, 1, shortcut=QKeySequence('8'))
    self.addButton('9', 'nineButton', '9', 9, 2, shortcut=QKeySequence('9'))
    self.addButton('0', 'zeroButton', '0', 10, 0, shortcut=QKeySequence('0'))
    self.addButton('.', 'dotButton', '.', 10, 1, shortcut=QKeySequence('.'))
    self.addButton('+/-', 'plusminusButton', '-', 10, 2)
    
    self.addButton('(', 'leftParButton', '(', 7, 3, shortcut=QKeySequence('('))
    self.addButton(')', 'rightParButton', ')', 7, 4, shortcut=QKeySequence(')'))
    self.addButton(u'\u00d7', 'multButton', '*', 8, 3, shortcut=QKeySequence('*'))
    self.addButton(u'\u00f7', 'divButton', '/', 8, 4, shortcut=QKeySequence('/'))
    self.addButton('+', 'plusButton', '+', 9, 3, shortcut=QKeySequence('+'))
    self.addButton('-', 'minusButton', '-', 9, 4, shortcut=QKeySequence('-'))
    self.equalButton = self.addButton('=', 'equalButton', '=', 10, 3, 1, 2, slot=self.compute, shortcut=QKeySequence('='))
    
  # add a button to the layout
  def addButton(self, text, name, equation, row, col, rowSpan = 1, colSpan = 1, slot = None, shortcut = None):
    
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
  def on_aboutAction_triggered(self):
    msb = QMessageBox(self)
    msb.setWindowTitle('About')
    msb.setText('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce sollicitudin dui pulvinar ante rutrum pretium et non dolor. Quisque pretium sodales nulla, non dapibus magna mollis quis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Maecenas id sodales felis. Mauris nec finibus orci, et vehicula sapien. Cras id nibh mauris. Praesent nec ante vel diam molestie dictum ut in augue. Suspendisse consectetur lacus non odio faucibus tempus. Proin quis eros sodales, condimentum leo non, blandit turpis. Nullam suscipit semper malesuada. Donec massa orci, fermentum ac dignissim sit amet, iaculis sed magna. Nulla ullamcorper efficitur dui, sit amet consequat ligula.')
    msb.setStandardButtons(QMessageBox.Ok)
    msb.exec_()
    
  # menu->help shown
  def on_helpAction_triggered(self):
    msb = QMessageBox(self)
    msb.setWindowTitle('Help')
    msb.setText(helpStr())
    msb.setStandardButtons(QMessageBox.Ok)
    msb.exec_()
    
  # handle mouse presses
  def mousePressEvent(self, event: QMouseEvent) -> None:
      # ignore mouse presses on the main window itself so that focus is not lost
      event.ignore()
      return

  # check wether the equation is valid or not
  def validateEquation(self):
  
    #TODO: get whether the equation is valid or not from the equation evaluator
    if True:
      self.equationText.setStyleSheet('border: 1px solid ' + COLOR_WRONG)
      self.equalButton.setEnabled(False)
    else:
      self.equationText.setStyleSheet('border: 1px solid ' + COLOR_MEDLIGHT)
      self.equalButton.setEnabled(True)
    
  # add element to the equation
  def addTextToEquation(self, str):

    # add the string to the current location of the cursor
    self.equationString = self.equationString[:self.cursorPosition] + str + self.equationString[self.cursorPosition:]
    
    # calculate the new cursor position
    self.cursorPosition += len(str)
    
    # if the parameter is a function, sets the cursor to inside the parenthesis
    if len(str) > 1 and str[-1] == ')':
      self.cursorPosition -= 1
    
    #update the equation shown
    self.writeEquation()
    
  # move the cursor 1 step to the left
  def cursorLeft(self):
    self.cursorPosition -= 1
    if self.cursorPosition < 0:
      self.cursorPosition = 0
    self.writeEquation()
    
  # move the cursor 1 step to the right
  def cursorRight(self):
    self.cursorPosition += 1
    if self.cursorPosition > len(self.equationString):
      self.cursorPosition = len(self.equationString)
    self.writeEquation()
  
  # write the equation to the label, adding the cursor to the correct location
  def writeEquation(self):

    # write a _ character under the cursor position
    if self.cursorPosition == len(self.equationString):
      tmpStr = self.equationString + '_'
    else:
      tmpStr = self.equationString[:self.cursorPosition] + '<u>' + self.equationString[self.cursorPosition] + '</u>' + self.equationString[self.cursorPosition+1:]

    self.equationText.setText(tmpStr)
    self.validateEquation()
    
  # remove the character before the cursor position
  def backspace(self):
    back = self.cursorPosition - 1
    if back < 0:
      back = 0
    self.equationString = self.equationString[:back] + self.equationString[self.cursorPosition:]
    self.cursorLeft()
    self.writeEquation()
    
  # remove the character on the cursor position
  def delete(self):
    front = self.cursorPosition + 1
    if front > len(self.equationString):
      front = len(self.equationString)
    self.equationString = self.equationString[:self.cursorPosition] + self.equationString[front:]
    self.writeEquation()

  # clear the equation
  def clearText(self):
    self.equationText.setText('_')
    self.equationString = ''
    self.cursorPosition = 0
    
  # computer the equation
  def compute(self):
    tmp = QMessageBox(self)
    tmp.setWindowTitle('Equation')
    tmp.setText(self.equationText.text())
    tmp.setStandardButtons(QMessageBox.Ok)
    self.clearText()
    tmp.exec_()
    
def main(argv):

  #TODO: if command line equation argument, dont show the UI, and process the equation

  app = QApplication(argv)

  # get the stylesheet for dark mode
  stylesheet = QFile(QFileInfo(os.path.realpath(__file__)).absolutePath() + '/darkstyle.qss')
  stylesheet.open(QFile.ReadOnly | QFile.Text)
  stream = QTextStream(stylesheet)
  app.setStyleSheet(stream.readAll())
  
  # increase the foot size
  font = app.font()
  font.setPixelSize(22)
  app.setFont(font)
  
  # create the main window
  window = MainWindow()
  window.setWindowTitle('ETERNITY Calculator')
  window.show()

  sys.exit(app.exec_())


if __name__ == '__main__':
  main(sys.argv)