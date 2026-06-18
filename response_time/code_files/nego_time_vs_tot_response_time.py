import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("C:\\Users\\bhashitha\\OneDrive\\Documents\\4th-yr-1st-sem\\research\\tourism research\\results\\response_time_results.json")

sns.scatterplot(x="total_negotiation_time_ms", y="total_response_time_ms", data=df)
plt.title("Negotiation Time vs Total Response Time")
plt.xlabel("Negotiation Time (ms)")
plt.ylabel("Total Response Time (ms)")
plt.tight_layout()
plt.savefig("negotiation_vs_response_time.png")