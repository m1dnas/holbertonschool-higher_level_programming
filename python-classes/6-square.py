#!/usr/bin/python3
"""Square module: task 6 of the project python-classes"""


class Square:
    """a square class"""
    def __init__(self, size=0, position=(0,0)):
        """the private instance size attribute w/ validation"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        """return the size of the square"""
        return(self.__size)

    @size.setter
    def size(self, size):
        """set the size of the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """prints the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character '#'"""
        position = (0, 0)
        if self.__position[1] > 0:
            print("")
        if self.__size >= 0:
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(end=" ")
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
