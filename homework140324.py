#2 реверс строки
def reverse(str: str) -> str:
    if (str == "" or str == " "):
        return ""
    result = ''
    start = len(str) - 1
    while (start >= 0):
        if (str[start] == ' '):
            start -= 1
        else:
            if (len(result) > 0):
                result += (' ')
            rev = start
            while (rev >= 0 and str[rev] != ' '):
                rev -= 1
            result += (str[rev + 1: rev + 1 + start - rev])
            start = rev

    return result

print(reverse("sfdghgjh jgfh ff"))


#1
#2
from sys import stdin

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def isPalindrome(head):
    # It stores the Linked List node value.
    st = []

    # Creating temporary Node.
    temp = head

    while temp is not None:
        # Add the current node value to stack.
        st.append(temp.data)

        # Move current pointer to next node.
        temp = temp.next

    while head is not None:

        # Get the top most element of stack.
        top = st.pop()

        if top != head.data:
            return False

        head = head.next

    return True


def takeinput():
    inputlist = [int(ele) for ele in input().split()]

    head = None
    tail = None

    for currentData in inputlist:

        if currentData == -1:
            break

        Newnode = Node(currentData)

        if head is None:
            head = Newnode
            tail = Newnode
        else:
            tail.next = Newnode
            tail = Newnode

    return head


# Main
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeinput()

    if isPalindrome(head):
        print('true')
    else:
        print('false')

    t -= 1