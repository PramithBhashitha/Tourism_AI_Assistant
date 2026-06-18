import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("negotiation_efficiency_results.json")

sns.boxplot(x="total_negotiation_time_ms", data=df)
plt.title("Total Negotiation Time (ms)")
plt.xlabel("Time (ms)")
plt.tight_layout()
plt.savefig("negotiation_time_boxplot.png")
