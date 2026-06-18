import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("response_time_results.json")

agent_cols = [
    "flight_agent_latency_ms",
    "resort_agent_latency_ms",
    "activities_agent_latency_ms",
    "judge_latency_ms"
]
df[agent_cols].mean().plot(kind="bar")

plt.title("Average Latency per Agent")
plt.ylabel("Latency (ms)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("average_agent_latency.png")