import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("C:\\Users\\bhashitha\\OneDrive\\Documents\\4th-yr-1st-sem\\research\\tourism research\\results\\resource_optimization_results.json")

sns.scatterplot(x="cpu_usage_percent", y="memory_usage_mb", data=df)
plt.title("CPU vs Memory Usage")
plt.xlabel("CPU Usage (%)")
plt.ylabel("Memory (MB)")
plt.tight_layout()
plt.savefig("cpu_vs_memory_usage.png")