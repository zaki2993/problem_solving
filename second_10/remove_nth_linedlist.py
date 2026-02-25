class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head == None or head.next == None:
            return None
        temp = head
        count = 1
        while temp.next != None:
            temp = temp.next
            count += 1
        c = (count-1) - n
        if c == 1:
            head = head.next 
            return head
        temp = head
        target = 1
        while target < c - 1:
            temp = temp.next
            target += 1
        temp.next = temp.next.next
        return head
