class Solution(object):
    def mergeKLists(self, lists):
        newlist = newlisttemp = None
        temp = None
        while lists:
            lists = [node for node in lists if node is not None]
            if not lists:
                break
            min_node = lists[0]
            index = 0
            size = len(lists)

            if size == 1:
                if newlisttemp is None:
                    return lists[0]
                else:
                    newlisttemp.next = lists[0]
                    return newlist
            for i in range(size):
                if lists[i].val < min_node.val:
                    min_node = lists[i]
                    index = i
            temp = lists[index]
            lists[index] = lists[index].next
            temp.next = None

            if newlisttemp is None:
                newlist = temp
                newlisttemp = temp
            else:
                newlisttemp.next = temp
                newlisttemp = temp
        return newlist
