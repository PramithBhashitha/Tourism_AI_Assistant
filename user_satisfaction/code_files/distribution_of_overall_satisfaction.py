import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("user_satisfaction_results.json")

sns.histplot(data=df, x="overall_satisfaction", kde=True, discrete=True)
plt.title("Distribution of Overall Satisfaction")
plt.xlabel("Rating (1-5)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("overall_satisfaction_distribution.png")