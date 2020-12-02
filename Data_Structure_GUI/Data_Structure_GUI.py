from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from GUI_for_Data_Structure import *
from LinkedList import *
from Stack import *
from Queue import *
from BST import *

from functools import partial 

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
        self.Queue_insert_button.clicked.connect(self.Queue_enqueue_app)
        self.Queue_delete_button.clicked.connect(self.Queue_dequeue_app)

        #Quit Button
        self.quit_button.clicked.connect(self.close_app)

    def Queue_enqueue_app(self):
        global queue_index_num

        if self.Queue_insert_Edit.text() == '':
            return False

        queue_enqueue_node = str(self.Queue_insert_Edit.text())
        queue_list.queue_put(queue_enqueue_node)
        self.Queue_insert_Edit.clear()

        queue_index_num = 0

        if queue_index_num == 0:
            self.queue_node_1.setText(queue_list.print_queue(queue_index_num))
            if queue_list.print_queue(queue_index_num) != '':
                self.queue_node_1.setStyleSheet("color : black;"
                                            "background-color: #ffcf5d;"
                                            "border: 2px solid black;")
            queue_index_num += 1

        if queue_index_num == 1:
            self.queue_node_2.setText(queue_list.print_queue(queue_index_num))
            if queue_list.print_queue(queue_index_num) != '':
                self.queue_node_2.setStyleSheet("color : black;"
                                            "background-color: #ff8239;"
                                            "border: 2px solid black;")
            queue_index_num += 1

        if queue_index_num == 2:    
            self.queue_node_3.setText(queue_list.print_queue(queue_index_num))
            if queue_list.print_queue(queue_index_num) != '':
                self.queue_node_3.setStyleSheet("color : black;"
                                            "background-color: #e20000;"
                                            "border: 2px solid black;")
            queue_index_num += 1

        if queue_index_num == 3:
            self.queue_node_4.setText(queue_list.print_queue(queue_index_num))
            if queue_list.print_queue(queue_index_num) != '':
                self.queue_node_4.setStyleSheet("color : black;"
                                            "background-color: #d50000;"
                                            "border: 2px solid black;")
            queue_index_num += 1

        if queue_index_num == 4:
            self.queue_node_5.setText(queue_list.print_queue(queue_index_num))
            if queue_list.print_queue(queue_index_num) != '':
                self.queue_node_5.setStyleSheet("color : black;"
                                            "background-color: #c30000;"
                                            "border: 2px solid black;")
            queue_index_num += 1

        if queue_index_num == 5:
            self.queue_node_6.setText(queue_list.print_queue(queue_index_num))
            if queue_list.print_queue(queue_index_num) != '':
                self.queue_node_6.setStyleSheet("color : black;"
                                            "background-color: #aa0000;"
                                            "border: 2px solid black;")
            queue_index_num += 1

        if queue_index_num == 6:
            self.queue_node_7.setText(queue_list.print_queue(queue_index_num))
            if queue_list.print_queue(queue_index_num) != '':
                self.queue_node_7.setStyleSheet("color : black;"
                                            "background-color: #a30000;"
                                            "border: 2px solid black;")

        if self.queue_node_7.text():
            self.Queue_checking.setText("Queue Overflow")
            self.Queue_checking.setStyleSheet("color: black;"
                                          "background-color: #aa6919;")

        elif self.queue_node_1.text() != '' and self.stack_node_7.text() == '':
            self.Queue_checking.setText("None")
            self.Queue_checking.setStyleSheet("color: white;"
                                        "background-color: #00ffff;")


    def Queue_dequeue_app(self):
        global queue_index_num

        queue_list.queue_pop()

        queue_index_num = 0

        if queue_index_num == 0:
            self.queue_node_1.setText(queue_list.print_queue(queue_index_num))
            if queue_list.print_queue(queue_index_num) == '':
                self.queue_node_1.clear()
                self.queue_node_1.setStyleSheet("background-color: #ffffff;")
            queue_index_num += 1

        if queue_index_num == 1:
            self.queue_node_2.setText(queue_list.print_queue(queue_index_num))
            if queue_list.print_queue(queue_index_num) == '':
                self.queue_node_2.clear()
                self.queue_node_2.setStyleSheet("background-color: #ffffff;")
            queue_index_num += 1

        if queue_index_num == 2:    
            self.queue_node_3.setText(queue_list.print_queue(queue_index_num))
            if queue_list.print_queue(queue_index_num) == '':
                self.queue_node_3.clear()
                self.queue_node_3.setStyleSheet("background-color: #ffffff;")
            queue_index_num += 1

        if queue_index_num == 3:
            self.queue_node_4.setText(queue_list.print_queue(queue_index_num))
            if queue_list.print_queue(queue_index_num) == '':
                self.queue_node_4.clear()
                self.queue_node_4.setStyleSheet("background-color: #ffffff;")
            queue_index_num += 1

        if queue_index_num == 4:
            self.queue_node_5.setText(queue_list.print_queue(queue_index_num))
            if queue_list.print_queue(queue_index_num) == '':
                self.queue_node_5.clear()
                self.queue_node_5.setStyleSheet("background-color: #ffffff;")
            queue_index_num += 1

        if queue_index_num == 5:
            self.queue_node_6.setText(queue_list.print_queue(queue_index_num))
            if queue_list.print_queue(queue_index_num) == '':
                self.queue_node_6.clear()
                self.queue_node_6.setStyleSheet("background-color: #ffffff;")
            queue_index_num += 1

        if queue_index_num == 6:
            self.queue_node_7.setText(queue_list.print_queue(queue_index_num))
            if queue_list.print_queue(queue_index_num) == '':
                self.queue_node_7.clear()
                self.queue_node_7.setStyleSheet("background-color: #ffffff;")

        if self.queue_node_1.text() == '':
            self.Queue_checking.clear()
            self.Queue_checking.setText("Queue underflow")
            self.Queue_checking.setStyleSheet("color: white;"
                                        "background-color: #aaff7f;")
            return False

        elif self.queue_node_1.text() != '' and self.queue_node_7.text() == '':
            self.Queue_checking.setText("None")
            self.Queue_checking.setStyleSheet("color: white;"
                                        "background-color: #00ffff;")

    def Tree_insert_app(self):
        global tree_index_num

        GUI_tree_list = []

        if self.Tree_insert_Edit.text() == '':
            return False

        Tree_insert_node = int(self.Tree_insert_Edit.text())

        bt.add(Tree_insert_node)
        GUI_tree_list = re_positioning()
        print()
        self.Tree_insert_Edit.clear()

        tree_index_num = 0

        self.Tree_node_1.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_2.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_3.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_4.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_5.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_6.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_7.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_8.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_9.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_10.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_11.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_12.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_13.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_14.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_15.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        

    def Tree_delete_app(self):
        global tree_index_num, tree_array

        GUI_tree_list = []

        if self.Tree_delete_Edit.text() == '':
            return False

        Tree_delete_node = int(self.Tree_delete_Edit.text())

        bt.remove(Tree_delete_node)
        re_positioning()
        GUI_tree_list = re_positioning()
        self.Tree_delete_Edit.clear()

        tree_index_num = 0

        self.Tree_node_1.clear()
        self.Tree_node_1.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_2.clear()
        self.Tree_node_2.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_3.clear()
        self.Tree_node_3.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_4.clear()
        self.Tree_node_4.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_5.clear()
        self.Tree_node_5.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_6.clear()
        self.Tree_node_6.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_7.clear()
        self.Tree_node_7.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_8.clear()
        self.Tree_node_8.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_9.clear()
        self.Tree_node_9.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_10.clear()
        self.Tree_node_10.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_11.clear()
        self.Tree_node_11.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_12.clear()
        self.Tree_node_12.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_13.clear()
        self.Tree_node_13.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_14.clear()
        self.Tree_node_14.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1

        self.Tree_node_15.clear()
        self.Tree_node_15.setText(str(GUI_tree_list[tree_index_num]))
        tree_index_num += 1




    def Stack_insert_app(self):
        global stack_index_num
        push_stack_node = str(self.Stack_Push_Edit.text())

        if self.Stack_Push_Edit.text() == '':
            return False
        
        stack_list.stack_push(push_stack_node)
        self.Stack_Push_Edit.clear()
        
        if stack_index_num == 0:
            self.stack_node_1.setText(stack_list.print_stack(stack_index_num))
            self.stack_node_1.setStyleSheet("color : black;"
                                            "background-color: #ffcf5d;"
                                            "border: 2px solid black;")
            self.stack_node_1.setFont(QFont('Berlin Sans FB Demi', 15))
            stack_index_num += 1

        elif stack_index_num == 1:
            self.stack_node_2.setText(stack_list.print_stack(stack_index_num))
            self.stack_node_2.setStyleSheet("color : black;"
                                            "background-color: #ff8239;"
                                            "border: 2px solid black;")
            self.stack_node_2.setFont(QFont('Berlin Sans FB Demi', 15))
            stack_index_num += 1

        elif stack_index_num == 2:
            self.stack_node_3.setText(stack_list.print_stack(stack_index_num))
            self.stack_node_3.setStyleSheet("color : black;"
                                            "background-color: #e20000;"
                                            "border: 2px solid black;")
            self.stack_node_3.setFont(QFont('Berlin Sans FB Demi', 15))
            stack_index_num += 1

        elif stack_index_num == 3:
            self.stack_node_4.setText(stack_list.print_stack(stack_index_num))
            self.stack_node_4.setStyleSheet("color : black;"
                                            "background-color: #d50000;"
                                            "border: 2px solid black;")
            self.stack_node_4.setFont(QFont('Berlin Sans FB Demi', 15))
            stack_index_num += 1
        
        elif stack_index_num == 4:
            self.stack_node_5.setText(stack_list.print_stack(stack_index_num))
            self.stack_node_5.setStyleSheet("color : black;"
                                            "background-color: #c30000;"
                                            "border: 2px solid black;")
            self.stack_node_5.setFont(QFont('Berlin Sans FB Demi', 15))
            stack_index_num += 1

        elif stack_index_num == 5:
            self.stack_node_6.setText(stack_list.print_stack(stack_index_num))
            self.stack_node_6.setStyleSheet("color : black;"
                                            "background-color: #aa0000;"
                                            "border: 2px solid black;")
            self.stack_node_6.setFont(QFont('Berlin Sans FB Demi', 15))
            stack_index_num += 1

        elif stack_index_num == 6:
            self.stack_node_7.setText(stack_list.print_stack(stack_index_num))
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
            stack_list.stack_pop()
            self.stack_node_1.clear()
            self.stack_node_1.setStyleSheet("background-color: #ffffff;")
            stack_index_num -= 1

        elif stack_index_num == 2:
            stack_list.stack_pop()
            self.stack_node_2.clear()
            self.stack_node_2.setStyleSheet("background-color: #ffffff;")
            stack_index_num -= 1
        
        elif stack_index_num == 3:
            stack_list.stack_pop()
            self.stack_node_3.clear()
            self.stack_node_3.setStyleSheet("background-color: #ffffff;")
            stack_index_num -= 1
        
        elif stack_index_num == 4:
            stack_list.stack_pop()
            self.stack_node_4.clear()
            self.stack_node_4.setStyleSheet("background-color: #ffffff;")
            stack_index_num -= 1

        elif stack_index_num == 5:
            stack_list.stack_pop()
            self.stack_node_5.clear()
            self.stack_node_5.setStyleSheet("background-color: #ffffff;")
            stack_index_num -= 1

        elif stack_index_num == 6:
            stack_list.stack_pop()
            self.stack_node_6.clear()
            self.stack_node_6.setStyleSheet("background-color: #ffffff;")
            stack_index_num -= 1

        elif stack_index_num == 7:
            stack_list.stack_pop()
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
        stack_list.reset_stack()
        queue_list.reset_queue()
        
        sys.exit()


if __name__ == "__main__":
    import sys

    stack_index_num = 0
    tree_index_num = 0
    queue_index_num = 0

    GUI_tree_list = []
      
    init_list()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = main()
    ui.setupUi(MainWindow)

    ui.setupUi(MainWindow)
    ui.menu()

    MainWindow.show()
    sys.exit(app.exec_())
