class Directory:

    def __init__(
        self,
        name,
        path,
        # directories,
        # files
    ):
        self.name = name
        self.path = path
        self.directories = []
        self.files = []
        self.size = 0

    def add_child_directory(self,d):
        self.directories.append(d)
    
    def add_file(self,f):
        self.files.append(f)

    def get_size(self):
        size = 0
        for file in self.files:
            size += file.get_size()
        for directory in self.directories:
            size += directory.get_size()
        self.size = size
        return size

class File:

    def __init__(
        self,
        name,
        size
    ):
        self.name = name
        self.size = size
    
    def get_size(self):
        return self.size