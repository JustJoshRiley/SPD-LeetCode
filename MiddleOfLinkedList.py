class Solution:
    def middleNode(self, head):
        length = 0
        
        current = head
        while current:
            length += 1
            current = current.next

        if length == 1:
            return head

        middle = int(length / 2)
        count = 0
        while head:
            count += 1
            head = head.next
            if count == middle:
                return head

        return None