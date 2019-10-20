import sqlite3 as lite
con=lite.connect('RegistrationForm.db')
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMessageBox, QComboBox, QRadioButton
from RegistrationFormDeleteWindow import *
from RegistrationFormShowAllWindow import *
from RegistrationFormUpdateWindow import *

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


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Registration Form'
        self.left = 500
        self.top = 200
        self.width = 374
        self.height = 361
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
        register.setGeometry(0,300,75,23)

        rec_delete=QPushButton("Delete",self)
        rec_delete.setGeometry(90,300,75,23)

        showall=QPushButton("Show All Records",self)
        showall.setGeometry(180,300,100,23)

        update=QPushButton("Update",self)
        update.setGeometry(298,300,75,23)

        update.clicked.connect(self.update_rec)

        register.clicked.connect(self.signup)

        rec_delete.clicked.connect(self.delete)
        
        showall.clicked.connect(self.show_all)
        
        self.show()


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

    def delete(self):
        self.win=Window()
        self.win.show()

    def show_all(self):
        self.win_show=Window_show()
        self.win_show.show()

    def update_rec(self):
        self.win_up=Window_update()
        self.win_up.show()
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
