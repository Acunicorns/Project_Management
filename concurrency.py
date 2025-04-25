class Lock:
    def __init__(self):
        self.locked = False

    def acquire(self):
        """Acquire the lock."""
        if not self.locked:
            self.locked = True
            return True
        return False

    def release(self):
        """Release the lock."""
        self.locked = False

class ConditionVariable:
    def __init__(self):
        self.waiting_threads = []

    def wait(self, thread_id):
        """Put thread in waiting state."""
        self.waiting_threads.append(thread_id)

    def signal(self):
        """Signal one waiting thread."""
        if self.waiting_threads:
            return self.waiting_threads.pop(0)
        return None

class ThreadAPI:
    def __init__(self):
        self.threads = {}
        self.lock = Lock()
        self.condition = ConditionVariable()

    def create_thread(self, thread_id, task):
        """Create a new thread for a controller task."""
        self.threads[thread_id] = Thread(thread_id, task)
        return self.threads[thread_id]

    def run_thread(self, thread_id):
        """Run the specified thread with synchronization."""
        if self.lock.acquire():
            self.threads[thread_id].start()
            self.lock.release()
        else:
            self.condition.wait(thread_id)
            self.run_thread(thread_id)

# Example usage
if __name__ == "__main__":
    api = ThreadAPI()
    api.create_thread(1, "Read joystick input")
    api.create_thread(2, "Process button input")
    api.run_thread(1)  # Runs with lock
    api.run_thread(2)  # Waits if lock is held
