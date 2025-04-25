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

    def create_process(self, pid, priority):
        """Create a new process with given PID and priority."""
        self.processes[pid] = PCB(pid, priority)
        return self.processes[pid]

    def switch_process(self, current_pid, next_pid):
        """Switch between two processes, saving and restoring states."""
        if current_pid in self.processes:
            self.processes[current_pid].state = "Waiting"
        if next_pid in self.processes:
            self.processes[next_pid].state = "Running"

# Example usage
if __name__ == "__main__":
    pm = ProcessManager()
    pm.create_process(1, 1)  # High-priority rendering process
    pm.create_process(2, 3)  # Lower-priority audio process
    pm.switch_process(1, 2)