import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("C:\\Users\\bhashitha\\OneDrive\\Documents\\4th-yr-1st-sem\\research\\tourism research\\results\\response_time_results.json")

sns.histplot(data=df, x="total_response_time_ms", kde=True)
plt.title("Distribution of End-to-End Response Time")
plt.xlabel("Response Time (ms)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("endtoend_response_time_distribution.png")