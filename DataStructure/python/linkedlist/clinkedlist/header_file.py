'''
tail이 있고 없고의 차이를 생각해보자
tail이 있으면 첫 노드에 삽입할 때 마지막 노드가 쉽게 삽입할 첫 노드를 바라보게 할 수 있다. 하지만 메모리를 먹는다.
tail이 없으면 메모리는 안 먹는다 하지만 마지막 노드를 찾기 위해 while을 돌려서
맨 앞을 보는 노드(마지막 노드가 맨 앞을 보므로)를 찾아야한다.

-> 내 생각에는 연결 리스트의 장점이 삽입, 삭제가 쉽지만 단점이 찾는데 오래걸릴 수 도 있다 였으니
tail이 있는게 좋을 것 같다.
'''


class Node():
    def __init__(self, data):
        self.data = data
        # 마지막은 일단 None -> 이것으로 마지막 노드에 삽입할 때 ok
        self.next = None

class CLinkedList():
    def __init__(self, head):
        self.head = head
        self.tail = head
    
    # 마지막 노드에 삽입
    def addToEnd(self, node):
        if(self.head is None):
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.next = self.head
            self.tail = node
    
    # 첫 노드에 삽입
    def addToStart(self, node):
        if (self.head is None):
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
            self.tail.next = node

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
        while(tmp.next is not self.head):
            # 근데 마지막 노드를 찾는게 문제가 아니고 마지막 노드 하나 전 노드를 찾아야 한다.
            if(tmp.next.next is self.head):
                data = tmp.next.data
                tmp.next = self.head
                self.tail = tmp
            else:
                tmp = tmp.next
        return data

    # 맨 앞 노드 삭제
    def deleteStart(self):
        data = self.head.data
        if(self.head.next is None):
            return
        else:
            self.tail = self.head.next
            self.head = self.head.next # 이제 지워도 마지막 노드가 첫 노드를 바라보는 것 잊지말자
            self.tail.next = self.head
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


    # null이 없다 보니 무한 루프가 출력되면 잘 연결한 거다. 하지만 print()를 수정해야한다.
    # print 해보니 진짜 원형이 느껴진다.
    def print2(self):
        tmp = self.head
        while (1):
            print(tmp.data,"-> ", end="")
            tmp = tmp.next
            if(tmp is self.head):
                print()
                break

