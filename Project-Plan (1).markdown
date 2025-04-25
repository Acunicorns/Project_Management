# Game Console OS Simulation Project Plan

## Project Overview
This project simulates a game console operating system optimized for low-latency process management, efficient memory allocation, concurrent handling of game inputs, and a file system for game assets. The system is developed in Python, using GitHub for version control and task management.

## Work Breakdown Structure (WBS)
- **1. Process Management** (Completed)
  - 1.1 Design Process Control Block (PCB) for game processes (#1)
  - 1.2 Implement process creation, switching, and termination (#2)
  - 1.3 Implement a Round Robin scheduler with low-latency for game tasks (#3)
- **2. Memory Management** (Completed)
  - 2.1 Implement paging for game asset memory allocation (#4)
  - 2.2 Simulate address translation using page tables (#5)
- **3. Concurrency & Synchronization** (Completed)
  - 3.1 Design a thread API for controller input handling (#6)
  - 3.2 Implement locks and condition variables (#7)
  - 3.3 Simulate Producer-Consumer problem for game input/output (#8)
- **4. File System** (Completed)
  - 4.1 Design a directory structure for game save files and assets (#9)
  - 4.2 Implement file creation, reading, writing, deletion (#10)
- **5. Bonus Features** (Completed)
  - 5.1 Visualization of process scheduling queues (#11)
  - 5.2 Simulated multi-core CPU for parallel game tasks (#12)

## Timeline
| Milestone                     | Planned Date | Status      |
|-------------------------------|--------------|-------------|
| Process Management Complete   | 2025-05-10   | Completed   |
| Memory Management Complete    | 2025-05-23   | Completed   |
| Concurrency Complete          | 2025-05-30   | Completed   |
| File System Complete          | 2025-06-05   | Completed   |
| Bonus Features Complete       | 2025-06-10   | Completed   |
| Final Report and Presentation | 2025-06-15   | In Progress |

## Resources
- **Programming Language**: Python 3.9+
- **Tools**: GitHub (Repository and Issues), Visual Studio Code
- **Team**: 5 members, each contributing 10-15 hours/week
- **Hardware**: Standard laptops for development and simulation

## Task Management
All tasks (#1 to #14) have been completed and tracked using GitHub Issues. Commits reference issue numbers (e.g., `#1` for PCB design). The project is now preparing for the final report and presentation.

## Risks
| Risk                              | Mitigation                     | Status    |
|-----------------------------------|--------------------------------|-----------|
| Scheduler latency issues          | Optimized Round Robin (#13)    | Resolved  |
| Memory allocation inefficiencies  | Added priority scheduling (#14) | Resolved  |
| Concurrency bugs in threads       | Early testing with small datasets | Resolved |

## Stakeholders
| Stakeholder | Role                | Involvement                     |
|-------------|---------------------|---------------------------------|
| Team        | Developers          | Implemented and tested OS components |
| Instructor  | Evaluator           | Review deliverables and demo    |
