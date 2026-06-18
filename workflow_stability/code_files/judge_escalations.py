import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("workflow_stability_results.json")

sns.histplot(data=df, x="judge_escalations", kde=True, discrete=True)
plt.title("Distribution of Judge Escalations")
plt.xlabel("Escalations")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("judge_escalations_distribution.png")