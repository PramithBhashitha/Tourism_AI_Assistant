import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("response_time_results.json")

api_cols = [
    "flight_api_latency_ms",
    "resort_api_latency_ms",
    "activities_api_latency_ms"
]
df[api_cols].mean().plot(kind="bar")

plt.title("Average API Latency")
plt.ylabel("Latency (ms)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("average_api_latency.png")