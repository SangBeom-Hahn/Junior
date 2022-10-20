import queue

# class Node():
#     def __int__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data
#
# # 얘는 진짜 init 함수가 필요없고 top만 있으면 되겠는데?
#
# class BT():
#     def __init__(self):
#         self.top = None
#
#     def setNode(self, data):
#         node = Node(data)
#         return node
#
#     def search(self, p, x):
#         p = self.top
#         if(self.top == None):
#             return None
#         elif(self.top.data == x):
#             return self.top
#         elif(self.top.data > x):
#             self.search(self.top.left, x)
#         else:
#             self.search(self.top.right, x)
#
#     def add(self, p, data):
#         add_node = self.setNode(data)
#         p = self.top
#         if(p == None):
#             self.top = add_node
#         elif(self.top.data == data):
#             print("삽입 실패")
#             return
#         elif (self.top.data > data):
#             self.add(self.top.left, data)
#         else:
#             self.add(self.top.right, data)
#         return p









# 버전 2 -> 연결리스트에서 초기화할 때 헤드노드를 같이 넣어준게 좋아서 따라해보자
# 1. 연결리스트의 head처럼 root를 self로 가지고 있어서 재귀할 때 인자로 안주고 계속 class 내부에서 사용 가능
# 2. ㅋㅋㅋ 그런 줄 알았는데 트리는 선택!!!이 필수이고 선택은 재귀로 하니 무조건 인자로 포인터를 줘야함
# 3. 근데 가만 보니깐 연결리스트 방식도 생성자 인자로 head가 있네?? 처음 초기화할 때 헤드노드를 같이 넣어준다고 했잖아 -> 그러니 연결리스트 방식으로 충분히 재귀 사용 가능
# 4. ㅋㅋㅋㅋ 아니 근데 재귀는 BT를 하는게 아니고 메서드를 하는건데?? ㅋㅋㅋㅋ 걍 무조건 연결리스트 방식이다.

class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BT():
    def __init__(self, root):
        self.root = root

    def setNode(self, data): # 노드를 생성하고 데이터를 받고 부모와 연결하는 것
        return Node(data)

    def preOrder(self, root):
        if(self.root is not None):
            print(root.data)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def levelOrder(self):
        q = queue.Queue()
        q.put(self.root)
        while(not q.empty()):
            n = q.get()
            if(n is not None): # 왼이나 우자식이 null일 수도 있으니깐
                print(n.data)
                q.put(n.left)
                q.put(n.right)

    # ★재귀는 if None 타입이 무조건 맨 위다 안 그러면 무조건 Nonetype 에러 뜸!!
    def search(self, root, x):
        if(root is None):
            print("탐색 실패")  # 돌아갈 필요도 없지 않을까??
            return None
        elif(root.data > x):
            return self.search(root.left, x)
        elif(root.data < x):
            return self.search(root.right, x)
        else: # 검색 성공
            print("탐색 성공")
            return self.root


    # 재귀를 하는데 메소드 안에 노드를 만드는 게 있으면 안 되니
    # 데이터를 재귀하고 자리를 찾고 setNode를 하자

    # 오호라 self가 바라보는 루트랑 재귀에서 재대입될 루트 구분 어캐할 거임??
    # 아니 클래스에서의 재귀를 헷갈려하네 자꾸 클래스를 재귀하려해
    # self.root는 BT의 최상위 부모이고 그냥 root는 재귀 호출시에 선택되는 노드이다.
    # ★재귀는 if None 타입이 무조건 맨 위다 안 그러면 무조건 Nonetype 에러 뜸!!
    def insert(self, root, x):
        if (root is None):
            # 돌아갈 필요도 없지 않을까?? 무조건 돌아가야한다
            # 안 돌아가면 그냥 아무것도 일어나지 않고 노드 생성만하고 끝이다.
            # return도 해야하고 재귀를 호출한 곳에서는 리턴한 걸 받아서 레퍼런스를 대입도 해야한다
            print("삽입 성공")
            return self.setNode(x)
        elif (root.data > x):
            root.left = self.insert(root.left, x)
        elif (root.data < x):
            root.right = self.insert(root.right, x)
        else:  # none을 만난 거야
            print("삽입 실패")
        return root # 이거 왜 하는 거지?? 이거 안하면 연결이 새로 리셋되나?



    # 연결리스트에서와 마찬가지로 pre를 알면 좋듯이 삭제나, 삽입할 노드의 부모 노드를 알면 좋다 (parents) 부모 노드도 순회할 때 같이 알아보자
    # 루트는 무조건 알아야지??
    def delCase1(self, root, parent, node): # 책에서는 노드를 받는데 난 데이터를 받는 거로하자 -> 뭐로 해도 상관없다. 아미 삭제할 노드를 찾은 상태이니 노드로 하잨ㅋ
        if(parent is None):
            root = None
        else:
            if(parent.left == node):
                parent.left = None
            else:
                parent.right = None

        return root # 트리 전체가 변경될 수도 있으므로 root를 반환한다

    def delCase2(self, parent, root, node): # 삭제할 노드는 이미 찾은 상태니깐 node를 검사하고 밑에서 붙이는 흐름이 틀린게 아니다.
        # 노드 검사
        if(node.left is not None):
            child = node.left # 파이썬은 이런게 되는 신기한 언어라는 것!!!ㅜㅠ
        else:
            child = node.right

        if(node == root):
            root = child
        else:
            if(node is parent.left):
                node.left = child
            else:
                node.right = child
        return root

    # 이번엔 후계자 노드와 후계자의 부모노드를 찾아야한다, parent와 node는 삭제할 노드이지 후계자가 아니다.
    def delCase3(self, parent, root, node):
        succp = node # 찾기위한 변수
        succ = node.right # 후계자를 오른쪽 서브트리에서 가장 작은애로 고르겠다는 것 left도 가능

        while(succ.left != None): # 이것이 search_min_bst이다
            succp = succ
            succ = succ.left

        # ↑ 여기까지하면 후계자와 후계자의 부모를 찾은거다

        # 삭제할 노드에 값을 넣기전에 후계자부터 바꾼다
        # 후계자 부모의 왼쪽자식에 후계자의 오른쪽 자식을 붙인다
        succp.left = succ.right
        node.data = succ.data

        return root


    def deleteNode(self, root, x):
        if(root == None): # 공백트리이면
            return None

        # 연결리스트와 마찬가지로 pre를 만들고 탐색(연결리스트면 순회)를 한다
        # 이걸 삽입에서는 안하다가 여기서 처음 나온거라서 생소하다.
        parent = None
        node = root

        # 순회와 비슷한 방식으로 while을 써서 node가 None일 때까지 parent와 node를 찾는다
        while(node != None and node.data != x):
            parent = node
            if(x < node.data):
                node = node.left
            else:
                node = node.right

        if(node == None):
            return None
        if(node.left == None and node.right == None):
            root = self.delCase1(parent, root, node)
        elif(node.left == None or node.right == None):
            root = self.delCase2(parent, root, node)
        else:
            root = self.delCase3(parent, root, node)

        return root


bt = BT(Node(5))
bt.insert(bt.root, 7)
bt.search(bt.root, 7)
bt.insert(bt.root, 3)
bt.insert(bt.root, 8)
bt.insert(bt.root, 6)
bt.search(bt.root, 7)






