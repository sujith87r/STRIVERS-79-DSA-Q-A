class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if head == None:
        head = newNode
        return head
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return head
# utility function to create cycle
def createCycle(head, a, b):
    cnta = 0
    cntb = 0
    p1 = head
    p2 = head
    while cnta != a or cntb != b:
        if cnta != a:
            p1 = p1.next
            cnta += 1
        if cntb != b:
            p2 = p2.next
            cntb += 1
    p2.next = p1
# utility function to detect cycle
def cycleDetect(head):
    if head == None:
        return False
    fast = head
    slow = head
    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False
if __name__ == "__main__":
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 4)
    createCycle(head, 1, 3)  # creating cycle in the list
    if cycleDetect(head) == True:
        print("Cycle detected")
    else:
        print("Cycle not detected")
