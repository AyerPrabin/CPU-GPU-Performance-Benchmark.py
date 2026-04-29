# CPU-GPU-Performance-Benchmark.py
Analyzes instruction-level parallelism by comparing sequential and parallel processing of CPU/GPU-bound tasks.
1. CPU-Performance-Benchmark.py

Purpose: Analyzes instruction-level parallelism by comparing sequential and parallel processing of CPU-bound tasks.

Logic: Executes 100 complex mathematical tasks involving 5,000,000 iterations each.

Hardware Impact: Demonstrates how a multi-core architecture bypasses sequential bottlenecks and calculates speedup factors and parallel efficiency.

2. Vector-Processing-Stress-Test.py

Purpose: Measures system throughput when handling high-volume data batches using vectorization.

Logic: Processes a batch of 100 4K-resolution images (16 million data points each) using NumPy and Python's Multiprocessing Pool.

Hardware Impact: Evaluates the balance between core-level concurrency and bus latency during massive data transfers.
