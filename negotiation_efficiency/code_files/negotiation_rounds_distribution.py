import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("C:\\Users\\bhashitha\\OneDrive\\Documents\\4th-yr-1st-sem\\research\\tourism research\\results\\negotiation_efficiency_results.json")




sns.histplot(data=df, x="negotiation_rounds", kde=True)
plt.title("Distribution of Negotiation Rounds")
plt.xlabel("Rounds")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("negotiation_rounds_distribution.png")