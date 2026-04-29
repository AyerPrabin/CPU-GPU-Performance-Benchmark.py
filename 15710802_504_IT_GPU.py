import numpy as np
import time
from multiprocessing import Pool, cpu_count
def calculate_brightness(img_array):
    """
    Optimized Core: Processes millions of points via vectorization.
    This replaces slow nested loops for high performance.
    """
    return np.mean(img_array)

def run_performance_test():
    print(f"{'=' * 65}\n🚀 HARDWARE STRESS TEST: HIGH WORKLOAD BATCH\n{'=' * 65}")

    # CONFIGURATION: We use 100 images to overcome 'Pool' setup overhead [cite: 23, 26]
    n_img = 100
    res = 1000  # 4K resolution (16 million points per image) [cite: 10]
    size = (res, res)
    cores = cpu_count()

    print(f"💻 SYSTEM CORES   : {cores} CORES DETECTED")
    print(f"📊 TOTAL WORKLOAD : {n_img * res * res:,} DATA POINTS")
    print(f"{'=' * 65}")

    # Faster pre-allocation in RAM [cite: 37]
    print("Generating image batch...")
    images = [np.random.randint(0, 256, size, dtype=np.uint8) for _ in range(n_img)]

    # --- METHOD 1: SEQUENTIAL ---
    # CPU executes instructions one after another [cite: 20]
    print(f"\n🐢 METHOD 1: SEQUENTIAL PROCESSING")
    t0 = time.time()
    for i, img in enumerate(images):
        _ = calculate_brightness(img)
        if (i + 1) % 20 == 0:
            print(f"  ✅ [{i + 1}/{n_img}] Images Processed")
    t_seq = time.time() - t0

    # --- METHOD 2: PARALLEL ---
    # Bypasses the sequential bottleneck using multiple cores [cite: 26, 28]
    print(f"\n⚡ METHOD 2: PARALLEL PROCESSING")
    t1 = time.time()
    with Pool(processes=cores) as pool:
        # map handles the 100 tasks in parallel across the hierarchy [cite: 40]
        results = pool.map(calculate_brightness, images)
        print(f"  🚀 All {n_img} Images Processed via {cores} Cores")
    t_par = time.time() - t1

    # --- PERFORMANCE ANALYSIS ---
    speedup = t_seq / t_par
    p_efficiency = (speedup / cores) * 100 # Tutor's Efficiency Formula

    # Dynamic UI logic
    winner = "Parallel ⚡" if t_par < t_seq else "Sequential 🐢"

    print(f"\n{'=' * 65}\n🏆 FINAL PERFORMANCE REPORT\n{'=' * 65}")
    print(f"Sequential Duration   : {t_seq:.4f}s")
    print(f"Parallel Duration     : {t_par:.4f}s")
    print(f"Winner                : {winner} is faster! 🏁")
    print(f"Speedup Factor        : {speedup:.2f}x Faster 🚀")
    print(f"Parallel Efficiency   : {p_efficiency:.1f}% ✅")
    print(f"{'=' * 65}")

    # Hardware Justification for Part B Report [cite: 161]
    if t_par < t_seq:
        print("💡 Hardware Insight: Parallelism won because the workload was heavy.")
        print("   The system utilized core-level concurrency and L3 cache[cite: 19, 22].")
    else:
        print("💡 Hardware Insight: Sequential won due to Bus Latency[cite: 57].")
        print("   Data transfer time exceeded the calculation time[cite: 56].")
    print(f"{'=' * 65}")

if __name__ == "__main__":
    run_performance_test()