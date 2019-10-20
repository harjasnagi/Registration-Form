import sqlite3 as lite
con=lite.connect('RegistrationForm.db')

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout

class Window_show(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Show All Records"
        self.left = 0
        self.top = 0
        self.width = 750
        self.height = 670
        self.ShowUI()
    def ShowUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.createTable()
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout)
        
        self.show()    
    def createTable(self):
        with con:
            cur=con.cursor()
            cur.execute("SELECT * FROM Form")
            rows=cur.fetchall()
            if(len(rows)==0):
                QMessageBox.question(self,'PROMPT', "There is No Data in the Database", QMessageBox.Ok)
            else:
                self.tableWidget = QTableWidget()
                self.tableWidget.setRowCount(len(rows)+1)
                self.tableWidget.setColumnCount(7)
                self.tableWidget.setItem(0,0, QTableWidgetItem("Username"))
                self.tableWidget.setItem(0,1, QTableWidgetItem("Password"))
                self.tableWidget.setItem(0,2, QTableWidgetItem("Retype Password"))
                self.tableWidget.setItem(0,3, QTableWidgetItem("Hint Question"))
                self.tableWidget.setItem(0,4, QTableWidgetItem("Hint Password"))
                self.tableWidget.setItem(0,5, QTableWidgetItem("Gender"))
                self.tableWidget.setItem(0,6, QTableWidgetItem("Email ID"))
                self.tableWidget.move(0,0)
                for row_no, row_data in enumerate(rows,1):
                    for col_no,data in enumerate(row_data):
                        self.tableWidget.setItem(row_no,col_no,QTableWidgetItem(str(data)))
                 
            
        
if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    ex=Window_show()
    sys.exit(app.exec_())
