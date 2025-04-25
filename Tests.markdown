# Test Scenarios for Game Console OS Simulation

This document provides test scenarios to validate the functionality of the Game Console OS simulation. Each test is linked to a specific module and GitHub Issue.

**Related Issue**: #20 (Test Scenarios)

## 1. Memory Management (#5)
**File**: `memory_management.py`  
**Objective**: Test address translation and page fault handling.  
**Test Scenario**:
- Create a `PageTable` instance.
- Allocate two pages: virtual page 1 to physical frame 100, virtual page 2 to physical frame 200.
- Access virtual page 3 (should trigger a page fault and allocate a new frame).
- Verify the physical address of page 3.

**Steps**:
```python
pt = PageTable()
pt.allocate_page(1, 100)
pt.allocate_page(2, 200)
print(pt.get_physical_address(3))  # Should allocate new frame (e.g., 101)
```

**Expected Output**:
```
101
```

**Pass Criteria**: Page fault is handled, and a new physical frame is allocated.

---

## 2. Concurrency - Thread API (#6)
**File**: `concurrency.py`  
**Objective**: Test thread creation and execution for controller inputs.  
**Test Scenario**:
- Create a `ThreadAPI` instance.
- Create two threads: one for "Joystick input" and one for "Button input."
- Run both threads and verify their execution.

**Steps**:
```python
api = ThreadAPI()
api.create_thread(1, "Joystick input")
api.create_thread(2, "Button input")
api.run_thread(1)
api.run_thread(2)
```

**Expected Output**:
```
Thread 1 executing Joystick input
Thread 2 executing Button input
```

**Pass Criteria**: Both threads execute their tasks without errors.

---

## 3. Concurrency - Locks and Condition Variables (#7)
**File**: `concurrency.py`  
**Objective**: Test synchronization with locks and condition variables.  
**Test Scenario**:
- Create a `ThreadAPI` instance with a lock.
- Run two threads attempting to acquire the lock.
- Verify that the second thread waits until the lock is released.

**Steps**:
```python
api = ThreadAPI()
api.create_thread(1, "Joystick input")
api.create_thread(2, "Button input")
api.run_thread(1)  # Acquires lock
api.run_thread(2)  # Should wait
```

**Expected Output**:
```
Thread 1 executing Joystick input
Thread 2 executing Button input
```

**Pass Criteria**: Second thread waits for the lock, ensuring no race conditions.

---

## 4. Concurrency - Producer-Consumer Problem (#8)
**File**: `concurrency.py`  
**Objective**: Test synchronized data flow between producers and consumers.  
**Test Scenario**:
- Create a `ProducerConsumer` instance with a buffer size of 2.
- Produce three items: "Joystick input 1," "Joystick input 2," "Joystick input 3."
- Consume two items and verify the buffer state.

**Steps**:
```python
pc = ProducerConsumer(2)
pc.produce(1, "Joystick input 1")
pc.produce(1, "Joystick input 2")
pc.consume(2)
pc.consume(2)
```

**Expected Output**:
```
Thread 1 produced Joystick input 1
Thread 1 produced Joystick input 2
Thread 2 consumed Joystick input 1
Thread 2 consumed Joystick input 2
```

**Pass Criteria**: Buffer respects size limit, and items are produced/consumed in order.

---

## 5. File System - Directory Structure (#9)
**File**: `file_system.py`  
**Objective**: Test hierarchical directory creation.  
**Test Scenario**:
- Create a `FileSystem` instance.
- Create directories: `/saves/game1` and `/assets/textures`.
- Verify the directory structure.

**Steps**:
```python
fs = FileSystem()
fs.create_directory("/saves/game1")
fs.create_directory("/assets/textures")
print(fs.root.children["saves"].children["game1"].name)
print(fs.root.children["assets"].children["textures"].name)
```

**Expected Output**:
```
game1
textures
```

**Pass Criteria**: Directories are created and accessible.

---

## 6. File System - File Operations (#10)
**File**: `file_system.py`  
**Objective**: Test file creation, reading, writing, and deletion.  
**Test Scenario**:
- Create a file `/saves/game1/save.dat` with content "Level 5".
- Read the file content.
- Update the content to "Level 6".
- Delete the file and verify it’s gone.

**Steps**:
```python
fs = FileSystem()
fs.create_directory("/saves/game1")
fs.create_file("/saves/game1/save.dat", "Level 5")
print(fs.read_file("/saves/game1/save.dat"))
fs.write_file("/saves/game1/save.dat", "Level 6")
print(fs.read_file("/saves/game1/save.dat"))
fs.delete_file("/saves/game1/save.dat")
print(fs.read_file("/saves/game1/save.dat"))
```

**Expected Output**:
```
Level 5
Level 6
None
```

**Pass Criteria**: File operations work as expected, and deletion removes the file.

---

## 7. Scheduler Queue Visualization (#11)
**File**: `scheduler_visualization.py`  
**Objective**: Test visualization of process queues.  
**Test Scenario**:
- Create a `ProcessManager` instance.
- Add three processes (PIDs 1, 2, 3).
- Visualize the queue after each addition.

**Steps**:
```python
pm = ProcessManager()
pm.add_process(1)
pm.visualize_queue()
pm.add_process(2)
pm.visualize_queue()
pm.add_process(3)
pm.visualize_queue()
```

**Expected Output**:
```
Scheduler Queue: 1
Scheduler Queue: 1 -> 2
Scheduler Queue: 1 -> 2 -> 3
```

**Pass Criteria**: Queue visualization correctly reflects the process order.

---

## 8. Multi-Core CPU Simulation (#12)
**File**: `process_management.py`  
**Objective**: Test process distribution across multiple cores.  
**Test Scenario**:
- Create a `ProcessManager` instance with 2 cores.
- Add three processes (PIDs 1, 2, 3).
- Run one scheduling cycle and verify core assignments.

**Steps**:
```python
pm = ProcessManager(num_cores=2)
pm.create_process(1, 1)
pm.create_process(2, 3)
pm.create_process(3, 2)
pm.round_robin_schedule(10)
```

**Expected Output**:
```
Core 0 running process 1
Core 1 running process 2
```

**Pass Criteria**: Processes are distributed across cores, and each core runs a process.

---

## Notes
- Run tests in a Python 3.9+ environment.
- Ensure all files (`process_management.py`, `memory_management.py`, etc.) are in the same directory.
- Log any unexpected outputs in GitHub Issues for debugging.

**Commit**: `git commit -m "Added test scenarios #20"`