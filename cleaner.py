import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



form_class = uic.loadUiType("./cleaner.ui")[0]



class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.driver = webdriver.Chrome()

        self.Btn_login.clicked.connect(self.login)
        self.Btn_logout.clicked.connect(self.logout)
        self.Btn_delete_board.clicked.connect(self.board)
        self.Btn_delete_cmt.clicked.connect(self.cmt)

    def login(self):
        print("로그인 버튼 클릭")
        self.driver.get('https://sign.dcinside.com/login?s_url=https%3A%2F%2Fgall.dcinside.com%2F&s_key=210')
        self.time.sleep(3)

        self.id = self.line_id.text()
        self.pw = self.line_password.text()

        self.driver.find_element('id').send_keys(self.id)
        self.driver.find_element('pw').send_keys(self.pw)
        self.driver.find_element()
        self.time.sleep(3)


    def logout(self):
         print("로그아웃 클릭")
    def board(self):
         print("게시글 삭제버튼 클릭")
    def cmt(self):
         print("댓글 삭제버튼 클릭")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

