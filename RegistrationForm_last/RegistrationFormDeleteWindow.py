import sqlite3 as lite
con=lite.connect('RegistrationForm.db')
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMessageBox

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title="Delete"
        self.left=500
        self.top=200
        self.width=500
        self.height=80
        self.WindowUI()
    def WindowUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        del_label=QLabel("Enter Email ID to Delete Data",self)
        del_label.setGeometry(10,20,200,10)
        self.del_box=QLineEdit(self)
        self.del_box.setGeometry(200,17,270,22)
        del_button=QPushButton("Delete Data",self)
        del_button.setGeometry(205,50,100,25)
        del_button.clicked.connect(self.del_data)
        self.show()
    def del_data(self):
        email_delete=self.del_box.text()
        with con:
            cur=con.cursor()
            cur.execute("SELECT * FROM Form WHERE EMAIL='%s'"%email_delete)
            rows=cur.fetchall()
            if(len(rows)==0):
                 QMessageBox.question(self,'PROMPT', "Entered Email does not Exist", QMessageBox.Ok)
            else:
                confirm=QMessageBox.question(self,'PROMPT', "Entered Email will be Deleted. Do you want to Continue?", QMessageBox.Yes,QMessageBox.No)
                if(confirm==QMessageBox.Yes):
                    cur.execute("DELETE FROM Form WHERE EMAIL='%s'"%email_delete)
                    QMessageBox.question(self,'PROMPT', "Record Deleted", QMessageBox.Ok)
                    self.close()
                else:
                    pass
                    

if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    ex=Window()
    sys.exit(app.exec_())
