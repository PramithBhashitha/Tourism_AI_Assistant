import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("C:\\Users\\bhashitha\\OneDrive\\Documents\\4th-yr-1st-sem\\research\\tourism research\\results\\resource_optimization_results.json")

sns.histplot(data=df, x="tokens_total", kde=True)
plt.title("Distribution of Total Token Usage")
plt.xlabel("Tokens")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("total_token_usage_distribution.png")