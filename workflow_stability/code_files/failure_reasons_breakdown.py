import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("C:\\Users\\bhashitha\\OneDrive\\Documents\\4th-yr-1st-sem\\research\\tourism research\\results\\workflow_stability_results.json")
# Filter out rows where workflow failed due to "no reason" or "coordinator crash"
df = df[~df["workflow_failure_reason"].isin(["", "coordinator_crash"])]


sns.countplot(y="workflow_failure_reason", data=df)
plt.title("Types of Workflow Failures")
plt.xlabel("Count")
plt.ylabel("Failure Reason")
plt.tight_layout()
plt.savefig("types_of_workflow_failures.png")