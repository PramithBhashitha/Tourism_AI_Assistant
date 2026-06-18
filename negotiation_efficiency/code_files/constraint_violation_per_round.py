import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("C:\\Users\\bhashitha\\OneDrive\\Documents\\4th-yr-1st-sem\\research\\tourism research\\results\\negotiation_efficiency_results.json")

sns.lineplot(x="run_id", y="constraint_violations_per_round", data=df)
plt.title("Constraint Violations Across Runs")
plt.xlabel("Run ID")
plt.ylabel("Violations")
plt.tight_layout()
plt.savefig("constraint_violations_across_runs.png")