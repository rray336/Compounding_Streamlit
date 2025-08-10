# Compounding Streamlit App

This project is an interactive Streamlit web application that simulates and visualizes wealth growth under different investment strategies. It compares the Kelly Criterion and Mean-Variance investing approaches by running Monte Carlo simulations of compounding returns over multiple periods.

## Features

- Choose from three predefined investment strategies.
- Simulate wealth growth over a user-defined number of periods.
- View arithmetic mean, geometric mean, and standard deviation for each strategy.
- Visualize the compounding effect and compare strategies on a dynamic plot.

## Requirements

Install the following Python packages:

- `streamlit`
- `numpy`
- `matplotlib`

You can install them with:

```sh
pip install streamlit numpy matplotlib
```

## How to Run

Run the app using the following command:

```sh
python -m streamlit run Compounding_streamlit.py
```

## Inputs

- **Number of periods (N):** Selectable via a slider (10 to 200).
- **Strategies:** Select one or more strategies to compare using the multiselect widget.

## Output

- **Statistics:** For each selected strategy, the app displays the arithmetic mean, geometric mean, and standard deviation of the return distribution.
- **Plot:** A matplotlib chart showing simulated wealth growth over the selected number of periods for each strategy.

---

See [Compounding_streamlit.py](Compounding_streamlit.py) for the implementation.
