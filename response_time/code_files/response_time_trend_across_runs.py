import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("C:\\Users\\bhashitha\\OneDrive\\Documents\\4th-yr-1st-sem\\research\\tourism research\\results\\response_time_results.json")

sns.lineplot(x="run_id", y="total_response_time_ms", data=df)
plt.title("Response Time Across Simulation Runs")
plt.xlabel("Run ID")
plt.ylabel("Response Time (ms)")
plt.tight_layout()
plt.savefig("response_time_across_runs.png")