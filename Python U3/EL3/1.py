import numpy as np
import pandas as pd

# ---------- SIMULATION ----------

np.random.seed(1)

# 48 hours, 1-second sampling

idx = pd.date_range("2025-01-01", periods=48*60*60, freq="1S")
df = pd.DataFrame(index=idx)
df["flow_lpm"] = 0.0

def inject_burst(start, duration, flow):
    df.loc[start:start+pd.Timedelta(seconds=duration), "flow_lpm"] = flow

# Usage bursts
for _ in range(20):  # taps
    inject_burst(np.random.choice(idx[:-300]), np.random.randint(30,120), np.random.uniform(4,6))

for _ in range(6):   # showers
    inject_burst(np.random.choice(idx[:-1200]), np.random.randint(600,900), np.random.uniform(8,12))

for _ in range(3):   # washing machine
    inject_burst(np.random.choice(idx[:-3600]), np.random.randint(1800,2400), np.random.uniform(12,15))

# Slow leak for 6 hours
leak_start = idx[20000]
leak_end = leak_start + pd.Timedelta(hours=6)
df.loc[leak_start:leak_end, "flow_lpm"] += 0.4

# Sensor noise
noise = np.random.normal(0, 0.15, len(df))
df.loc[df.flow_lpm > 0, "flow_lpm"] += noise[df.flow_lpm > 0]
df.flow_lpm = df.flow_lpm.clip(lower=0)

# ---------- PANDAS TASKS ----------
# Event segmentation
TH = 0.3
df["active"] = df.flow_lpm > TH
df["event_id"] = (df.active != df.active.shift()).cumsum()

# Hourly water usage
df["liters"] = df.flow_lpm / 60
hourly_usage = df.resample("1H")["liters"].sum()

# Leak detection
leaks = []
for _, g in df.groupby("event_id"):
    if len(g) > 6*3600 and 0.2 < g.flow_lpm.mean() < 1:
        leaks.append([g.index[0], g.index[-1], g.flow_lpm.mean()])

leak_df = pd.DataFrame(leaks, columns=["Start","End","Avg Flow (LPM)"])

# Usage classification
usage = []
for _, g in df.groupby("event_id"):
    if g.flow_lpm.mean() > TH:
        f = g.flow_lpm.mean()
        u = "Tap" if f < 6 else "Shower" if f < 10 else "Washing Machine"
        usage.append([g.index[0], len(g), f, u])

usage_df = pd.DataFrame(usage, columns=["Start","Duration(sec)","Avg Flow","Type"])

# Leakage impact report
leak_loss = df.loc[leak_start:leak_end, "liters"].sum()

leak_report = {
    "Leak Duration (hrs)": 6,
    "Water Lost (liters)": round(leak_loss,2),
    "Estimated Monthly Loss (liters)": round(leak_loss*5,2)
}

print("\nHourly Usage (sample):")
print(hourly_usage.head())

print("\nLeak Detected:")
print(leak_df)

print("\nLeak Impact Report:")
print(pd.Series(leak_report))
