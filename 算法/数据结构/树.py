class Node:
    def __init__(self,name,type='dir'):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None
        # 链式存储
#模拟文件系统
class FileSystemTree:
    def __init__(self):
        self.root = Node("/")
        self.now = self.root


    def mkdir(self,name):
        # name 以斜杠结尾
        if name[-1] != "/":
            name += "/"
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self,name):
        if name [-1] != "/":
            name += "/"
        if name == "../":
            self.now = self.now.parent
            return
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        raise  ValueError("invalid dir")

