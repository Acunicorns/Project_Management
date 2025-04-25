# Mini Operating System Simulation Project Plan

## Project Overview
This project simulates a game console operating system with low-latency process scheduling, efficient memory management, concurrency, and a file system for game assets.

## Work Breakdown Structure (WBS)
- **1. Process Management**
  - 1.1 Design Process Control Block (PCB)
  - 1.2 Implement process creation, switching, and termination
  - 1.3 Implement Round Robin scheduler
- **2. Memory Management**
  - 2.1 Implement paging and page tables
  - 2.2 Simulate address translation
- **3. Concurrency & Synchronization**
  - 3.1 Design thread API
  - 3.2 Implement locks and condition variables
  - 3.3 Simulate Producer-Consumer problem
- **4. File System**
  - 4.1 Design directory structure
  - 4.2 Implement file creation, reading, writing, deletion
- **5. Bonus Features (Optional)**
  - 5.1 Visualization of scheduler queues
  - 5.2 Multi-core CPU simulation

## Timeline
| Milestone                     | Planned Date |
|-------------------------------|--------------|
| Process Management Complete   | 2025-05-10   |
| Memory Management Complete    | 2025-05-20   |
| Concurrency Complete          | 2025-05-30   |
| File System Complete          | 2025-06-05   |
| Bonus Features (if any)       | 2025-06-10   |
| Final Report and Presentation | 2025-06-15   |

## Task Assignments
| Task                     | Assignee       |
|--------------------------|----------------|
| PCB Design               | Member 1       |
| Round Robin Scheduler    | Member 2       |
| Page Tables              | Member 3       |
| Thread API               | Member 4       |
| File System Design       | Member 5       |

## Resources
- Programming Language: Python
- Tools: GitHub, Visual Studio Code, Python 3.9+
- Team: 5 members, each contributing 10-15 hours/week

## Risks
| Risk                              | Mitigation                     |
|-----------------------------------|--------------------------------|
| Scheduler performance issues      | Add priority queue (#5)        |
| Limited team availability         | Adjust timeline if needed      |
| Complexity in concurrency         | Early testing and debugging    |