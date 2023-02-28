from login_page import Ui_MainWindow
from order_menu import Ui_My_order
from admin import Ui_MainWindow as admin
from welcome_page import Ui_MainWindow as main
from order_view import Ui_MainWindow as order_veiw_windows
from shop_menu import Ui_MainWindow as shop_windows
from user_menu import Ui_createuser
from PyQt5 import QtWidgets
import mysql.connector
from datetime import date
import sys


        



######################################       SQL connectin CLASS #################################################################3


class sql_tables:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1995",
            database = 'product')
        
    
    def add_order(self,order_id,order_name,data,customer,product_name,price,quantity):
        cursor = self.mydb.cursor()
        querry = ("INSERT INTO order_new"
                  "(order_id,order_name,data,customer,product_name,price,quantity)"
                  "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        data = (order_id,order_name,data,customer,product_name,price,quantity)
        cursor.execute(querry, data)
        self.mydb.commit()

    def view_order_full(self):
        curr = self.mydb.cursor()
        sql = "SELECT * FROM order_new"
        curr.execute(sql)
        result = curr.fetchall() 

        return result

    
    def view_shops(self):
        curr = self.mydb.cursor()
        sql = "SELECT * FROM shop_list"
        curr.execute(sql)
        result = curr.fetchall()
        all_shops = []

        for i in result:
            all_shops.append(i[0])

        return all_shops,result

    def login_page(self,us,pswr):
        curr = self.mydb.cursor()
        sql = "SELECT * FROM users"
        curr.execute(sql)
        result = curr.fetchall() 
        user_names = []
        user_passwords = []

        for user,password in result:
            user_names.append(user)
            user_passwords.append(password)

        if us in user_names and pswr in user_passwords:
            action = "open"
            enter_name = us
        else:
            action = "not open"
            enter_name = us
    

        return action, enter_name
    
    def user_sql_view(self):
        curr = self.mydb.cursor()
        sql = "SELECT * FROM users"
        curr.execute(sql)
        result = curr.fetchall()

        return result

    def user_sql_delete(self,text):
        cur = self.mydb.cursor()
        qry = "DELETE FROM users WHERE user_name = '{}'".format(text)
        cur.execute(qry)
        self.mydb.commit()

    def add_sql_user(self,user_name,user_password):
        cursor = self.mydb.cursor()
        querry = ("INSERT INTO users"
                  "(user_name,password)"
                  "VALUES (%s, %s)")
        data = (user_name,user_password)
        cursor.execute(querry, data)
        self.mydb.commit()

    def shop_sql_delete(self,text):
        cur = self.mydb.cursor()
        qry = "DELETE FROM shop_list WHERE shops = '{}'".format(text)
        cur.execute(qry)
        self.mydb.commit()

    def add_sql_shop(self,shop_name):
        cursor = self.mydb.cursor()
        querry = ("INSERT INTO shop_list"
                  "(shops)"
                  "VALUES (%s)")
        data = (shop_name,)
        cursor.execute(querry, data)
        self.mydb.commit()


######################################################### ADMIN MENU CLASS #####################################################

# for add user
class for_user(QtWidgets.QMainWindow,Ui_createuser):
    def __init__(self):
        super().__init__()
        self.user = Ui_createuser()
        self.user.setupUi(self)
        result = sql_tables().user_sql_view()
        self.user.users_name.setRowCount(len(result))
        self.user.adduser.pressed.connect(self.add_user)
        self.user.deleteuser.pressed.connect(self.delete_user)
        for row,item in enumerate(result):
            col1 = QtWidgets.QTableWidgetItem(str(item[0]))
            col2 = QtWidgets.QTableWidgetItem(str(item[1]))
            self.user.users_name.setItem(row,0,col1)
            self.user.users_name.setItem(row,1,col2)
    def add_user(self):
        name_of_new_user = self.user.user_add_name.text()
        password_of_new_user = self.user.user_password.text()
        sql_tables().add_sql_user(name_of_new_user,password_of_new_user)
        self.close()
        self.user_display = for_user()
        self.user_display.show()
        

    def delete_user(self):
        text = self.user.delete_user_name_id.text()
        sql_tables().user_sql_delete(text)
        self.close()
        self.user_display = for_user()
        self.user_display.show()


### shop menu
class for_shop(QtWidgets.QMainWindow,shop_windows):
    def __init__(self):
        super().__init__()
        self.shop = shop_windows()
        self.shop.setupUi(self)
        _,result = sql_tables().view_shops()
        self.shop.tableWidget.setRowCount(len(result))
        self.shop.shop_add.pressed.connect(self.new_shop)
        self.shop.shop_remove.pressed.connect(self.delete_shop)
        for row,item in enumerate(result):
            col1 = QtWidgets.QTableWidgetItem(str(item[0]))
            self.shop.tableWidget.setItem(row,0,col1)


    def new_shop(self):
        text = self.shop.add_shop_text.text()
        sql_tables().add_sql_shop(text)
        self.close()
        self.user_display = for_shop()
        self.user_display.show()


    def delete_shop(self):
        text = self.shop.delete_shop_text.text()
        sql_tables().shop_sql_delete(text)
        self.close()
        self.user_display = for_shop()
        self.user_display.show()
###################################################### MAIN APP CLASS ################################################################3
class my(QtWidgets.QMainWindow,main):
    def __init__(self):

        super(my,self).__init__()
        self.main_enter = main()
        self.main_enter.setupUi(self)

        self.main_enter.pushButton.pressed.connect(self.log_page)

    def log_page(self):
        self.desk = Ui_MainWindow()
        self.desk.setupUi(self)
        self.desk.login.pressed.connect(self.order_menu)


    def order_menu(self):
        name = self.desk.login_name.text()
        password = self.desk.password.text()
        result,self.my_name = sql_tables().login_page(name,password)

        if result == 'open' and self.my_name =="admin":
            self.my_admin_page = admin()
            self.my_admin_page.setupUi(self)
            self.my_admin_page.backtologin.pressed.connect(self.log_page)
            self.my_admin_page.allorders.pressed.connect(self.order_check)
            self.my_admin_page.addshop.pressed.connect(self.shop_open)
            self.my_admin_page.addnewuser.pressed.connect(self.user_open)


        elif result == 'open':
            self.order = Ui_My_order()
            self.order.setupUi(self)
            full_company,_ = sql_tables().view_shops()
            self.order.comboBox.addItems(full_company)
            self.order.data.setText(str(date.today()))
            self.order.order_maker.setText(self.my_name)
            self.order.approve_but.pressed.connect(self.order_info_filling)
            self.order.back_to_login.pressed.connect(self.log_page)

        else:
            print("not working")

    def order_info_filling(self):
        self.company_name = self.order.comboBox.currentText()
        self.order_number  = self.order.order_id.text()
        self.product_name = self.order.product_name.text()
        self.product_price = self.order.price_value.text()
        self.product_qty = self.order.quantity.text()
        self.order_date = date.today()
        self.creater_name = self.my_name
        self.total_sum = str(float(self.product_price) * float(self.product_qty))

        self.over_all = float(self.product_price) * float(self.product_qty)

        sql_tables().add_order(self.order_number,self.creater_name,self.order_date,self.company_name,self.product_name,self.product_price,self.product_qty)

    def order_check(self):
        self.main_enter = order_veiw_windows()
        self.main_enter.setupUi(self)
        self.main_enter.back_to_admin.pressed.connect(self.back_to_admin_view)
        self.main_enter.delete_order.pressed.connect(self.remove_order)
        result = sql_tables().view_order_full()

        self.main_enter.tableWidget.setRowCount(len(result))

        for row,item in enumerate(result):
            col1 = QtWidgets.QTableWidgetItem(str(item[0]))
            col2 = QtWidgets.QTableWidgetItem(str(item[1]))
            col3 = QtWidgets.QTableWidgetItem(str(item[2]))
            col4 = QtWidgets.QTableWidgetItem(str(item[3]))
            col5 = QtWidgets.QTableWidgetItem(str(item[4]))
            col6 = QtWidgets.QTableWidgetItem(str(item[5]))
            col7 = QtWidgets.QTableWidgetItem(str(item[6]))

            self.main_enter.tableWidget.setItem(row,0,col1)
            self.main_enter.tableWidget.setItem(row,1,col2)
            self.main_enter.tableWidget.setItem(row,2,col3)
            self.main_enter.tableWidget.setItem(row,3,col4)
            self.main_enter.tableWidget.setItem(row,4,col5)
            self.main_enter.tableWidget.setItem(row,5,col6)
            self.main_enter.tableWidget.setItem(row,6,col7)

    def remove_order(self):
        text = self.main_enter.lineEdit.text()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1995",
            database = 'product'
        )


        cur = mydb.cursor()


        qry = "DELETE FROM order_new WHERE order_id = '{}'".format(text)

        cur.execute(qry)
        mydb.commit()

        result = sql_tables().view_order_full()

        self.main_enter.tableWidget.setRowCount(len(result))

        for row,item in enumerate(result):
            col1 = QtWidgets.QTableWidgetItem(str(item[0]))
            col2 = QtWidgets.QTableWidgetItem(str(item[1]))
            col3 = QtWidgets.QTableWidgetItem(str(item[2]))
            col4 = QtWidgets.QTableWidgetItem(str(item[3]))
            col5 = QtWidgets.QTableWidgetItem(str(item[4]))
            col6 = QtWidgets.QTableWidgetItem(str(item[5]))
            col7 = QtWidgets.QTableWidgetItem(str(item[6]))

            self.main_enter.tableWidget.setItem(row,0,col1)
            self.main_enter.tableWidget.setItem(row,1,col2)
            self.main_enter.tableWidget.setItem(row,2,col3)
            self.main_enter.tableWidget.setItem(row,3,col4)
            self.main_enter.tableWidget.setItem(row,4,col5)
            self.main_enter.tableWidget.setItem(row,5,col6)
            self.main_enter.tableWidget.setItem(row,6,col7)

    def user_open(self):
        self.user_display = for_user()
        self.user_display.show()
    def shop_open(self):
        self.shop_display = for_shop()
        self.shop_display.show()
############  back

    def back_to_admin_view(self):
        self.my_admin_page = admin()
        self.my_admin_page.setupUi(self)
        self.my_admin_page.backtologin.pressed.connect(self.log_page)
        self.my_admin_page.allorders.pressed.connect(self.order_check)
        self.my_admin_page.addshop.pressed.connect(self.shop_open)
        self.my_admin_page.addnewuser.pressed.connect(self.user_open)


app = QtWidgets.QApplication(sys.argv)
my_app = my()
my_app.show()
app.exec_()