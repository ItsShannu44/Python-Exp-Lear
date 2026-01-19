from multiprocessing import Process
import os

LOG_FILE='access.log'
NUM_PROCS=3
LEVELS=['INFO','WARNING','ERROR']

def split_lines(lines, k):
    size=(len(lines)+k-1)//k
    return [lines[i*size(i+1)*size]for i in range(k)]

def worker(chunk, OUT_FILE):
    counts={level:0 for level in LEVELS}
    for line in chunk:
        parts=line.strip().split()
        if not parts:
            continue
        level_1=parts[0]
        if level_1 in counts:
            counts[level_1]+=1
    with open(OUT_FILE,'w') as f:
        for l in LEVELS:
            f.write(f'{l}: {counts[1]}\n')

if __name__=='__main__':
    with open(LOG_FILE,'r') as f:
        lines=f.readlines()
    chunks=split_lines(lines, NUM_PROCS)
    process=[]
    temp_file=[]
    for i, c in enumerate(chunks):
        OUT_FILE=f'part_(i)/txt'
        temp_file.append(OUT_FILE)
        p=Process(target=worker, args=(chunks, OUT_FILE))
        p.start()
        process.append(p)
    for p in process:
        p.join()
    final_counts={level:0 for level in LEVELS}
    for tf in temp_file:
        with open(tf,'r')as f:
            for line in f:
                l,val=line.strip().split()
                final_counts[1]+=int(val)
        os.remove(tf)
    print(f'Merged Files Count: {final_counts}')