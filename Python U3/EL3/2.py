import numpy as np
import pandas as pd

# ---------- SIMULATION ----------
np.random.seed(2)

# 24 hours, 5-second sampling
idx = pd.date_range("2025-01-01", periods=24*60*12, freq="5S")
df = pd.DataFrame(index=idx)
df["heart_rate"] = 70

# Sleep & active baseline
df.loc["2025-01-01 00:00":"2025-01-01 06:00", "heart_rate"] = 55
df.loc["2025-01-01 22:00":"2025-01-01 23:59", "heart_rate"] = 60

# Exercise sessions
sessions = [("07:00","07:30"), ("18:00","18:45")]

for s, e in sessions:
    start = pd.Timestamp(f"2025-01-01 {s}")
    end = pd.Timestamp(f"2025-01-01 {e}")

    df.loc[start:end, "heart_rate"] = np.linspace(
        100, 150, len(df.loc[start:end])
    )

    recovery_end = end + pd.Timedelta(minutes=15)
    df.loc[end:recovery_end, "heart_rate"] = np.linspace(
        150, 75, len(df.loc[end:recovery_end])
    )


# Motion noise
df["heart_rate"] += np.random.normal(0, 3, len(df))

# ---------- PANDAS TASKS ----------
# Sleep & active inference
df["state"] = np.where(df.heart_rate < 60, "Sleep", "Active")

# Exercise detection
df["exercise"] = df.heart_rate > 120

# Recovery time calculation
recoveries = []
for t in df[df.exercise].index:
    post = df.loc[t:t+pd.Timedelta(minutes=20)]
    if (post.heart_rate < 80).any():
        recoveries.append((t, (post.heart_rate < 80).idxmax()))

recovery_df = pd.DataFrame(recoveries, columns=["Exercise End","Recovered At"])

# Abnormal HR detection
df["abnormal"] = (df.heart_rate > 170) | (df.heart_rate < 40)

# Daily fitness summary
summary = {
    "Average HR": round(df.heart_rate.mean(),1),
    "Max HR": int(df.heart_rate.max()),
    "Exercise Sessions": len(sessions),
    "Abnormal Events": int(df.abnormal.sum()),
    "Sleep Hours": round((df.state=="Sleep").sum()*5/3600,2)
}

print("\nRecovery Times:")
print(recovery_df.head())

print("\nDaily Fitness Summary:")
print(pd.Series(summary))
