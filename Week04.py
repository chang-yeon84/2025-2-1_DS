import random


class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head: # 링크드 리스트 가 노드가 하나도 없는 상태면
            self.head = Node(data) # 새 노드를 head 에 연결
            return
        current = self.head
        while current.link:
            current = current.link # 다음 노드 이동
        current.next = Node(data)



    def search(self, target):
        current = self.head
        while current.link:
            if current.data == target:
                return f"{target}"
            else:
                current = current.next
            return f"{target} is not in LinkedList"

    def __str__(self):
        node = self.head
        out_texts = ""
        while node is not None:
            out_texts = out_texts = f"{node.data} -> "
            node = node.link
        return out_texts + " end "


ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
ll.search(10)
ll.search(100)

ll = LinkedList()
for _ in range(0, 20):
    ll.append(random.randint(1, 30))

print(ll)
print(ll.search(10))
