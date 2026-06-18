import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("resource_optimization_results.json")

api_cols = ["flight_api_calls", "resort_api_calls", "activities_api_calls"]
df[api_cols].mean().plot(kind="bar")

plt.title("Average API Calls per Agent")
plt.ylabel("API Calls")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("average_api_calls_per_agent.png")