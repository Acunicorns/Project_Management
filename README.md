# Game Console Operating System Simulation


## Overview
This project simulates a lightweight operating system (OS) for a game console, implementing core OS components: process management, memory management, concurrency, and a file system. The game console theme ensures low-latency process scheduling, efficient memory allocation for game assets, real-time input handling, and persistent storage for save files. The project is developed in Python and managed using GitHub for version control and task tracking.

## Features
- **Process Management**: Round Robin scheduler with priority-based scheduling for game tasks (#1, #2, #3, #13, #14).
- **Memory Management**: Paging and address translation for game assets (#4, #5).
- **Concurrency**: Thread API, locks, and Producer-Consumer simulation for controller inputs (#6, #7, #8).
- **File System**: Hierarchical directory structure and file operations for save files and textures (#9, #10).
- **Bonus Features**: Scheduler queue visualization and multi-core CPU simulation (#11, #12).

## Installation
1. **Clone the Repository**:

2. **Requirements**:
   - Python 3.9+
   - No external libraries required (standard Python only).

3. **Run Tests**:
   - See `Tests.md` for test scenarios.
   - Example:
     ```sh
     python process_management.py
     python memory_management.py
     ```

## Project Structure
| File/Folder                  | Description                              |
|------------------------------|------------------------------------------|
| `process_management.py`      | Process creation, scheduling, multi-core |
| `memory_management.py`       | Paging and address translation           |
| `concurrency.py`             | Thread API, locks, Producer-Consumer      |
| `file_system.py`             | File system and file operations          |
| `scheduler_visualization.py` | Scheduler queue visualization             |
| `PCB-Design.md`              | Process Control Block design (#1)        |
| `File-System-Design.md`      | File system design (#9)                  |
| `Multi-Core-Design.md`       | Multi-core CPU design (#12)              |
| `Project-Goal.md`            | Project objectives                       |
| `Project-Plan.md`            | Work breakdown, timeline, risks          |
| `Task-Assignments.md`        | Task assignments for team members        |
| `Final-Report.md`            | Final project report                     |
| `Tests.md`                   | Test scenarios for all modules           |

## Usage Examples
1. **Run Scheduler**:
   ```python
   from process_management import ProcessManager
   pm = ProcessManager(num_cores=2)
   pm.create_process(1, 1)  # Rendering
   pm.create_process(2, 3)  # Audio
   pm.round_robin_schedule(10)
   ```

2. **Manage Files**:
   ```python
   from file_system import FileSystem
   fs = FileSystem()
   fs.create_directory("/saves/game1")
   fs.create_file("/saves/game1/save.dat", "Level 5")
   print(fs.read_file("/saves/game1/save.dat"))  # Output: Level 5
   ```

3. **Visualize Queue**:
   ```python
   from scheduler_visualization import ProcessManager
   pm = ProcessManager()
   pm.add_process(1)
   pm.add_process(2)
   pm.visualize_queue()  # Output: Scheduler Queue: 1 -> 2
   ```

## Testing
Refer to `Tests.md` for detailed test scenarios covering all modules. Run each test to verify functionality:
```sh
python memory_management.py
python concurrency.py
```

## Contributing
- Track tasks and issues in GitHub Issues (#1-#20).
- Use commit messages with issue numbers (e.g., `git commit -m "Implemented file operations #10"`).
- Update `Progress-Report.md` for weekly progress (if applicable).

## Authors
- Pelin Ece Burgun
- İrem Aras
- Oğulcan Zorba
- Sena Küçüksaraç
- Furkan Küçük



## License
This project is for educational purposes and not licensed for commercial use.

**Commit**: `git commit -m "Added README and test scenarios #20"`
