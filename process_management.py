class PCB:
    def __init__(self, pid, priority):
        self.pid = pid
        self.state = "Ready"
        self.priority = priority
        self.registers = {}
        self.program_counter = 0

class ProcessManager:
    def __init__(self, num_cores=2):
        self.processes = {}
        self.cores = [[] for _ in range(num_cores)]  # Each core has its own queue
        self.num_cores = num_cores

    def create_process(self, pid, priority):
        """Create a new process and assign to a core."""
        self.processes[pid] = PCB(pid, priority)
        # Assign to core with least processes
        min_core = min(range(self.num_cores), key=lambda i: len(self.cores[i]))
        self.cores[min_core].append(pid)
        return self.processes[pid]

    def round_robin_schedule(self, time_quantum):
        """Run Round Robin scheduling across multiple cores."""
        for core_id in range(self.num_cores):
            if self.cores[core_id]:
                current_pid = self.cores[core_id].pop(0)
                self.processes[current_pid].state = "Running"
                print(f"Core {core_id} running process {current_pid}")
                self.processes[current_pid].state = "Waiting"
                self.cores[core_id].append(current_pid)

# Example usage
if __name__ == "__main__":
    pm = ProcessManager(num_cores=2)
    pm.create_process(1, 1)  # Rendering process
    pm.create_process(2, 3)  # Audio process
    pm.round_robin_schedule(10)  # Simulate multi-core scheduling
