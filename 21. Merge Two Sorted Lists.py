class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		if not l1 or not l2:
			return l1 if not l2 else l2

		if l1.val <= l2.val:
			ptr = head = l1
			l1 = l1.next
		else:
			ptr = head = l2
			l2 = l2.next
	   
		while l1 and l2:
			if l1.val <= l2.val:
				ptr.next = l1
				l1 = l1.next
			else:
				ptr.next = l2
				l2 = l2.next
			ptr = ptr.next
		
		ptr.next = l1 if l1 else l2
		
		return head
