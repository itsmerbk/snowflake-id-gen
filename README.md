# 64-Bit Distributed Snowflake ID Generator

- **Track:** Distributed Systems
- **Complexity:** O(1) lock-free gen

## Overview
Time-ordered 64-bit unique ID generator packing timestamp, worker ID, and sequence.

## Run & Verify
```bash
python3 main.py
```
