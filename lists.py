from typing import Any


class Node:
    """
    An implementation of a list using LinkedList
    Also works as an Iterator
    """

    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

    def append(self, data: Any) -> None:
        """
        Add node to the end of the list
        This is a recursive method may take long time for appending for a large list

        >>> LinkedList = Node()
        >>> LinkedList.append(1)
        >>> LinkedList
        [1]
        >>> LinkedList.append(2)
        >>> LinkedList
        [1, 2]

        :param data: The value to be added to the end of the list
        :return: None
        """
        if self.data is None:
            self.data = data
            return

        if self.next is None:
            self.next = Node(data)
            return

        self.next.append(data)

    def pop(self) -> Any:
        """
        Remove a node from the end of the list

        >>> LinkedList = Node(1)
        >>> LinkedList.append(2)
        >>> LinkedList
        [1, 2]
        >>> LinkedList.pop()
        2
        >>> LinkedList.pop()
        1
        >>> LinkedList
        []
        >>> LinkedList.pop()
        Traceback (most recent call last):
            ...
        IndexError: Can't pop from empty list

        :return: The value of the popped node
        """

        if self.data is None:
            raise IndexError("Can't pop from empty list")

        if self.next is None:
            value = self.data
            self.data = None
            self.next = None
            return value

        temp = self
        while temp.next.next:
            temp = temp.next
        value = temp.next.data
        temp.next = None
        return value

    def push(self, data: Any) -> None:
        """
        Add node to the start of the list

        >>> LinkedList = Node(1)
        >>> LinkedList
        [1]
        >>> LinkedList.push(2)
        >>> LinkedList
        [2, 1]

        :param data: The value to be added to the start of the list
        :return: None
        """
        if self.data is None:
            self.data = data
            return

        node = Node(data)
        node.next = self.next
        self.next = node
        self.data, self.next.data = self.next.data, self.data
        return

    def __reversed__(self) -> 'Node':
        """
         Reverse the list

        >>> LinkedList = Node(1)
        >>> LinkedList.append(2)
        >>> LinkedList
        [1, 2]
        >>> reversed_list = reversed(LinkedList)
        >>> reversed_list
        [2, 1]

        :return: Head of the reversed list
        """
        if self.data is None:
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
        >>> LinkedList
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
        >>> LinkedList
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
        return temp.data

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
        if self.data is None:
            return str(self_list)
        temp = self
        while temp:
            self_list.append(temp.data)
            temp = temp.next
        return str(self_list)

    def __repr__(self) -> str:
        """
        same as __str__() method

        :return: A string representation of the LinkedList
        """
        return self.__str__()


if __name__ == '__main__':
    import doctest

    doctest.testmod()
