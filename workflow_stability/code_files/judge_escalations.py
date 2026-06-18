import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("C:\\Users\\bhashitha\\OneDrive\\Documents\\4th-yr-1st-sem\\research\\tourism research\\results\\workflow_stability_results.json")

sns.histplot(data=df, x="judge_escalations", kde=True, discrete=True)
plt.title("Distribution of Judge Escalations")
plt.xlabel("Escalations")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("judge_escalations_distribution.png")