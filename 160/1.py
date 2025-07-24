from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    '''
    brute force: O(n*m),for every node in B, loop A and compare if headA==headB
    '''

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''
        a cheating method
        Custom Obj CAN be added to set!
        time: O(n+m)
        space: O(n+m)
        '''
        seen = set()
        # while headA:
        #     seen.add(id(headA))
        #     headA = headA.next
        # while headB:
        #     if id(headB) in seen:
        #         return headB
        #     headB = headB.next
        while headA:
            seen.add(headA)
            headA = headA.next
        while headB:
            if headB in seen:
                return headB
            headB = headB.next

        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''
        use len: if different end: no intersection
        compare len, and move head of the longer linkedlist by the offset
        this is faster than using set
        time: O(n+m)
        space: O(1)

        '''
        lenA = 1
        lenB = 1
        a = headA
        b = headB
        while a.next:
            lenA += 1
            a = a.next
        while b.next:
            lenB += 1
            b = b.next
        if a != b:  # compare end
            return None
        if lenA > lenB:  # maintain a is shorter
            lenA, lenB = lenB, lenA
            headA, headB = headB, headA
        while lenB != lenA:
            lenB -= 1
            headB = headB.next
        while headA != headB:
            headB = headB.next
            headA = headA.next
        return headA

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''
        2 ptr
        time: O(n+m)
        space: O(1)

        example: 
            listA=[    0,4,5]
            listB=[1,2,3,4,5]
            distance before intersection: 1, 3 -> offset we need to make: 3-1=2
        when a get to end and b is on 3, a go to 1(2 step faster)
        by doing this, a gets 2 when b is on 5, then a goes to 3, b goes to 0
        so the length difference is compensated, now they have same distance to skip before meeting at first intersect

        example: 
            listA=[      4,5]
            listB=[1,2,3,4,5]
            distance before intersection: 0, 3 -> difference: 3
        a goes to 5, be goes to 2, then a goes to 1, b goes to 3, offset is 2
        a goes to 3, be goes to 5, then a goes to 4, b goes to 4

        example: 
            listA=[4,5,]
            listB=[1,2,3,]
            distance before intersection: 0, 3 -> difference: 3
        a goes to 5, be goes to 2, then a goes to 1, b goes to 3, offset is 2
        a goes to 3, be goes to 5, then a goes to 4, b goes to 4

        '''
        a = headA
        b = headB
        swapped = False
        while a and b and a != b:
            if a.next:
                a = a.next
            else:
                if not swapped:
                    a = headB
                    swapped = True
                else:
                    return None
            if b.next:
                b = b.next
            else:
                b = headA

        return a

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''
        without flag value:
        consider they intersect at None, so skip value is their length
        offset is the len of shorter one + 1(since we take None into consideration)
        example: 
            listA=[4,5,]
            listB=[1,2,3,]
            distance before intersection: 0, 3 -> difference: 3
        a goes to 5, be goes to 2, then a goes to None, b goes to 3
        a goes to 1, be goes to 3, then a goes to 2, b goes to 4,
        their ramaining distance aligned
        so they'll hit None at the same time! 

        example: 
            listA=[]
            listB=[1,2,]
            distance before intersection: 0, 2 -> difference: 2 (intersect at None)
            offset: len(a)+1 = 0+1
        a goes to 1, be goes to 2, then a goes to 2, b goes to None
        their ramaining distance to None aligned:
            a has 2 before hit None at the end of B
            b has 2 before hit None at the end of A (2 -> None of b -> None of a)
        a goes to None, be goes to None(the head of a)
        so they'll hit None at the same time! 

        '''
        a = headA
        b = headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
