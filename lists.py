from typing import Any


class Node:
    """
    An implementation of a list using LinkedList
    Also works as an Iterator
    """

    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None

    def append(self, val: Any) -> None:
        """
        Add node to the end of the list
        This is a recursive method may take long time for appending for a large list

        >>> LinkedList = Node()
        >>> LinkedList.append(1)
        >>> print(LinkedList)
        [1]
        >>> LinkedList.append(2)
        >>> print(LinkedList)
        [1, 2]

        :param val: The value to be added to the end of the list
        :return: None
        """
        if self.val is None:
            self.val = val
            return

        if self.next is None:
            self.next = Node(val)
            return

        self.next.append(val)

    def pop(self) -> Any:
        """
        Remove a node from the end of the list

        >>> LinkedList = Node(1)
        >>> LinkedList.append(2)
        >>> print(LinkedList)
        [1, 2]
        >>> LinkedList.pop()
        2
        >>> LinkedList.pop()
        1
        >>> print(LinkedList)
        []
        >>> LinkedList.pop()
        Traceback (most recent call last):
            ...
        IndexError: Can't pop from empty list

        :return: The value of the popped node
        """

        if self.val is None:
            raise IndexError("Can't pop from empty list")

        if self.next is None:
            value = self.val
            self.val = None
            self.next = None
            return value

        temp = self
        while temp.next.next:
            temp = temp.next
        value = temp.next.val
        temp.next = None
        return value

    def push(self, val: Any) -> None:
        """
        Add node to the start of the list

        >>> LinkedList = Node(1)
        >>> print(LinkedList)
        [1]
        >>> LinkedList.push(2)
        >>> print(LinkedList)
        [2, 1]

        :param val: The value to be added to the start of the list
        :return: None
        """
        if self.val is None:
            self.val = val
            return

        node = Node(val)
        node.next = self.next
        self.next = node
        self.val, self.next.val = self.next.val, self.val
        return

    def __reversed__(self) -> 'Node':
        """
         Reverse the list

        >>> LinkedList = Node(1)
        >>> LinkedList.append(2)
        >>> print(LinkedList)
        [1, 2]
        >>> reversed_list = reversed(LinkedList)
        >>> print(reversed_list)
        [2, 1]

        :return: Head of the reversed list
        """
        if self.val is None:
            return self

        if self.next is None:
            return self

        prev = None
        current = self
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def __iter__(self) -> 'Node':
        """
        returns a standard Iterator object

        >>> LinkedList = Node(1)
        >>> LinkedList.append(2)
        >>> print(LinkedList)
        [1, 2]
        >>> iterator = iter(LinkedList)
        >>> next(iterator)
        1
        >>> next(iterator)
        2
        >>> next(iterator)
        Traceback (most recent call last):
            ...
        StopIteration

        :return:
        """
        self.current = self
        return self

    def __next__(self) -> Any:
        """
        Next value of an iterator object

        >>> LinkedList = Node(1)
        >>> LinkedList.append(2)
        >>> print(LinkedList)
        [1, 2]
        >>> iterator = iter(LinkedList)
        >>> next(iterator)
        1
        >>> next(iterator)
        2
        >>> next(iterator)
        Traceback (most recent call last):
            ...
        StopIteration

        :return: Value of the next node
        """
        if self.current is None:
            raise StopIteration

        temp = self.current
        self.current = temp.next
        return temp.val

    def __str__(self) -> str:
        """
        A list Representation of the LinkedList

        >>> LinkedList = Node(1)
        >>> LinkedList.append(2)
        >>> print(LinkedList)
        [1, 2]

        :return: A string representation of the list
        """
        self_list = []
        if self.val is None:
            return str(self_list)
        temp = self
        while temp:
            self_list.append(temp.val)
            temp = temp.next
        return str(self_list)

    def __repr__(self) -> str:
        """
        Representation of the LinkedList

        >>> LinkedList = Node(10)
        >>> LinkedList.append(20)
        >>> LinkedList.append(30)
        >>> LinkedList
        10->20->30
        >>> reversed_list = reversed(LinkedList)
        >>> reversed_list
        30->20->10

        :return: A string representation of the LinkedList
        """
        return "->".join(str(i) for i in self)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
