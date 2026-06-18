import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("user_satisfaction_results.json")

sns.countplot(x="final_acceptance", data=df)
plt.title("Final Acceptance Rate")
plt.xlabel("Accepted Final Plan")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("final_acceptance_rate.png")