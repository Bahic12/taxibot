from LinkedList import Noda, LinkedList

llist = LinkedList()

llist.head = Noda('Monday')
tuesday = Noda('Tuesday')
wednesday = Noda('Wednesday')

llist.head.next = tuesday
tuesday.next = wednesday

llist.push('Sunday')


llist.insertAfter(llist.head.next.next, 'Tuesday night')

llist.append('Thursday')

llist.deleteNode('Tuesday night')
llist.printlist()