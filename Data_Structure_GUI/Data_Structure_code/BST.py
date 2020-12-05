
class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


# 이진트리 만들기
class BinaryTree:
    # 초기값 head는 None
    def __init__(self):
        self.head = Node(None)

        self.preorder_list = []
        self.inorder_list = []
        self.postorder_list = []

    # 값 추가하기 head가 없을 경우
    def add(self, item):

        for i in tree_array:
            if i == item:
                return False

        array.append(item)

        if self.head.val is None:
            self.head.val = item

        # head가 있으면 왼쪽배치 or 오른쪽배치
        else:
            self.__add_node(self.head, item)

    # head가 있는 경우
    def __add_node(self, cur, item):
        print('부모:', cur.val, '자식:', item)
        # head 값이 크면 왼쪽으로
        if cur.val >= item:
            if cur.left is not None:
                self.__add_node(cur.left, item)
            else:
                cur.left = Node(item)
        # head 값이 작으면 오른쪽으로
        else:
            if cur.right is not None:
                self.__add_node(cur.right, item)
            else:
                cur.right = Node(item)

    # 찾기!!
    def search(self, item):
        global tree_cycle, tree_array

        tree_cycle = 0
        
        for i in range(len(tree_array)):
            if tree_array[i] == item:
                tree_array[i] = ''

        if self.head is None:
            return False
        else:
            return self.__search_node(self.head, item)

    def __search_node(self, cur, item):
        global tree_cycle, tree_array

        # print(cur.val, item)
        if cur.val == item:
            tree_array[tree_cycle] = int(cur.val)
            return True
        else:
            if cur.val >= item:
                if cur.left is not None:
                    tree_cycle = (tree_cycle * 2) + 1
                    return self.__search_node(cur.left, item)
                else:
                    return False
            else:
                if cur.right is not None:
                    tree_cycle = (tree_cycle * 2) + 2
                    return self.__search_node(cur.right, item)
                else:
                    return False

    # 지우기!!
    def remove(self, item):

        for i in array:
            if i == item:
                array.remove(i)
                tree_array.remove(i)
                tree_array.append('')

        #루트노드의 존재 여부 확인

        if self.head is None:
            print("no item")

        #self.head.val값과 item값이 일치하는지 확인

        if self.head.val == item:
            # 1) 노드의 자식이 없는 경우.

            if self.head.left is None and self.head.right is None:
                self.head = None

            # 2) 노드의 자식이 하나인 경우

            elif self.head.left is not None and self.head.right is None:
                self.head = self.head.left

            elif self.head.left is None and self.head.right is not None:
                self.head = self.head.right

            # 3) 노드의 자식이 둘인 경우

            elif self.head.left is not None and self.head.right is not None:
                self.head.val = self.most_left_val_from_right_tree(self.head.right).val
                self.remove_most_left_val(self.head, self.head.right, self.head.val)

        else:
            #self.head.val(기준)값과 item값의 대소비교가 필요.
            if self.head.val >= item:
                self._remove(self.head, self.head.left, item)
            else:
                self._remove(self.head, self.head.right, item)

    #삭제메서드2(루트노드 이후)

    def _remove(self, parent, cur, item):

        #cur.val(기준)값과 item값이 일치하는 경우, 일치하지않는 경우

        if cur.val == item:
            # 1) 노드의 자식이 없는 경우
            if cur.left is None and cur.right is None:
                if parent.left == cur:
                    parent.left = None
                else:
                    parent.right = None

            # 2) 노드의 자식이 하나인 경우

            elif cur.left is not None and cur.right is None:
                if parent.left == cur:
                    parent.left = cur.left
                else:
                    parent.right = cur.left

            elif cur.left is None and cur.right is not None:
                if parent.left == cur:
                    parent.left = cur.right
                else:
                    parent.right = cur.right

            # 3) 노드의 자식이 둘인 경우

            elif cur.left is not None and cur.right is not None:
                cur.val = self.most_left_val_from_right_tree(cur.right).val
                self.remove_most_left_val(cur, cur.right, cur.val)
        else:
            if cur.val >= item:
                self._remove(cur, cur.left, item)
            else:
                self._remove(cur, cur.right, item)

 

    #삭제메서드3(오른쪽 서브트리에서 제일 왼쪽의 리프노드를 찾는 메서드)

    def most_left_val_from_right_tree(self, cur):

        #cur.left가 존재하냐 안하냐에 따름.

        if cur.left is None:
            return cur
        else:
            return self.most_left_val_from_right_tree(cur.left)

    

    #삭제메서드4(찾은 제일 왼쪽의 리프노드를 제거하는 메서드)

    def remove_most_left_val(self, parent, cur, item):

        #cur.val값과 item값이 일치하냐 안하냐로 갈림
        if cur.val == item:
            #parent노드의 오른쪽 왼쪽 중에서 어디에 cur노드가 속하느냐 따라에 갈림
            if parent.left == cur:
                parent.left = None
            else:
                parent.right = None

        else:
            #cur.val(기준)값과 item값의 대소비교 필요
            if cur.val >= item:
                self.remove_most_left_val(cur, cur.left, item)
            else:
                self.remove_most_left_val(cur, cur.right, item)

    
    # 순회 Traverse
    # 전위순회 preorder 1. 루트 방문, 2. 왼쪽 서브트리, 3. 오른쪽 서브트리
    # 완성되어 있는 트리를 다른 서버에 리스트 형태로 보내서 그 서버에서 다시 트리를 구성할 때 사용
    def preorder_traverse(self):
        global tree_cycle

        tree_cycle = 0
        self.preorder_list = []
        if self.head is not None:
            self.__preorder(self.head)

    def __preorder(self, cur):
        global tree_cycle, tree_array

        self.preorder_list.append(cur.val)
        #tree_array[tree_cycle] = int(cur.val)
        print(tree_cycle)


        # print(cur.val)
        if cur.left is not None:
            tree_cycle = (tree_cycle * 2) + 1
            self.__preorder(cur.left)
        if cur.right is not None:
            tree_cycle = (tree_cycle * 2) + 2 
            self.__preorder(cur.right)

    # 정위순회 inorder 1. 왼쪽 2. 루트 3. 오른쪽
    # 오름차순 정렬할 때 | n의 시간복잡도로 정렬가능
    def inorder_traverse(self):
        global tree_cycle
        self.inorder_list = []
        tree_cycle = 0
        if self.head is not None:
            self.__inorder(self.head)

    def __inorder(self, cur):
        global tree_cycle
        if cur.left is not None:
            self.__inorder(cur.left)

        #self.inorder_list.append(cur.val)
        self.inorder_list.append(cur.val)
        # print(cur.val)

        if cur.right is not None:
            self.__inorder(cur.right)

    # 후위순회 postorder 1. 왼쪽, 3. 오른쪽, 3. 루트
    #
    def postorder_traverse(self):
        self.postorder_list = []
        if self.head is not None:
            self.__postorder(self.head)

    def __postorder(self, cur):
        if cur.left is not None:
            self.__postorder(cur.left)

        if cur.right is not None:
            self.__postorder(cur.right)

        self.postorder_list.append(cur.val)
        # print(cur.val)


def re_positioning():
    global array
    
    for i in array:
        bt.search(i)

    print(tree_array)
    print(array)

    return tree_array

bt = BinaryTree()

tree_array = [''] * 16

tree_cycle = 0

array = []


