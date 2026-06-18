import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("workflow_stability_results.json")

sns.countplot(x="workflow_success", data=df)
plt.title("Workflow Success vs Failure")
plt.xlabel("Success")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("workflow_success_vs_failure.png")