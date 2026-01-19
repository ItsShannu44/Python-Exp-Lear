from multiprocessing import Process
import os

LOG_FILE = r"D:\Github\Python Exp Lear\Python U4\Forking\access.log"
NUM_PROCS = 3
LEVELS = ['INFO', 'WARNING', 'ERROR']


def split_lines(lines, k):
    size = (len(lines) + k - 1) // k
    return [lines[i*size:(i+1)*size] for i in range(k)]


def worker(chunk, out_file):
    counts = {level: 0 for level in LEVELS}

    for line in chunk:
        parts = line.strip().split()
        if not parts:
            continue
        level = parts[0]
        if level in counts:
            counts[level] += 1

    with open(out_file, 'w') as f:
        for l in LEVELS:
            f.write(f"{l}: {counts[l]}\n")


if __name__ == '__main__':
    with open(LOG_FILE, 'r') as f:
        lines = f.readlines()

    chunks = split_lines(lines, NUM_PROCS)

    processes = []
    temp_files = []

    for i, c in enumerate(chunks):
        out_file = f"part_{i}.txt"
        temp_files.append(out_file)
        p = Process(target=worker, args=(c, out_file))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    final_counts = {level: 0 for level in LEVELS}

    for tf in temp_files:
        with open(tf, 'r') as f:
            for line in f:
                level, val = line.strip().split(':')
                final_counts[level] += int(val)
        os.remove(tf)

    print("Merged Files Count:", final_counts)
