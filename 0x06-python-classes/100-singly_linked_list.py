#!/usr/bin/python3


"""Defines a Node and Linked List"""


class Node:
    """ Defines a node
    """
    def __init__(self, data, next_node=None):
        """ definition of the node
        Args:
            self: object
            data(int): value at node
            next_node(Node): pointer to next node
        Returns: None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ data getter
        Args:
            Self: object
        Returns: data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """ data setter
        Args:
            self: object
            value(int): value at node
        Returns: Node
        """
        if not isinstance(value, int):
            raise TypeError("data must be of an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Node getter
        Args:
            Self: object
        Return: none
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Node setter
        Args:
            self: object
            value(Node): node to be st
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Defines a Singly linked list """
    def __init__(self) -> None:
        """ initializing of node
        Args:
            self: object
        """
        self.__head = None

    def __str__(self) -> str:
        """ setting up the linked list
        Args:
            Self: object
        Returns: linked list string
        """
        temp = self.__head
        strList = ""
        while (temp):
            strList += str(temp.data) + "\n"
            temp = temp.next_node
        return strList[:-1]

    def sorted_insert(self, value):
        """ Function to insert into linked like
            sorted
        Args:
            Self: Object
        Returns: None
        """
        newNode = Node(value)
        if not self.__head:
            self.__head = newNode
            return
        if value < self.__head.data:
            newNode.next_node = self.__head
            self.__head = newNode
            return
        temp = self.__head
        while (temp.next_node and temp.next_node.data < value):
            temp = temp.next_node
        if temp.next_node:
            newNode.next_node = temp.next_node
        temp.next_node = newNode
