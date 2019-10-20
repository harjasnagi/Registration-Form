import sqlite3 as lite
con=lite.connect('RegistrationForm.db')
try:
    con.execute('''CREATE TABLE Form
        (USERNAME          VARCHAR(50),
        PASSWORD           VARCHAR(50),
        RETYPE_PASS        VARCHAR(100),     
        HINT_QUES          VARCHAR(50),
        HINT_PASS          VARCHAR(30),
        GENDER             VARCHAR(6),
        EMAIL              VARCHAR(50) PRIMARY KEY);''')
except lite.OperationalError:
    pass

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMessageBox, QComboBox, QRadioButton,QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
    
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Registration Form'
        self.left = 500
        self.top = 200
        self.width = 390
        self.height = 400
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        heading=QLabel("Registration Form",self)
        heading.setGeometry(150,20,90,13)
        
        username=QLabel("Username",self)
        username.setGeometry(60,50,50,13)
        
        password=QLabel("Password",self)
        password.setGeometry(60,80,47,13)
        
        re_pass=QLabel("Retype Password",self)
        re_pass.setGeometry(42,110,90,13)
        
        hint_ques=QLabel("Hint Question",self)
        hint_ques.setGeometry(49,140,70,13)
        
        hint_pass=QLabel("Hint Password",self)
        hint_pass.setGeometry(48,180,70,13)
        
        gender=QLabel("Gender",self)
        gender.setGeometry(60,220,40,13)
        
        mail=QLabel("Email ID",self)
        mail.setGeometry(60,250,47,13)


        self.line_user=QLineEdit(self)
        self.line_user.setGeometry(160,50,190,20)
        
        self.line_pass=QLineEdit(self)
        self.line_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_pass.setGeometry(160,80,190,20)
        
        self.line_pass2=QLineEdit(self)
        self.line_pass2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_pass2.setGeometry(160,110,190,20)
        
        self.box_ques=QComboBox(self)
        self.box_ques.setGeometry(160,140,190,22)
        self.box_ques.addItem("What is your Name?")
        self.box_ques.addItem("What is your favourite Colour?")
        self.box_ques.addItem("In which City do you Live?")
        self.box_ques.addItem("What is your Nickname?")
        self.box_ques.addItem("Which Car do you Own?")
        
        self.line_hint=QLineEdit(self)
        self.line_hint.setGeometry(160,180,190,20)
        self.line_hint.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.male_button=QRadioButton("Male",self)
        self.male_button.setGeometry(160,220,51,17)
        
        self.female_button=QRadioButton("Female",self)
        self.female_button.setGeometry(270,220,60,17)
        
        self.line_mail=QLineEdit(self)
        self.line_mail.setGeometry(160,250,190,20)

        register=QPushButton("Register",self)
        register.setGeometry(65,300,75,23)

        delete = QPushButton("Delete",self)
        delete.setGeometry(165,300,75,23)

        showall=QPushButton("Show All",self)
        showall.setGeometry(265,300,75,23)

        update=QPushButton("Update",self)
        update.setGeometry(65,350,75,23)
        
        register.clicked.connect(self.signup)
        register.setToolTip('Click to register details.')
        self.show()
        
        delete.clicked.connect(self.onClick)
        delete.setToolTip('Click to delete details.')
        self.show()

        update.clicked.connect(self.update_func)
        update.setToolTip('Click to update details.')
        self.show()


        showall.clicked.connect(self.on_click)
        showall.setToolTip('Click to see all details.')
        self.show()

    @pyqtSlot()

    def update_func(self):
        self.SW = update_class()
        self.SW.show()

    def on_click(self):
        self.SW = showclass()
        self.SW.show()
    
    def onClick(self):
        self.SW = deleted()
        self.SW.show()
        
    def signup(self):
        username=self.line_user.text()
        password=self.line_pass.text()
        retype=self.line_pass2.text()
        ques_hint=self.box_ques.currentText()
        pass_hint=self.line_hint.text()
        if (self.male_button.isChecked()):
            gen="Male"
        else:
            gen="Female"
        email=self.line_mail.text()
        if(password!=retype):
            QMessageBox.question(self,'PROMPT', "Passwords donot Match", QMessageBox.Ok)
            self.show()
        if(password==retype):
            with con:
                cur=con.cursor()
                cur.execute("SELECT EMAIL FROM Form WHERE EMAIL='%s'"%email)
                rows=cur.fetchone()
                if(rows!=None):
                    QMessageBox.question(self,'PROMPT', "This Email Address is already Occupied. Please select a different Email Address", QMessageBox.Ok)
        if(password==retype and rows==None):
            with con:
                cur=con.cursor()
                cur.execute("INSERT INTO Form Values('%s','%s','%s','%s','%s','%s','%s')"%(username,password,retype,ques_hint,pass_hint,gen,email))
                QMessageBox.question(self,'PROMPT', "Registered Successfully", QMessageBox.Ok)

