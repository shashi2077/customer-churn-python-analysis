import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/customer_churn.csv")

# -----------------------------
# 1. Data quality checks
# -----------------------------
print("Shape:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# -----------------------------
# 2. Overall churn
# -----------------------------
overall_churn = df["Churned"].mean() * 100
print(f"\nOverall churn rate: {overall_churn:.2f}%")

# -----------------------------
# 3. Churn by contract type
# -----------------------------
contract_churn = (
    df.groupby("ContractType")["Churned"]
      .mean()
      .mul(100)
      .sort_values(ascending=False)
)
print("\nChurn by contract type:\n", contract_churn)

# -----------------------------
# 4. Churn by AutoPay
# -----------------------------
autopay_churn = (
    df.groupby("AutoPay")["Churned"]
      .mean()
      .mul(100)
      .sort_values(ascending=False)
)
print("\nChurn by AutoPay:\n", autopay_churn)

# -----------------------------
# 5. Tenure segmentation
# -----------------------------
df["TenureBand"] = pd.cut(
    df["TenureMonths"],
    bins=[0, 6, 12, 24, 48, 72],
    labels=["0-6", "7-12", "13-24", "25-48", "49-72"]
)

tenure_churn = (
    df.groupby("TenureBand", observed=False)["Churned"]
      .mean()
      .mul(100)
)
print("\nChurn by tenure band:\n", tenure_churn)

# -----------------------------
# 6. Support ticket segmentation
# -----------------------------
df["TicketBand"] = pd.cut(
    df["SupportTickets"],
    bins=[-1, 0, 2, 4, 100],
    labels=["0", "1-2", "3-4", "5+"]
)

ticket_churn = (
    df.groupby("TicketBand", observed=False)["Churned"]
      .mean()
      .mul(100)
)
print("\nChurn by support tickets:\n", ticket_churn)

# -----------------------------
# 7. Satisfaction analysis
# -----------------------------
satisfaction_churn = (
    df.groupby("SatisfactionScore")["Churned"]
      .mean()
      .mul(100)
)
print("\nChurn by satisfaction score:\n", satisfaction_churn)

# -----------------------------
# 8. Charts
# -----------------------------
contract_churn.plot(kind="bar", title="Churn Rate by Contract Type")
plt.ylabel("Churn Rate (%)")
plt.tight_layout()
plt.savefig("churn_by_contract.png", dpi=150)
plt.close()

tenure_churn.plot(kind="bar", title="Churn Rate by Tenure Band")
plt.ylabel("Churn Rate (%)")
plt.tight_layout()
plt.savefig("churn_by_tenure.png", dpi=150)
plt.close()

ticket_churn.plot(kind="bar", title="Churn Rate by Support Ticket Band")
plt.ylabel("Churn Rate (%)")
plt.tight_layout()
plt.savefig("churn_by_support_tickets.png", dpi=150)
plt.close()

satisfaction_churn.plot(kind="bar", title="Churn Rate by Satisfaction Score")
plt.ylabel("Churn Rate (%)")
plt.tight_layout()
plt.savefig("churn_by_satisfaction.png", dpi=150)
plt.close()
