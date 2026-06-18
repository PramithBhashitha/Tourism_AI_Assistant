import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("workflow_stability_results.json")

sns.countplot(x="final_plan_valid", data=df)
plt.title("Final Plan Validity Rate")
plt.xlabel("Valid Final Plan")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("final_plan_validity_rate.png")