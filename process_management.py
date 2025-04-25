class PCB:
    def _init_(self, pid, priority):
        self.pid = pid
        self.state = "Ready"
        self.priority = priority
        self.registers = {}
        self.program_counter = 0

class ProcessManager:
    def _init_(self):
        self.processes = {}
        self.queue = []

    def create_process(self, pid, priority):
        """Create a new process with given PID and priority."""
        self.processes[pid] = PCB(pid, priority)
        self.queue.append(pid)
        return self.processes[pid]

    def switch_process(self, current_pid, next_pid):
        """Optimized switch between two processes."""
        if current_pid in self.processes:
            self.processes[current_pid].state = "Waiting"
            self.processes[current_pid].registers = {"optimized": True}
        if next_pid in self.processes:
            self.processes[next_pid].state = "Running"

    def round_robin_schedule(self, time_quantum):
        """Run Round Robin with priority-based scheduling."""
        if not self.queue:
            return
        # Sort queue by priority (lower number = higher priority)
        self.queue.sort(key=lambda pid: self.processes[pid].priority)
        current_pid = self.queue.pop(0)
        self.processes[current_pid].state = "Running"
        # Simulate execution for time_quantum
        self.processes[current_pid].state = "Waiting"
        self.queue.append(current_pid)

# Example usage
if _name_ == "_main_":
    pm = ProcessManager()
    pm.create_process(1, 1)  # High-priority rendering process
    pm.create_process(2, 3)  # Lower-priority audio process
    pm.round_robin_schedule(10)  # 10ms time quantum
