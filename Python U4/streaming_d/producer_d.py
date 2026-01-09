import json, random, time
from datetime import datetime, timezone

SENSORS=['S01','S02','S03','S04']
OUT_FILE='events.json1'

def iso_utc_now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds').replace("+00.00","Z")

def make_event(sensor_id,seq):
    t_c=round(random.uniform(22.0, 36.0), 2)
    h=round(random.uniform(35.0,80.0),2)
    return{'Sensor_Id':sensor_id,'Timestamp':iso_utc_now(),'Temperature':t_c,'Humidity':h,'Sequence':seq}
tot_events=1000
delay=0.1
seq=1

with open(OUT_FILE,'a', encoding='utf-8')as f:
    for _ in range(tot_events):
        sensor_id=random.choice(SENSORS)   
        event=make_event(sensor_id,seq)
        f.write(json.dumps(event)+'\n')
        f.flush()
        seq+=1
        time.sleep(delay)
print(f'{tot_events} writte to {OUT_FILE}')