class Lock:
    def _init_(self):
        self.locked = False

    def acquire(self):
        if not self.locked:
            self.locked = True
            return True
        return False

    def release(self):
        self.locked = False

class ConditionVariable:
    def _init_(self):
        self.waiting_threads = []

    def wait(self, thread_id):
        self.waiting_threads.append(thread_id)

    def signal(self):
        if self.waiting_threads:
            return self.waiting_threads.pop(0)
        return None

class ProducerConsumer:
    def _init_(self, buffer_size):
        self.buffer = []
        self.buffer_size = buffer_size
        self.lock = Lock()
        self.not_full = ConditionVariable()
        self.not_empty = ConditionVariable()

    def produce(self, thread_id, item):
        """Produce an item (e.g., controller input)."""
        while len(self.buffer) >= self.buffer_size:
            self.not_full.wait(thread_id)
        if self.lock.acquire():
            self.buffer.append(item)
            print(f"Thread {thread_id} produced {item}")
            self.lock.release()
            self.not_empty.signal()

    def consume(self, thread_id):
        """Consume an item (e.g., game logic processing)."""
        while not self.buffer:
            self.not_empty.wait(thread_id)
        if self.lock.acquire():
            item = self.buffer.pop(0)
            print(f"Thread {thread_id} consumed {item}")
            self.lock.release()
            self.not_full.signal()
            return item

# Example usage
if _name_ == "_main_":
    pc = ProducerConsumer(3)
    pc.produce(1, "Joystick input")  # Thread 1 produces
    pc.consume(2)  # Thread 2 consumes
