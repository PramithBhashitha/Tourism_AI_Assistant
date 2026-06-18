import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("user_satisfaction_results.json")

sns.scatterplot(x="time_spent_reviewing_ms", y="overall_satisfaction", data=df)
plt.title("Review Time vs Satisfaction")
plt.xlabel("Review Time (ms)")
plt.ylabel("Satisfaction")
plt.tight_layout()
plt.savefig("review_time_vs_satisfaction.png")