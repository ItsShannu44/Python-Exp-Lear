import json, time
from collections import defaultdict

IN_FILE='events.json1'

def follow(file_obj):
    #generator Fun
    # it has yield instead of return
    file_obj.seek(0,2)
    while True:
        line=file_obj.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line
counts=defaultdict(int)
total=0
bad_json=0
MAX_EVENTS=100

with open(IN_FILE,'r',encoding='utf-8')as f:
    for line in follow(f):
        line=line.strip()
        if not line:
            continue
        try:
            event=json.loads(line)
        except json.JSONDecoderError:
            bad_json+=1
            continue
        sensor_id=event.get("Sensor_Id","UNKNOWN")
        counts[sensor_id]+=1
        total+=1

        if total%20==0:
            print(f'Total: {total}, Bad JSON data {bad_json}, Counts:{dict(counts)}')
            if total>=MAX_EVENTS:
                print('Limit Reached, Stopping Consumer')
                break