import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("decision_quality_results.json")


sns.histplot(data=df, x="remaining_budget", kde=True)
plt.title("Distribution of Remaining Budget")
plt.xlabel("Remaining Budget")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("remaining_budget_distribution.png")