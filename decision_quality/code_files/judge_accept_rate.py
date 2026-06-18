import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("decision_quality_results.json")

sns.countplot(x="judge_accept", data=df)
plt.title("Judge Accept vs Reject")
plt.xlabel("Accepted by Judge")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("judge_accept_frequency.png")