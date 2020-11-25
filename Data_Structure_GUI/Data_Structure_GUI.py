from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from GUI_for_Data_Structure import *
from LinkedList import *
from Stack import *
from Tree import *
from Tree import bst
from functools import partial 

stack_index_num = 0
tree_index_num = 0

class main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        super().__init__()

    def menu(self):

        #Change Page
        mainButton_list = [self.Linked_list_page_button, self.Stack_page_button, self.Tree_page_button, self.Queue_page_button]
        for i, mainButton in enumerate(mainButton_list):
                mainButton.clicked.connect(partial(self.stackedWidget.setCurrentIndex, i))

        #Linked List Explain Button
        self.LinkedList_explan.setToolTip("연결 리스트, 링크드 리스트는 각 노드가 데이터와 포인터를 가지고 한 줄로 연결되어 있는 방식으로 데이터를 저장하는 자료 구조이다.\nINSERT에 수/문자를 입력하면 마지막 노드로 추가된다.\nDELETE에 지우고 싶은 수/문자를 입력하면 삭제된다.")

        #LinkedList Page
        self.LinkedList_insert_button.clicked.connect(self.Linkedlist_insert_app)
        self.LinkedList_delete_button.clicked.connect(self.Linkedlist_delete_app)

        #Stack Page
        self.Stack_insert_button.clicked.connect(self.Stack_insert_app)
        self.Stack_delete_button.clicked.connect(self.Stack_delete_app)

        #Stack Explain Button
        self.Stack_explan.setToolTip("스택은 가장 나중에 들어온 값이 먼저 나가는 자료구조이다.\nPush에 수/문자를 입력하면 스택의 가장 위에 값이 저장된다.\nPop 버튼을 클릭하면 스택의 가장 위 값이 삭제된다.\n이 스택은 최대 7개의 값을 저장할 수 있다.\n스택이 가득차면 Overflow, 비어있으면 Underflow 상태라고 함.")
            

        #Tree Page
        self.Tree_insert_button.clicked.connect(self.Tree_insert_app)
        self.Tree_delete_button.clicked.connect(self.Tree_delete_app)

        #Queue Page

        #Quit Button
        self.quit_button.clicked.connect(self.close_app)

    def Tree_insert_app(self):
        Tree_insert_node = self.Tree_insert_Edit.text()

        if self.Tree_insert_Edit.text() == '':
            return False
        elif Tree_insert_node.isalpha():
            return False

        bst.insert(Tree_insert_node)
        self.Tree_insert_Edit.clear()

        
        

    def Tree_delete_app(self):
        Tree_delete_node = self.Tree_delete_Edit.text()

        if self.Tree_delete_Edit.text() == '':
            return False
        elif Tree_delete_node.isalpha():
            return False


    def Stack_insert_app(self):
        global stack_index_num
        push_stack_node = str(self.Stack_Push_Edit.text())

        if self.Stack_Push_Edit.text() == '':
            return False
        
        stack_push(push_stack_node)
        self.Stack_Push_Edit.clear()
        
        if stack_index_num == 0:
            self.stack_node_1.setText(print_stack(stack_index_num))
            self.stack_node_1.setStyleSheet("color : black;"
                                            "background-color: #ffcf5d;"
                                            "border: 2px solid black;")
            self.stack_node_1.setFont(QFont('Berlin Sans FB Demi', 15))
            stack_index_num += 1

        elif stack_index_num == 1:
            self.stack_node_2.setText(print_stack(stack_index_num))
            self.stack_node_2.setStyleSheet("color : black;"
                                            "background-color: #ff8239;"
                                            "border: 2px solid black;")
            self.stack_node_2.setFont(QFont('Berlin Sans FB Demi', 15))
            stack_index_num += 1

        elif stack_index_num == 2:
            self.stack_node_3.setText(print_stack(stack_index_num))
            self.stack_node_3.setStyleSheet("color : black;"
                                            "background-color: #e20000;"
                                            "border: 2px solid black;")
            self.stack_node_3.setFont(QFont('Berlin Sans FB Demi', 15))
            stack_index_num += 1

        elif stack_index_num == 3:
            self.stack_node_4.setText(print_stack(stack_index_num))
            self.stack_node_4.setStyleSheet("color : black;"
                                            "background-color: #d50000;"
                                            "border: 2px solid black;")
            self.stack_node_4.setFont(QFont('Berlin Sans FB Demi', 15))
            stack_index_num += 1
        
        elif stack_index_num == 4:
            self.stack_node_5.setText(print_stack(stack_index_num))
            self.stack_node_5.setStyleSheet("color : black;"
                                            "background-color: #c30000;"
                                            "border: 2px solid black;")
            self.stack_node_5.setFont(QFont('Berlin Sans FB Demi', 15))
            stack_index_num += 1

        elif stack_index_num == 5:
            self.stack_node_6.setText(print_stack(stack_index_num))
            self.stack_node_6.setStyleSheet("color : black;"
                                            "background-color: #aa0000;"
                                            "border: 2px solid black;")
            self.stack_node_6.setFont(QFont('Berlin Sans FB Demi', 15))
            stack_index_num += 1

        elif stack_index_num == 6:
            self.stack_node_7.setText(print_stack(stack_index_num))
            self.stack_node_7.setStyleSheet("color : black;"
                                            "background-color: #a30000;"
                                            "border: 2px solid black;")
            self.stack_node_7.setFont(QFont('Berlin Sans FB Demi', 15))
            stack_index_num += 1

        else:
            return False
        
        #stack checking
        
        if self.stack_node_7.text():
            self.Stack_check.setText("Stack Overflow")
            self.Stack_check.setStyleSheet("color: black;"
                                          "background-color: #aa6919;")

        elif self.stack_node_1.text() != '' and self.stack_node_7.text() == '':
            self.Stack_check.setText("None")
            self.Stack_check.setStyleSheet("color: white;"
                                        "background-color: #00ffff;")
        
        

    def Stack_delete_app(self):
        global stack_index_num

        if stack_index_num == 1:
            stack_pop()
            self.stack_node_1.clear()
            self.stack_node_1.setStyleSheet("background-color: #ffffff;")
            stack_index_num -= 1

        elif stack_index_num == 2:
            stack_pop()
            self.stack_node_2.clear()
            self.stack_node_2.setStyleSheet("background-color: #ffffff;")
            stack_index_num -= 1
        
        elif stack_index_num == 3:
            stack_pop()
            self.stack_node_3.clear()
            self.stack_node_3.setStyleSheet("background-color: #ffffff;")
            stack_index_num -= 1
        
        elif stack_index_num == 4:
            stack_pop()
            self.stack_node_4.clear()
            self.stack_node_4.setStyleSheet("background-color: #ffffff;")
            stack_index_num -= 1

        elif stack_index_num == 5:
            stack_pop()
            self.stack_node_5.clear()
            self.stack_node_5.setStyleSheet("background-color: #ffffff;")
            stack_index_num -= 1

        elif stack_index_num == 6:
            stack_pop()
            self.stack_node_6.clear()
            self.stack_node_6.setStyleSheet("background-color: #ffffff;")
            stack_index_num -= 1

        elif stack_index_num == 7:
            stack_pop()
            self.stack_node_7.clear()
            self.stack_node_7.setStyleSheet("background-color: #ffffff;")
            stack_index_num -= 1

        else:
            return False


        if self.stack_node_1.text() == '':
            self.Stack_check.clear()
            self.Stack_check.setText("Stack underflow")
            self.Stack_check.setStyleSheet("color: white;"
                                        "background-color: #aaff7f;")
            return False

        elif self.stack_node_1.text() != '' and self.stack_node_7.text() == '':
            self.Stack_check.setText("None")
            self.Stack_check.setStyleSheet("color: white;"
                                        "background-color: #00ffff;")



    def Linkedlist_insert_app(self):
        input_node= str(self.LinkedList_insert_Edit.text())

        if self.LinkedList_insert_Edit.text() == '':
            return False

        Linked_insert_node(input_node)
        Linked_print_node = Linked_print_list()
        self.LinkedList_node_label.setText(Linked_print_node)
        self.LinkedList_insert_Edit.clear()

    def Linkedlist_delete_app(self):
        if self.LinkedList_delete_Edit.text() == '':
            return False

        if self.LinkedList_delete_Edit.text() == 'HEAD':
            return False

        remove_node = str(self.LinkedList_delete_Edit.text())
        Linked_delete_node(remove_node)
        Linked_print_node = Linked_print_list()
        self.LinkedList_node_label.setText(Linked_print_node)
        self.LinkedList_delete_Edit.clear()

    def close_app(self):
        print('close_app')
        reset_linkedlist()
        reset_stack()
        sys.exit()


if __name__ == "__main__":
      import sys
      init_list()
      app = QtWidgets.QApplication(sys.argv)
      MainWindow = QtWidgets.QMainWindow()
      ui = main()
      ui.setupUi(MainWindow)

      ui.setupUi(MainWindow)
      ui.menu()

      MainWindow.show()
      sys.exit(app.exec_())
