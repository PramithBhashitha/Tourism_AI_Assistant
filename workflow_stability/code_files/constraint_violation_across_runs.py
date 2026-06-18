import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("C:\\Users\\bhashitha\\OneDrive\\Documents\\4th-yr-1st-sem\\research\\tourism research\\results\\workflow_stability_results.json")

sns.lineplot(x="run_id", y="budget_constraint_violations", data=df, label="Budget")
sns.lineplot(x="run_id", y="timeline_constraint_violations", data=df, label="Timeline")

plt.title("Constraint Violations Across Runs")
plt.xlabel("Run ID")
plt.ylabel("Violations")
plt.legend()

# Adjust layout to prevent any edge or legend clipping
plt.tight_layout()

# 4. Save the figure to a file
plt.savefig("constraint_violations_across_runs.png")