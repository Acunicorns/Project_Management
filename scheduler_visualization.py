class ProcessManager:
    def __init__(self):
        self.queue = []

    def add_process(self, pid):
        self.queue.append(pid)

    def visualize_queue(self):
        """Visualize the scheduler queue in console."""
        print("Scheduler Queue:", " -> ".join(map(str, self.queue)) if self.queue else "Empty")

# Example usage
if __name__ == "__main__":
    pm = ProcessManager()
    pm.add_process(1)  # Rendering process
    pm.add_process(2)  # Audio process
    pm.visualize_queue()  # Output: Scheduler Queue: 1 -> 2
    pm.add_process(3)  # Input process
    pm.visualize_queue()  # Output: Scheduler Queue: 1 -> 2 -> 3