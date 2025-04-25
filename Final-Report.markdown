# Mini Operating System Simulation Project: Game Console OS

## 1. Introduction
The Mini Operating System Simulation Project aimed to design and implement a simulated operating system (OS) tailored for a game console. The OS supports low-latency process management, efficient memory allocation, concurrent handling of controller inputs, and a file system for game assets. The game console theme guided our design to prioritize real-time performance and seamless user interaction. This report outlines the system’s design, its alignment with OS principles, and the influence of the game console theme.

**Related Issue**: #16 (Final Report)

## 2. System Design and Implementation

### 2.1 Process Management
**Objective**: Simulate process creation, switching, and scheduling for game tasks (e.g., rendering, audio processing).  
**Design Decisions**:
- **Process Control Block (PCB)** (#2): Designed a lightweight PCB with fields for process ID, state, priority, registers, and program counter. The priority field ensured critical game tasks (e.g., rendering) were prioritized.
- **Process Creation and Switching** (#3): Implemented in `process_management.py` to create and switch processes efficiently, minimizing latency for real-time tasks.
- **Round Robin Scheduler** (#4, #14, #15): Adopted a Round Robin scheduler with a 10ms time quantum, optimized with priority-based scheduling to handle high-priority game processes first.

**OS Principles**:  
- **Process Isolation**: Each PCB maintains independent process states, ensuring no interference between tasks.
- **Scheduling**: Round Robin ensures fairness, while priority-based scheduling (added in #14) aligns with real-time requirements.

**Theme Influence**: The scheduler prioritizes rendering and input processes to prevent gameplay lag, critical for a game console.

### 2.2 Memory Management
**Objective**: Manage memory allocation for game assets (e.g., textures, audio buffers).  
**Design Decisions**:
- **Paging** (#5): Implemented a paging system with 4KB pages in `memory_management.py` to allocate memory for large assets efficiently.
- **Address Translation** (#6): Simulated virtual-to-physical address translation using page tables, with a FIFO page replacement policy for page faults.

**OS Principles**:  
- **Virtual Memory**: Paging enables efficient memory use and isolation for game assets.
- **Fault Tolerance**: Page fault handling ensures robust memory access under resource constraints.

**Theme Influence**: Paging was optimized for large, frequently accessed game assets, ensuring fast loading times during gameplay.

### 2.3 Concurrency & Synchronization
**Objective**: Handle concurrent controller inputs and game logic processing.  
**Design Decisions**:
- **Thread API** (#7): Designed a lightweight thread API in `concurrency.py` for tasks like reading joystick inputs, documented in `Thread-API-Design.md`.
- **Locks and Condition Variables** (#8): Implemented synchronization primitives to prevent race conditions in shared resources (e.g., input buffers).
- **Producer-Consumer Problem** (#9): Simulated controller inputs (producers) and game logic (consumers) with a fixed-size buffer, ensuring synchronized data flow.

**OS Principles**:  
- **Concurrency**: Threads enable parallel execution of input and game tasks.
- **Synchronization**: Locks and condition variables ensure safe resource access.

**Theme Influence**: The thread API and synchronization mechanisms support real-time input handling, critical for responsive controls in a game console.

### 2.4 File System
**Objective**: Manage game assets like save files and textures.  
**Design Decisions**:
- **Directory Structure** (#10): Designed a hierarchical file system in `file_system.py`, with directories like `/saves` and `/assets`, documented in `File-System-Design.md`.
- **File Operations** (#11): Implemented file creation, reading, writing, and deletion for efficient asset management.

**OS Principles**:  
- **Hierarchical Storage**: The directory structure organizes assets logically.
- **File Abstraction**: File operations abstract storage details, simplifying asset access.

**Theme Influence**: The file system prioritizes fast access to save files and textures, ensuring seamless gameplay and persistence.

### 2.5 Bonus Features
**Objective**: Enhance the OS with creative additions.  
**Design Decisions**:
- **Scheduler Queue Visualization** (#12): Implemented a console-based visualization in `scheduler_visualization.py` to display process queue dynamics, aiding debugging and presentation.
- **Multi-Core CPU Simulation** (#13): Simulated a dual-core CPU in `process_management.py`, distributing processes across cores for parallel execution, documented in `Multi-Core-Design.md`.

**OS Principles**:  
- **Parallelism**: Multi-core simulation improves throughput for compute-intensive tasks.
- **Visualization**: Queue visualization enhances system transparency.

**Theme Influence**: Multi-core support boosts performance for rendering and audio, while visualization showcases the OS’s real-time scheduling for game tasks.

## 3. Alignment with Operating System Principles
The OS simulation adheres to core OS principles:
- **Resource Management**: Efficiently allocates CPU (via scheduling), memory (via paging), and storage (via file system) for game tasks.
- **Abstraction**: Provides abstractions like processes, virtual memory, and files to simplify game development.
- **Concurrency**: Supports parallel execution and synchronization for real-time input and game logic.
- **Fault Tolerance**: Handles page faults and synchronization errors robustly.

The design balances simplicity (for simulation) with realism (for game console needs), ensuring all components work cohesively.

## 4. Influence of the Game Console Theme
The game console theme shaped every aspect of the design:
- **Low Latency**: The Round Robin scheduler and optimized context switching (#14) prioritize rendering and input tasks to prevent gameplay lag.
- **Efficient Resource Use**: Paging and file systems were tailored for large, frequently accessed game assets like textures and save files.
- **Real-Time Inputs**: The thread API and Producer-Consumer simulation ensure responsive controller handling.
- **Parallel Processing**: Multi-core simulation enhances performance for compute-intensive game tasks, aligning with modern console architectures.

The theme made the project more engaging by grounding abstract OS concepts in a real-world use case, guiding decisions toward user-centric performance.

## 5. Challenges and Solutions
- **Challenge**: Slow context switching (#3) increased latency.  
  **Solution**: Optimized switching mechanism (#14) reduced latency to <1ms (simulated).
- **Challenge**: Round Robin scheduler lacked priority support (#4).  
  **Solution**: Added priority-based scheduling (#15) to prioritize critical game tasks.
- **Challenge**: Large page tables impacted performance (#5).  
  **Solution**: Completed paging efficiently, with future optimization potential noted.

These challenges were tracked and resolved using GitHub Issues, ensuring traceability and team coordination.

## 6. Conclusion
The Game Console OS simulation successfully implemented a lightweight, efficient operating system tailored for real-time gaming needs. By adhering to OS principles and leveraging the game console theme, the system achieves low-latency process management, robust memory handling, concurrent input processing, and efficient asset storage. The bonus features (visualization and multi-core support) added creativity and realism, making the project both educational and engaging. The use of GitHub for task management and version control ensured a structured development process, preparing the team for real-world software engineering practices.

## 7. Future Work
- **GUI Integration**: Add a graphical interface for the OS to visualize game processes and inputs.
- **Security Features**: Implement file permissions or encrypted save files for user data protection.
- **Extended Testing**: Conduct stress tests with larger datasets to validate scalability.

**Commit**: `git commit -m "Added final report #16"`
