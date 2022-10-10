from header_file import *

'''
아니 이런게 어떻게 되지??
다 ~ 객체 지향 언어이기 때문이지
속성, 메소드 다 클래스에 쓰고 협력도 매개변수로 클래스를 전달하여 클래스에 쓴다.
실행은 메인에서 클래스를 객체로 생성해서한다.

↓ ll이라는 객체가 만들어져서 독립된 ll 하나에만 더하고 출력하고 하는 것!!
'''

ll = CLinkedList(Node("상범"))
ll.addToEnd(Node("미르"))
ll.addToStart(Node("한영"))

ll.print2()

ll.deleteEnd()
n = ll.deleteStart()
ll.print2()
print(n)





# if(__name__ == '__main__'):


