import sys
from Evalu import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtSql
import sqlite3
from pprint import pprint

class MainWindow_EXEC():
    
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
            
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)   
        #-------------------------- 
        
        self.create_DB()
        self.ui.pushButton.clicked.connect(self.print_data)
        self.model = None
        self.ui.pushButton.clicked.connect(self.sql_tableview_model)
        self.ui.pushButton_2.clicked.connect(self.sql_add_row)
        self.ui.pushButton_3.clicked.connect(self.sql_delete_row)
        
        
        #-------------------------- 
        
        self.MainWindow.show()
        sys.exit(app.exec_()) 
        
    #----------------------------------------------------------
    def sql_delete_row(self):
        if self.model:
            self.model.removeRow(self.ui.tableView.currentIndex().row())
        else:
            self.sql_tableview_model()       
                
    #----------------------------------------------------------
    def sql_add_row(self):
        if self.model:
            self.model.insertRows(self.model.rowCount(), 1)
        else:
            self.sql_tableview_model()

    #----------------------------------------------------------
    def sql_tableview_model(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('Suppliers.db')
        
        tableview = self.ui.tableView
        self.model = QtSql.QSqlTableModel()
        tableview.setModel(self.model)
        
        self.model.setTable('Supplier')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)   # All changes to the model will be applied immediately to the database
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Supplier_ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "CompanyName")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "ContactName")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "ContactTittle") 
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Address")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "City")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Region")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "PostalCode")        
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Country")
        self.model.setHeaderData(9, QtCore.Qt.Horizontal, "Phone")                          
        self.model.setHeaderData(10, QtCore.Qt.Horizontal, "Fax")
        self.model.setHeaderData(11, QtCore.Qt.Horizontal, "HomePage") 
    #----------------------------------------------------------
    def print_data(self):
        sqlite_file = 'Suppliers.db'
        conn = sqlite3.connect(sqlite_file)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM 'Supplier' ORDER BY Supplier_ID")
        all_rows = cursor.fetchall()
        pprint(all_rows)
        
        conn.commit()       # not needed when only selecting data
        conn.close()        
        
    #----------------------------------------------------------
    def create_DB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('Suppliers.db')
        db.open()
        
        query = QtSql.QSqlQuery()
          
        query.exec_("create table Supplier(Supplier_ID int primary key, "
                    "CompanyName varchar(40),ContactName varchar(30), ContactTittle varchar(30), Address varchar(60), City varchar(15), Region varchar(15), PostalCode varchar(10), Country varchar(15), Phone varchar(24), Fax varchar(24), HomePage Text )")
        query.exec_("insert into Supplier values(Lacoste,Juan,Carlos,juan12@gmai.com,NEWYORK,York,21100,,E.U.A,1234567890,1234567,Juanlos)")
        query.exec_("insert into Supplier values(Pirma,Jose,Damian,jose21@gmai.com,Canada,Toronto,12345,Canada,0987654321,7654321,Josess)")
        query.exec_("insert into Supplier values(Adiddas,Jhon,michael,jhon456@gmai.com,Texas,Corou,98765,E.U.A,1112223334,9876543,machil)")
        query.exec_("insert into Supplier values(Rolex,Dave,javier,Dav963@gmai.com,Tokio,Japon,35963,Japon,0987654321,7654321,Xavi)")

if __name__ == "__main__":
    MainWindow_EXEC()
