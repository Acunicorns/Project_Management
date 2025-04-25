class PCB:
    def __init__(self, pid, priority):
        self.pid = pid
        self.state = "Ready"
        self.priority = priority
        self.registers = {}
        self.program_counter = 0

class ProcessManager:
    def __init__(self):
        self.processes = {}
        self.queue = []

    def create_process(self, pid, priority):
        """Create a new process with given PID and priority."""
        self.processes[pid] = PCB(pid, priority)
        self.queue.append(pid)
        return self.processes[pid]

    def switch_process(self, current_pid, next_pid):
        """Switch between two processes, saving and restoring states."""
        if current_pid in self.processes:
            self.processes[current_pid].state = "Waiting"
        if next_pid in self.processes:
            self.processes[next_pid].state = "Running"

    def round_robin_schedule(self, time_quantum):
        """Run Round Robin scheduling with given time quantum."""
        if not self.queue:
            return
        current_pid = self.queue.pop(0)
        self.processes[current_pid].state = "Running"
        # Simulate execution for time_quantum
        self.processes[current_pid].state = "Waiting"
        self.queue.append(current_pid)

# Example usage
if __name__ == "__main__":
    pm = ProcessManager()
    pm.create_process(1, 1)  # High-priority rendering process
    pm.create_process(2, 3)  # Lower-priority audio process
    pm.round_robin_schedule(10)  # 10ms time quantum