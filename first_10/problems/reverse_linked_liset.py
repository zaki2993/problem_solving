# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        newlist = None
        while head != None:
            temp = head
            head = head.next
            temp.next = None
            if newlist == None:
                newlist = temp
            else :
                temp.next = newlist
                newlist = temp
        return newlist

        
