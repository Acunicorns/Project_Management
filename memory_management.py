class PageTable:
    def _init_(self):
        self.pages = {}  # Maps virtual page to physical frame

    def allocate_page(self, virtual_page, physical_frame):
        """Allocate a page for a game asset."""
        self.pages[virtual_page] = physical_frame

    def get_physical_address(self, virtual_page):
        """Get physical address for a virtual page."""
        if virtual_page not in self.pages:
            raise ValueError("Page fault: Virtual page not allocated")
        return self.pages[virtual_page]

    def translate_address(self, virtual_address):
        """Translate virtual address to physical address."""
        page_size = 4096  # 4KB pages
        virtual_page = virtual_address // page_size
        offset = virtual_address % page_size
        physical_frame = self.get_physical_address(virtual_page)
        if physical_frame is None:
            return None  # Page fault
        return physical_frame * page_size + offset

# Example usage
if _name_ == "_main_":
    pt = PageTable()
    pt.allocate_page(1, 100)  # Allocate texture data
    physical_addr = pt.translate_address(4096)  # Virtual address = 4096
    print(physical_addr)  # Output: 409600 (100 * 4096)
