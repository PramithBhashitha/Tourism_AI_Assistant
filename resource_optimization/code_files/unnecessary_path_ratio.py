import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("resource_optimization_results.json")

sns.lineplot(x="run_id", y="unnecessary_path_ratio", data=df)
plt.title("Unnecessary Path Ratio Across Runs")
plt.xlabel("Run ID")
plt.ylabel("UPR")
plt.tight_layout()
plt.savefig("unnecessary_path_ratio_across_runs.png")