class deleted(QMainWindow):     #####################################################################################
    def __init__(self):
        super(deleted,self).__init__()
        self.setWindowTitle('Deleting Record')
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 120
        self.setGeometry(self.left,self.top,self.width,self.height)

        email=QLabel("Enter EMAIL:",self)
        email.setGeometry(20,20,190,20)
        self.email=QLineEdit(self)
        self.email.setGeometry(130,20,250,30)

        delete2 = QPushButton("Delete",self)
        delete2.setGeometry(160,80,80,30)

        delete2.clicked.connect(self.onClick2)
        self.show()

    @pyqtSlot()

    def onClick2(self):
        email_del = self.email.text()
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Form WHERE EMAIL='%s'"%email_del)
            rows=cur.fetchall()
            if(len(rows)==0):
                QMessageBox.question(self,'PROMPT',"Entered Email not in existance",QMessageBox.Ok)
            else:
                cur.execute("DELETE FROM Form WHERE EMAIL='%s'"%email_del)
                QMessageBox.question(self,'PROMPT',"Record deleted",QMessageBox.Ok)

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class showclass(QWidget):   ##############################################################################################

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 300
        self.top = 200
        self.width = 800
        self.height = 350
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 

        # Show widget
        self.show()

    def createTable(self):
       # Create table
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Form")
            rows=cur.fetchall()
            if(len(rows)==0):
                QMessageBox.question(self,'PROMPT',"No Records",QMessageBox.Ok)
            else:
                self.tableWidget = QTableWidget()
                self.tableWidget.setRowCount(len(rows)+1
                                             )
                self.tableWidget.setColumnCount(7)
                self.tableWidget.setItem(0,0, QTableWidgetItem("Username"))
                self.tableWidget.setItem(0,1, QTableWidgetItem("Pass"))
                self.tableWidget.setItem(0,2, QTableWidgetItem("Re-Pass"))
                self.tableWidget.setItem(0,3, QTableWidgetItem("Hint Q"))
                self.tableWidget.setItem(0,4, QTableWidgetItem("Hint P"))
                self.tableWidget.setItem(0,5, QTableWidgetItem("Gender"))
                self.tableWidget.setItem(0,6, QTableWidgetItem("Email"))
                self.tableWidget.move(0,0)
                
                for row_no, row_data in enumerate(rows,1):
                    #self.tableWidget.insertRow(row_no)
                    for col_no,data in enumerate(row_data):
                        self.tableWidget.setItem(row_no,col_no,QtWidgets.QTableWidgetItem(str(data)))

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
 

