class Node():
    def __init__(self, data):
        self.data = data
        # 마지막은 일단 None -> 이것으로 마지막 노드에 삽입할 때 ok
        self.next = None

class LinkedList():
    # 이건 무조건 받으면서 링크드 리스트를 만들게 하네? > 공백 리스트를 애초에 만들지 않음
    # + c언어에서는 동적으로 리스트를 할당하면 free를 하는데 파이썬은 자동으로 주워담음
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

    # 마지막 노드 삭제
    def deleteEnd(self):
        tmp = self.head
        data = ""
        while(tmp.next):
            if(tmp.next.next is None):
                data = tmp.next.data
                tmp.next = None
                self.tail = tmp.next
            else:
                tmp = tmp.next
        return data

    # 맨 앞 노드 삭제
    def deleteStart(self):
        data = self.head.data
        if(self.head.next is None):
            return
        else:
            self.head = self.head.next
        return data

    # 원하는 값의 데이터 접근
    def searchData(self, data):
        tmp = self.head
        while(tmp):
            if(tmp.data == data):
                return tmp # 그 노드 자체를 리턴하는게 포인트
            else:
                tmp = tmp.next
        return -1

    #원하는 인덱스의 데이터 접근
    def searchIndex(self, index):
        tmp = self.head
        for _ in range(index):
            tmp = tmp.next

        return tmp # 그 노드 자체를 리턴하는게 포인트

    def print2(self):
        tmp = self.head
        while (tmp): # pop에서 처리하듯이 none 나오면 false로 봄
            print(tmp.data,"-> ", end="")
            tmp = tmp.next
