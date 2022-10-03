class Node():
    def __init__(self, data):
        self.data = data
        # 마지막은 일단 None -> 이것으로 마지막 노드에 삽입할 때 ok
        self.next = None

class LinkedList():
    def __init__(self, head):
        self.head = head
        self.tail = head
    
    # 마지막 노드에 삽입
    def addToEnd(self, node): #삽입할 노드를 준비한다.
        if(self.head is None): # 아무것도 없는 연결리스트면 head와 tail이 같이 새로 넣는 node를 가리킨다.
            self.head = node
            self.tail = node
        else:
            self.tail.next = node #
            self.tail = node
    
    # 첫 노드에 삽입
    def addToStart(self, node):
        if (self.head is None):  # 아무것도 없는 연결리스트면 head와 tail이 같이 새로 넣는 node를 가리킨다.
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    # 중간에 삽입 -> 이거 이전 노드 찾기 가능?
    def insertMiddel(self, pre, node):
        if(self.head is None):
            self.head = node
            self.tail = node
        else:
            node.next = pre.next
            pre.next = node

    def print2(self):
        tmp = self.head
        while (tmp): # pop에서 처리하듯이 none 나오면 false로 봄
            print(tmp.data)
            tmp = tmp.next
