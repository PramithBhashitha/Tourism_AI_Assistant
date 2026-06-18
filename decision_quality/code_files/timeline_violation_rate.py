import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("decision_quality_results.json")


sns.countplot(x="timeline_conflict", data=df)
plt.title("Timeline Conflict Frequency")
plt.xlabel("Timeline Conflict")
plt.ylabel("Count")
plt.savefig("timeline_conflict_frequency.png")