class Solution(object):
    def hasCycle(self, head):
        if head == None or head.next == None:
            return False
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
