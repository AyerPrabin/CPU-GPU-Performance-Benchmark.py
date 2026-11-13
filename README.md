# CPU Parallelism Benchmarks (Python)

Two small Python benchmarks that compare **sequential** and **parallel** processing on a multi-core CPU, and report the speedup and parallel efficiency. Written for a university computer architecture module (Coventry University), then cleaned up.

| Script | What it runs | What it shows |
|---|---|---|
| `cpu_benchmark.py` | 100 CPU-bound tasks, each a 5,000,000-step arithmetic loop | How a multiprocessing `Pool` spreads pure compute across cores, and how close it gets to an ideal speedup |
| `vector_benchmark.py` | 100 random 1000 x 1000 images, mean brightness with NumPy | When the work per task is small, the cost of moving data between processes can make the parallel version slower |

Both scripts print the core count, the time for each method, the speedup factor (sequential time / parallel time) and parallel efficiency ((speedup / cores) x 100).

## Run

```bash
pip install numpy
python cpu_benchmark.py
python vector_benchmark.py
```

Results depend on the machine: core count, clock speed, cache size and background load all change the numbers.

## What I learned

- Parallel processes only pay off when each task does enough work to cover the cost of starting workers and copying data to them.
- NumPy's vectorised operations are already fast on one core, so splitting them across processes can lose time to data transfer.
- Efficiency below 100% is normal: shared memory bandwidth, the OS scheduler and turbo-boost limits all reduce the gain from extra cores.

## Licence

MIT, see [LICENSE](./LICENSE).
