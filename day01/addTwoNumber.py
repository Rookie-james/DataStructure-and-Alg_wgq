#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : WGQ
# @Time    : 2020/11/9 20:08

'''
给出两个 非空 的链表用来表示两个非负整数。
其中，它们各自的位数是按照 逆序 的方式存储的，
并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，
则会返回一个新的链表来表示它们的和。
您可以假设除了数字0之外，这两个数都不会以0开头。
'''
'''
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        prenode = ListNode(0)   # 存储头节点
        lastnode = prenode      # 不断扩展，存储每次循环中的下一节点
        sum = 0
        while sum or l1 or l2:
            sum, cur = divmod(sum + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            lastnode.next = ListNode(cur)
            lastnode = lastnode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return prenode.next


def generateList(l: list) -> ListNode:
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next

def printList(l: ListNode):
    while l:
        print("%d, " %(l.val), end = '')
        l = l.next
    print('')

if __name__ == "__main__":
    l1 = generateList([1, 5, 8])
    l2 = generateList([9, 1, 2, 9])
    printList(l1)
    printList(l2)
    s = Solution()
    sum  = s.addTwoNumbers(l1, l2)
    printList(sum)





# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         #初始化一个节点，temp与head都指向该节点，但是temp需要不断扩展，因为明显结果不是一个节点能完成的。然后head.next就是我们要返回的头结点地址了。因为head本身是存储的0,它的next才是我们想要的第一个有用的数所在的地方。
#         temp = ListNode(0)
#         head = temp
#         #sum是l1,l2对应位相加的和，例如2+3=5。那么temp就存5。也可能是7+8=15,那么sum%10的数，即余数就是temp。商为1，被sum保存进入下一次循环，也就是下一位相加，例如下一位原来是3+4，但是这里有个进位1，就变成了3+4+1。之后不断循环即可。
#         sum = 0
#         #只要l1,l2或者sum有值就循环加。l1,l2=None,即说明到了链表尾部了。sum=0就说明最后一位没有进位了，合在一起是跳出来循环的条件
#         while l1!=None or l2!=None or sum!=0:
#         #只要l1，l2还有值，就加给sum。然后l1,l2往后走一步。
#             if l1!=None:
#                 sum+=l1.val
#                 l1 = l1.next
#             if l2!=None:
#                 sum+=l2.val
#                 l2 = l2.next
#               #a:余数。sum:商。也可写成：sum,a=divmod(sum,10)
#               # divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
#             a = sum%10
#             sum = sum//10
#             #就是程序开头的0节点后面就是和的第一位了
#             temp.next = ListNode(a)
#             #之后就开始进行ListNode(0).next.next的计算了
#             temp =temp.next
#             #返回ListNode(0)的下一个节点，因为那是和的第一位。
#         return head.next

# if __name__ == '__main__':
