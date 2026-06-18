import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("C:\\Users\\bhashitha\\OneDrive\\Documents\\4th-yr-1st-sem\\research\\tourism research\\results\\resource_optimization_results.json")

sns.lineplot(x="run_id", y="total_api_calls", data=df)
plt.title("Total API Calls Across Runs")
plt.xlabel("Run ID")
plt.ylabel("API Calls")
plt.tight_layout()
plt.savefig("total_api_calls_across_runs.png")