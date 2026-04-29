import time
from multiprocessing import Pool, cpu_count

# =========================================================================
# 🧩 THE CORE FUNCTION (Assessment Requirement)
# =========================================================================
def calculate_heavy_logic(task_id):
    """
    Simulates a heavy CPU-bound task like 3D physics or encryption.
    This demonstrates instruction-level parallelism and core usage.
    """
    # A heavy loop forces the CPU to work without needing massive RAM [cite: 135]
    count = 0
    for i in range(5_000_000):
        count += (i * i)
    return count

def run_performance_test():
    print(f"{'=' * 65}\n🚀 COVENTRY UNIVERSITY: HARDWARE PERFORMANCE TEST (PART B)\n{'=' * 65}")

    # Set 100 tasks to ensure all cores are fully utilized [cite: 124, 150]
    n_tasks = 100
    cores = cpu_count() # Identifies core count for parallel architecture [cite: 16]

    print(f"💻 SYSTEM CORES   : {cores} CORES DETECTED")
    print(f"📊 TOTAL WORKLOAD : {n_tasks} COMPLEX CPU TASKS")
    print(f"{'=' * 65}")

    # --- METHOD 1: SEQUENTIAL ---
    # Mimics executing instructions one after another, creating a bottleneck[cite: 20, 193].
    print(f"\n🐢 METHOD 1: SEQUENTIAL PROCESSING (1 Core)")
    t0 = time.time()
    for i in range(n_tasks):
        _ = calculate_heavy_logic(i)
        if (i + 1) % 20 == 0:
            print(f"  ✅ [Progress: {i + 1}/{n_tasks}] Completed")
    t_seq = time.time() - t0

    # --- METHOD 2: PARALLEL ---
    # Utilizes parallel processing to maximize proposed hardware[cite: 150, 152].
    print(f"\n⚡ METHOD 2: PARALLEL PROCESSING ({cores} Cores)")
    t1 = time.time()
    with Pool(processes=cores) as pool:
        # map handles the 100 tasks across the core hierarchy
        results = pool.map(calculate_heavy_logic, range(n_tasks))
        print(f"  🚀 All {n_tasks} Tasks Distributed via Multiprocessing")
    t_par = time.time() - t1

    # --- PERFORMANCE ANALYSIS ---
    speedup = t_seq / t_par
    # Tutor's Formula: (Speedup / Cores) * 100 [cite: 158]
    p_efficiency = (speedup / cores) * 100

    # Emojis based on which hardware configuration won
    seq_emoji = "🐢" if t_seq > t_par else "🏁"
    par_emoji = "⚡" if t_par < t_seq else "🐢"
    winner = "Parallel Architecture" if t_par < t_seq else "Sequential Logic"

    print(f"\n{'=' * 65}\n🏆 FINAL PERFORMANCE REPORT\n{'=' * 65}")
    print(f"Sequential Duration   : {t_seq:.4f}s {seq_emoji}")
    print(f"Parallel Duration     : {t_par:.4f}s {par_emoji}")
    print(f"Winner                : {winner} is faster! 🎯")
    print(f"Speedup Factor        : {speedup:.2f}x Faster 🚀")
    print(f"Parallel Efficiency   : {p_efficiency:.1f}% ✅")
    print(f"{'=' * 65}")

    # Linking program behavior to hardware features for Part B report [cite: 161]
    if t_par < t_seq:
        print("💡 Hardware Insight: Multi-core parallelism bypassed the bottleneck.")
        print("   This confirms your specification's choice of high core counts[cite: 16, 135].")
    else:
        print("💡 Hardware Insight: Low efficiency suggests thermal throttling[cite: 65].")
    print(f"{'=' * 65}")

if __name__ == "__main__":
    run_performance_test()