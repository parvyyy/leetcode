class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    i = 0
    # Find LL len
    curr = head
    while curr:
        curr, i = curr.next, i + 1

    idx = i - n
    # Edge case - One element LL
    if i == 1:
        return None
    
    # Edge case - Removing first element
    if idx == 0:
        return head.next
    
    prior = head
    for i in range(idx - 1):
        prior = prior.next

    # Alter the link - make the node before connect to the node after.
    prior.next = prior.next.next

    return head

def main():
    head = removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 2)

    ans = ''
    while head:
        ans += str(head.val) + ' '
        head = head.next

    print(ans)
    return 0

if __name__ == "__main__":
    main()