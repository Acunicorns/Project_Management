# Process Control Block (PCB) Design

## Overview
The PCB is designed for the game console OS to manage game processes (e.g., rendering, input handling) with low latency. It stores critical process information for efficient context switching.

## PCB Structure
| Field           | Description                              |
|-----------------|------------------------------------------|
| Process ID      | Unique identifier for the process        |
| State           | Running, Waiting, Terminated             |
| Priority        | Priority level (1-5, 1 highest)          |
| Registers       | CPU register states (simulated)          |
| Program Counter | Current instruction pointer              |

## Theme Connection
The PCB prioritizes high-priority game tasks (e.g., rendering) to ensure smooth gameplay. The lightweight structure supports fast context switching.

**Related Issue**: #1