#Nemit jain 

import numpy as np
import pandas as pd
import streamlit as st

# Setup the app title
st.title("🎨 Simple Room Paint & Budget Planner")
st.write("Enter your room size below to find out how much paint you need!")

# --- STEP 1: GET ROOM SIZE FROM USER ---
st.header("1. Room Details")

# Simple number inputs for the room dimensions
length = st.number_input("Room Length (in feet)", min_value=1.0, value=12.0)
width = st.number_input("Room Width (in feet)", min_value=1.0, value=10.0)
height = st.number_input("Wall Height (in feet)", min_value=1.0, value=8.0)

# Ask for the number of doors and windows to subtract
doors = st.number_input("How many doors in the room?", min_value=0, value=1)
windows = st.number_input("How many windows in the room?", min_value=0, value=2)


# --- STEP 2: CALCULATE THE SQUARE FOOTAGE ---
# Total wall surface area before subtractions
gross_wall_area = 2 * (length + width) * height

# Subtract 21 sq ft per door and 15 sq ft per window
door_area = doors * 21.0
window_area = windows * 15.0
total_subtractions = door_area + window_area

# Calculate the final surface area to paint (ensuring it doesn't go below 0)
net_wall_area = np.maximum(0.0, gross_wall_area - total_subtractions)
ceiling_area = length * width

# Show the area totals on the screen
st.subheader("Total Area to Cover")
st.write(f" Walls to Paint: **{net_wall_area:.1f} sq ft**")
st.write(f" Ceiling to Paint: **{ceiling_area:.1f} sq ft**")


# --- STEP 3: CREATE THE MATERIAL TABLE ---
st.header("2. Materials & Cost Calculator")

# 10th-grade coverage standard variables
# 1 Gallon of Wall Paint covers 200 sq ft (2 coats)
# 1 Gallon of Ceiling Paint covers 350 sq ft
# 1 Gallon of Primer covers 300 sq ft
wall_paint_qty = np.ceil(net_wall_area / 200.0)
ceiling_paint_qty = np.ceil(ceiling_area / 350.0)
primer_qty = np.ceil(net_wall_area / 300.0)

# Set prices for each item
wall_paint_price = 45.0
ceiling_paint_price = 35.0
primer_price = 25.0

# Calculate total costs for each item
wall_paint_cost = wall_paint_qty * wall_paint_price
ceiling_paint_cost = ceiling_paint_qty * ceiling_paint_price
primer_cost = primer_qty * primer_price

# Organize the data into a simple Pandas Table (DataFrame)
data = {
    "Material": ["Wall Paint", "Ceiling Paint", "Primer"],
    "Quantity Needed": [wall_paint_qty, ceiling_paint_qty, primer_qty],
    "Unit": ["Gallon(s)", "Gallon(s)", "Gallon(s)"],
    "Price Per Gallon": [
        f"${wall_paint_price}",
        f"${ceiling_paint_price}",
        f"${primer_price}",
    ],
    "Total Cost": [
        f"${wall_paint_cost:.2f}",
        f"${ceiling_paint_cost:.2f}",
        f"${primer_cost:.2f}",
    ],
}

shopping_list_df = pd.DataFrame(data)

# Show the table in the app
st.dataframe(shopping_list_df, use_container_width=True)


# --- STEP 4: FINAL TOTAL BUDGET ---
# Sum up all the final costs
grand_total = wall_paint_cost + ceiling_paint_cost + primer_cost

st.success(f"### 💰 Estimated Total Project Budget: ${grand_total:.2f}")
