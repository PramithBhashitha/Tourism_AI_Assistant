import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_json("user_satisfaction_results.json")

cols = [
    "relevance",
    "budget_fairness",
    "schedule_feasibility",
    "activity_suitability",
    "overall_satisfaction",
    "trust",
    "willingness_to_use"
]

# Sorting the averages in descending order for a cleaner visual ranking
df[cols].mean().sort_values(ascending=False).plot(kind="bar")

plt.title("Average User Satisfaction Scores")
plt.ylabel("Average Rating (1-5)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("average_user_satisfaction_scores.png")
