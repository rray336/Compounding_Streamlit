# streamlit_app.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

# ---- Functions ----
def random_choice(choices):
    return random.choice(choices)

def geometric_mean(iterable):
    return np.prod(iterable) ** (1 / len(iterable))

def wealth_creation(return_dist, N):
    wealth = 100
    wealth_series = [wealth]
    for _ in range(N):
        r = random_choice(return_dist)
        wealth *= r
        wealth = min(wealth, 1e9)
        wealth = max(wealth, 0)
        wealth_series.append(wealth)
    return wealth_series

# ---- Streamlit UI ----
st.title("Kelly Criterion vs Mean-Variance Investing")

N = st.slider("Number of periods (N)", min_value=10, max_value=200, value=50)

strategies = {
    "Strategy 1": np.array([1, 1.2, 1.2, 1, 1.2, 1]),
    "Strategy 2": np.array([0, 1.2, 1.2, 1, 1.2, 2.2]),
    "Strategy 3": np.array([0.4, 2.2, 2.2, 0.4, 2.2, 0.4])
}

selected = st.multiselect("Select strategies to compare", list(strategies.keys()), default=list(strategies.keys()))

# ---- Plotting ----
fig, ax = plt.subplots()
colors = {"Strategy 1": None, "Strategy 2": None, "Strategy 3": "darkred"}
for name in selected:
    ret = strategies[name]
    wealth = wealth_creation(ret, N)
    ax.plot(range(N+1), wealth, label=name, color=colors.get(name))
    st.write(f"**{name} Stats** — Arith Mean: {ret.mean():.3f}, Geom Mean: {geometric_mean(ret):.3f}, Std: {ret.std():.3f}")

ax.set_title("Wealth Growth Simulation")
ax.set_xlabel("Periods")
ax.set_ylabel("Wealth")
ax.legend()
st.pyplot(fig)
