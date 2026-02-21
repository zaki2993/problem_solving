# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val < list2.val:
            temp = list1
            list1 = list1.next
            temp.next = None
            newlist = temp
        else:
            temp = list2
            list2 = list2.next
            temp.next = None
            newlist = temp
        templist = newlist
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp = list1
                list1 = list1.next
                temp.next = None
                templist.next = temp
                templist = templist.next
            else:
                temp = list2
                list2 = list2.next
                temp.next = None
                templist.next = temp
                templist = templist.next
        if list1 == None:
            templist.next = list2
        else:
            templist.next = list1
        return newlist
