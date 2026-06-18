import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("C:\\Users\\bhashitha\\OneDrive\\Documents\\4th-yr-1st-sem\\research\\tourism research\\results\\negotiation_efficiency_results.json")




agent_cols = ["flight_agent_messages", "resort_agent_messages", "activities_agent_messages", "judge_messages"]
df[agent_cols].sum().plot(kind="bar")

plt.title("Total Messages Exchanged per Agent")
plt.ylabel("Message Count")

# Rotate the x-axis agent labels so they don't overlap and are easy to read
plt.xticks(rotation=45, ha='right')

# Adjust layout to make sure rotated labels aren't cut off at the bottom
plt.tight_layout()

# 4. Save the figure to a file
plt.savefig("total_agent_messages.png")