from second_week.python_prac.Stack_structure import Node


class Queue:
    def __init__(self):
        self.front = None

        def push(self,val):
            if not self.front:
                self.front = Node(val)
                return

            node = self.front
            while node.next:
                node = node.next

            node.next = Node(val)

        def pop(self):
            if not self.front:
                return None
            node = self.front
            self.front = node.next
            return node.val

        def is_empty(self):
            return self.front is None

    # class Queue:
    #     def __init__(self):
    #         self.front = None
    #
    #     def push(self, value):
    #         if not self.front:
    #             self.front = Node(value)
    #             return
    #
    #         node = self.front
    #         while node.next:
    #             node = node.next
    #         node.next = Node(value)
    #
    #     def pop(self):
    #         if not self.front:
    #             return None
    #
    #         node = self.front
    #         self.front = self.front.next
    #         return node.val
    #
    #     def is_empty(self):
    #         return self.front is None