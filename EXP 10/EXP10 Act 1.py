#Create a Streamlit grocery bill calculator.
"""
Created on Mon Apr 27 15:41:58 2026

@author: swapnil
"""

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Grocery Bill Calculator", page_icon="🛒")

st.title("🛒 Grocery Bill Calculator")
st.write("Add your items below to calculate the total cost.")

# Initialize a default dataframe in session state if it doesn't exist
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(
        [
            {"Item": "Milk", "Quantity": 1, "Price per Unit": 3.50},
            {"Item": "Bread", "Quantity": 2, "Price per Unit": 2.20},
        ]
    )

# The Data Editor: allows users to add/delete/edit rows
edited_df = st.data_editor(
    st.session_state.df,
    num_rows="dynamic",
    column_config={
        "Item": st.column_config.TextColumn("Item Name", help="What are you buying?", width="medium"),
        "Quantity": st.column_config.NumberColumn("Qty", min_value=1, step=1),
        "Price per Unit": st.column_config.NumberColumn("Price ()", min_value=0.0, format="%.2f"),
    },
    use_container_width=True,
    key="grocery_editor"
)

# Calculations
if not edited_df.empty:
    # Ensure numeric types for calculation
    qty = pd.to_numeric(edited_df["Quantity"], errors='coerce').fillna(0)
    price = pd.to_numeric(edited_df["Price per Unit"], errors='coerce').fillna(0)
    
    total_cost = (qty * price).sum()
    item_count = qty.sum()

    st.divider()

    # Display Results
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Items", int(item_count))
    with col2:
        st.metric("Total Cost", f"{total_cost:,.2f}")

    # Optional: Tax Calculation
    with st.expander("Add Tax/Discounts"):
        tax_rate = st.slider("Tax Rate (%)", 0, 15, 0)
        tax_amount = total_cost * (tax_rate / 100)
        final_total = total_cost + tax_amount
        st.write(f"**Tax Amount:** {tax_amount:.2f}")
        st.subheader(f"Grand Total: {final_total:.2f}")
else:
    st.info("Add an item to get started!")
