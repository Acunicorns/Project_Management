class FileSystemNode:
    def _init_(self, name, is_directory=False):
        self.name = name
        self.is_directory = is_directory
        self.children = {} if is_directory else None
        self.content = "" if not is_directory else None

class FileSystem:
    def _init_(self):
        self.root = FileSystemNode("/", is_directory=True)

    def create_directory(self, path):
        """Create a directory at the specified path."""
        node = self._navigate_path(path)
        if not node:
            parts = path.strip("/").split("/")
            current = self.root
            for part in parts:
                if part not in current.children:
                    current.children[part] = FileSystemNode(part, is_directory=True)
                current = current.children[part]

    def create_file(self, path, content=""):
        """Create a file with optional content."""
        parts = path.strip("/").split("/")
        dir_path = "/".join(parts[:-1])
        file_name = parts[-1]
        directory = self._navigate_path(dir_path)
        if directory and directory.is_directory and file_name not in directory.children:
            directory.children[file_name] = FileSystemNode(file_name)
            directory.children[file_name].content = content

    def read_file(self, path):
        """Read the content of a file."""
        node = self._navigate_path(path)
        if node and not node.is_directory:
            return node.content
        return None

    def write_file(self, path, content):
        """Write content to a file."""
        node = self._navigate_path(path)
        if node and not node.is_directory:
            node.content = content

    def delete_file(self, path):
        """Delete a file."""
        parts = path.strip("/").split("/")
        dir_path = "/".join(parts[:-1])
        file_name = parts[-1]
        directory = self._navigate_path(dir_path)
        if directory and file_name in directory.children:
            del directory.children[file_name]

    def _navigate_path(self, path):
        """Navigate to the node at the given path."""
        parts = path.strip("/").split("/")
        current = self.root
        for part in parts:
            if not current.is_directory or part not in current.children:
                return None
            current = current.children[part]
        return current

# Example usage
if _name_ == "_main_":
    fs = FileSystem()
    fs.create_directory("/saves/game1")
    fs.create_file("/saves/game1/save.dat", "Player progress: Level 5")
    print(fs.read_file("/saves/game1/save.dat"))  # Output: Player progress: Level 5
    fs.write_file("/saves/game1/save.dat", "Player progress: Level 6")
    fs.delete_file("/saves/game1/save.dat")
