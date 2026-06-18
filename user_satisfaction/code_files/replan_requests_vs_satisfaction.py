import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("user_satisfaction_results.json")

sns.scatterplot(x="replan_requests", y="overall_satisfaction", data=df)
plt.title("Replan Requests vs Satisfaction")
plt.xlabel("Replan Requests")
plt.ylabel("Overall Satisfaction")
plt.tight_layout()
plt.savefig("replan_requests_vs_satisfaction.png")