class update_class(QWidget):                ##################################################################################
    def __init__(self):
        super(update_class,self).__init__()
        self.setWindowTitle('Update Record')
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 120
        self.setGeometry(self.left,self.top,self.width,self.height)

        email=QLabel("Enter EMAIL:",self)
        email.setGeometry(20,20,190,20)
        self.email=QLineEdit(self)
        self.email.setGeometry(130,20,250,30)

        search = QPushButton("Search",self)
        search.setGeometry(160,80,80,30)

        search.clicked.connect(self.search)
        self.show()

    @pyqtSlot()

    def search(self):
        email_search = self.email.text()   #############    ############              ################      ##############
        flag = email_search
        print("Outside")
        need()
        def need(self):
            print("Before")
            print(flag)

        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Form WHERE EMAIL='%s'"%email_search)
            rows=cur.fetchall()
            if(len(rows)==0):
                QMessageBox.question(self,'PROMPT',"Email does not EXIST",QMessageBox.Ok)
            else:
                ans=QMessageBox.question(self,'PROMPT',"Email Found,Update?",QMessageBox.Yes,QMessageBox.No)
                #ans = QMessageBox.Yes
                if(ans == QMessageBox.Yes):
                    print("HEREEE")
                    self.mid_func()
                #QMessageBox.question(self,'PROMPT',"Record deleted",QMessageBox.Ok)

    def mid_func(self):
        print("Mid")
        self.SW = new()
        self.SW.show()
#print(flag)
class new(QMainWindow):     ####################################################################################################
    def __init__(self):
        super().__init__()
        self.title = 'Updating...'
        self.left = 500
        self.top = 200
        self.width = 390
        self.height = 400
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        heading=QLabel("Registration Form",self)
        heading.setGeometry(150,20,90,13)
        with con:
            cur = con.cursor()
            print("Start")
            #cur.execute("SELECT * FROM Form WHERE EMAIL='%s'"%flag)
            print("Fetching,")

            rows=cur.fetchall()
            for row in rows:
                print("Username =", row[0])
                print("Password =", row[1])
                print("ReTyped =",row[2])
                print("Hint Question =",row[3])
                print("Hint Answer =",row[4])
                print("Gender =", row[5])
                print("Email =", row[6])
                
        username=QLabel("Username",self)
        username.setGeometry(60,50,50,13)
        
        password=QLabel("Password",self)
        password.setGeometry(60,80,47,13)
        
        re_pass=QLabel("Retype Password",self)
        re_pass.setGeometry(42,110,90,13)
        
        hint_ques=QLabel("Hint Question",self)
        hint_ques.setGeometry(49,140,70,13)
        
        hint_pass=QLabel("Hint Password",self)
        hint_pass.setGeometry(48,180,70,13)
        
        gender=QLabel("Gender",self)
        gender.setGeometry(60,220,40,13)
        
        mail=QLabel("Email ID",self)
        mail.setGeometry(60,250,47,13)

        self.line_user=QLineEdit(self)
        self.line_user.setGeometry(160,50,190,20)
        #self.line_user="HELLO"
        
        self.line_pass=QLineEdit(self)
        self.line_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_pass.setGeometry(160,80,190,20)
        
        self.line_pass2=QLineEdit(self)
        self.line_pass2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_pass2.setGeometry(160,110,190,20)
        
        self.box_ques=QComboBox(self)
        self.box_ques.setGeometry(160,140,190,22)
        self.box_ques.addItem("What is your Name?")
        self.box_ques.addItem("What is your favourite Colour?")
        self.box_ques.addItem("In which City do you Live?")
        self.box_ques.addItem("What is your Nickname?")
        self.box_ques.addItem("Which Car do you Own?")
        
        self.line_hint=QLineEdit(self)
        self.line_hint.setGeometry(160,180,190,20)
        self.line_hint.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.male_button=QRadioButton("Male",self)
        self.male_button.setGeometry(160,220,51,17)
        
        self.female_button=QRadioButton("Female",self)
        self.female_button.setGeometry(270,220,60,17)
        
        self.line_mail=QLineEdit(self)
        self.line_mail.setGeometry(160,250,190,20)

        update_done=QPushButton("Update",self)
        update_done.setGeometry(120,300,75,23)



        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())  
