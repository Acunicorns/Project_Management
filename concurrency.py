class Thread:
    def __init__(self, thread_id, task):
        self.thread_id = thread_id
        self.task = task
        self.state = "Idle"

    def start(self):
        """Start the thread to execute the task."""
        self.state = "Running"
        # Simulate task execution (e.g., reading controller input)
        print(f"Thread {self.thread_id} executing {self.task}")

    def stop(self):
        """Stop the thread."""
        self.state = "Stopped"

class ThreadAPI:
    def __init__(self):
        self.threads = {}

    def create_thread(self, thread_id, task):
        """Create a new thread for a controller task."""
        self.threads[thread_id] = Thread(thread_id, task)
        return self.threads[thread_id]

    def run_thread(self, thread_id):
        """Run the specified thread."""
        if thread_id in self.threads:
            self.threads[thread_id].start()

# Example usage
if __name__ == "__main__":
    api = ThreadAPI()
    api.create_thread(1, "Read joystick input")
    api.run_thread(1)  # Output: Thread 1 executing Read joystick input