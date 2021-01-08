class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None

    def Insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__Insert(self.root, value)

    def __Insert(self, root, value):

        if value < root.value:
            if root.left:
                self.__Insert(root.left, value)
            else:
                root.left = Node(value)
        else:
            if root.right:
                self.__Insert(root.right, value)
            else:
                root.right = Node(value)

    def InOrder(self):
        return self.__InOrder(self.root)

    def __InOrder(self, root):
        if root is not None:
            self.__InOrder(root.left)
            print(root.value)
            self.__InOrder(root.right)

    def PreOrder(self):
        return self.__PreOrder(self.root)

    def __PreOrder(self, root):
        if root is not None:
            print(root.value)
            self.__PreOrder(root.left)
            self.__PreOrder(root.right)


    def PostOrder(self):
        return self.__PostOrder(self.root)

    def __PostOrder(self, root):
        if root is not None:
            self.__PostOrder(root.left)
            self.__PostOrder(root.right)
            print(root.value)

    def FindMin(self):
        return self.__FindMin(self.root)

    def __FindMin(self, root):
        if root is None:
            return 0
        elif root.left is None:
            return root.value
        else:
            return self.__FindMin(root.left)

    def FindMax(self):
        return self.__FindMax(self.root)

    def __FindMax(self, root):
        if root is None:
            return 0
        elif root.right is None:
            return root.value
        else:
            return self.__FindMax(root.right)

    def Successor(self):
        return self.__Successor(self.root)

    def __Successor(self, root):
        if root.right is not None:
            return self.__FindMin(root.right)

    def Predeccessor(self):
        return self.__Predeccessor(self.root)

    def __Predeccessor(self, root):
        if root.left is not None:
            return self.__FindMax(root.left)

    def Height(self):
        return self.__Height(self.root)

    def __Height(self, root):

        if root is None:
            return 0
        return max(self.__Height(root.left), self.__Height(root.right)) + 1

    def Delete(self, value):
        return self.__Delete(self.root, value)

    def __Delete(self, root, value):
        if root is None:
            return root

        if value < root.value:
            root.left = self.__Delete(root.left, value)

        elif value > root.value:
            root.right = self.__Delete(root.right, value)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.__FindMin(root.right)
            root.value = temp.value
            root.right = self.__Delete(root.right, temp.value)
        return root

obj = BST()
obj.Insert(5)
obj.Insert(3)
obj.Insert(23)
obj.Insert(6)
obj.Insert(9)



obj.InOrder()
print()
obj.PreOrder()
print()
obj.PostOrder()
obj.Delete(9)
print()
obj.InOrder()
#
print(obj.Height())
#
print(obj.FindMax())
print()
print(obj.FindMin())
print(obj.Successor())
print(obj.Predeccessor())