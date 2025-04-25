class FileSystemNode:
    def __init__(self, name, is_directory=False):
        self.name = name
        self.is_directory = is_directory
        self.children = {} if is_directory else None
        self.content = "" if not is_directory else None

class FileSystem:
    def __init__(self):
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
if __name__ == "__main__":
    fs = FileSystem()
    fs.create_directory("/saves/game1")  # Directory for game save files
    print(fs.root.children["saves"].children["game1"].name)  # Output: game1