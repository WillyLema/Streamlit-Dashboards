# ---------------------------------------------------------
# Tab 3 — Visualizations
# ---------------------------------------------------------
with tab3:
    st.header("Visualizations")

    # -------------------------
    # Load your data (example)
    # Replace this with your real Uber DF
    # -------------------------
    data = pd.DataFrame({
        "Switchbacks": range(1, 51),       # Example column
        "distance": [1, 2, 3, 4, 5] * 10,
        "fare": [5, 7, 9, 13, 17] * 10
    })

    # Function you provided
    def load_data(df):
        display(df['Switchbacks'])

    # -------------------------
    # Create 3 columns
    # -------------------------
    left_col, mid_col, right_col = st.columns([3, 3, 3])

    # -------------------------
    # LEFT COLUMN — Table + Slider Filter
    # -------------------------
    with left_col:
        st.subheader("Data Table (Filtered)")

        # Slider to choose row range
        min_row, max_row = st.slider(
            "Select row range:",
            min_value=0,
            max_value=len(data) - 1,
            value=(0, 10),   # default range
            step=1
        )

        # Filter dataframe
        filtered_df = data.iloc[min_row:max_row + 1]

        # Display using your function
        load_data(filtered_df)

        # Also render table for Streamlit clarity
        st.dataframe(filtered_df, use_container_width=True)

    # -------------------------
    # MIDDLE COLUMN — Line Chart
    # -------------------------
    with mid_col:
        st.subheader("Line Chart")
        st.line_chart(filtered_df[['distance', 'fare']])

    # -------------------------
    # RIGHT COLUMN — Bar Chart
    # -------------------------
    with right_col:
        st.subheader("Bar Chart")
        st.bar_chart(filtered_df[['distance', 'fare']])
