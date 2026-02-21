def reverseList(head):
    newlist = None
    current = head
    while current is not None:
        new_node = ListNode(current.val)  # create new node
        new_node.next = newlist           # insert at front
        newlist = new_node
        current = current.next

    return newlist


def get_size(head):
    count = 0
    current = head

    while current is not None:
        count += 1
        current = current.next

    return count


class Solution(object):
    def reorderList(self, head):
        size = get_size(head)
        if size == 0 or size == 1:
            return None
        rev = reverseList(head)
        temp = head 
        head = head.next
        temp.next = None
        newlist = temp
        tempnewlist = newlist
        sizenewlist = 1
        temp = rev
        rev = rev.next
        temp.next = None
        tempnewlist.next = temp
        tempnewlist = temp
        sizenewlist = 2
        while sizenewlist < size:
            temp = head 
            head = head.next
            temp.next = None
            tempnewlist.next = temp
            tempnewlist = temp
            sizenewlist = sizenewlist + 1 
            if sizenewlist == size:
                break
            temp = rev
            rev = rev.next
            temp.next = None
            tempnewlist.next = temp
            tempnewlist = temp
            sizenewlist = sizenewlist + 1 
        return newlist
