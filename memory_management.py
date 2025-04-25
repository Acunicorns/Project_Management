class PageTable:
    def __init__(self):
        self.pages = {}  # Maps virtual page to physical frame

    def allocate_page(self, virtual_page, physical_frame):
        """Allocate a page for a game asset."""
        self.pages[virtual_page] = physical_frame

    def get_physical_address(self, virtual_page):
        """Get physical address for a virtual page."""
        return self.pages.get(virtual_page, None)

# Example usage
if __name__ == "__main__":
    pt = PageTable()
    pt.allocate_page(1, 100)  # Allocate texture data
    print(pt.get_physical_address(1))  # Output: 100