import sqlite3 as lite
con=lite.connect('RegistrationForm.db')
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMessageBox, QComboBox, QRadioButton

email_update=""

class Window_update(QWidget):
    def __init__(self):
        super().__init__()
        self.title="Update Records"
        self.left=500
        self.top=200
        self.width=500
        self.height=80
        self.Update_WinUI()
    def Update_WinUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        up_label=QLabel("Enter Email ID to Update Data",self)
        up_label.setGeometry(10,20,200,20)
        self.up_box=QLineEdit(self)
        self.up_box.setGeometry(200,17,270,22)
        up_button=QPushButton("Search",self)
        up_button.setGeometry(205,50,100,25)
        up_button.clicked.connect(self.search)
        self.show()
        
    def search(self):
        global email_update
        email_update=self.up_box.text()
        with con:
            cur=con.cursor()
            cur.execute("SELECT * FROM Form WHERE EMAIL='%s'"%email_update)
            rows=cur.fetchall()
            if(len(rows)==0):
                 QMessageBox.question(self,'PROMPT', "Entered Email does not Exist", QMessageBox.Ok)
            else:
                self.win_up2=Update_2()
                self.win_up2.line_mail.setText(email_update)
                for row in rows:
                    self.win_up2.line_user.setText(row[0])
                    self.win_up2.line_pass.setText(row[1])
                    self.win_up2.line_pass2.setText(row[2])
                    if(row[3]=="What is your Name?"):
                        self.win_up2.box_ques.setCurrentIndex(0)
                    elif(row[3]=="What is your favourite Colour?"):
                        self.win_up2.box_ques.setCurrentIndex(1)
                    elif(row[3]=="In which City do you Live?"):
                        self.win_up2.box_ques.setCurrentIndex(2)
                    elif(row[3]=="What is your Nickname?"):
                        self.win_up2.box_ques.setCurrentIndex(3)
                    else:
                        self.win_up2.box_ques.setCurrentIndex(4)
                    self.win_up2.line_hint.setText(row[4])
                    if(row[5]=="Male"):
                        self.win_up2.male_button.setChecked(True)
                    else:
                        self.win_up2.female_button.setChecked(True)
                self.win_up2.show()
                self.close()

                
class Update_2(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Update'
        self.left = 500
        self.top = 200
        self.width = 374
        self.height = 361
        self.Window_2()
    def Window_2(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        heading=QLabel("Update Data",self)
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
        self.line_mail.setReadOnly(True)
        self.line_mail.setToolTip("Email ID cannot be Edited")

        update_button=QPushButton("Update",self)
        update_button.setGeometry(150,300,75,23)

        update_button.clicked.connect(self.up_rec)

    def up_rec(self):
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
                cur.execute("UPDATE Form SET USERNAME='%s', PASSWORD='%s', RETYPE_PASS='%s', HINT_QUES='%s', HINT_PASS='%s', GENDER='%s', EMAIL='%s' WHERE EMAIL='%s'"%(username,password,retype,ques_hint,pass_hint,gen,email,email_update))
                QMessageBox.question(self,'PROMPT', "Updated Successfully", QMessageBox.Ok)
                self.close()
                
if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    ex=Window_update()
    ex1=Update_2()
    sys.exit(app.exec_())

        
