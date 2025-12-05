import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="HBR - UBER Case Study Dashboard",
    layout="wide"
)

# ---------------------------------------------------------
# Header with two logos and centered title
# ---------------------------------------------------------
col1, col2, col3 = st.columns([1, 4, 1])

with col1:
    st.image("Data files/Uber-logo.png", width=120)

with col2:
    st.markdown(
        """
        <h1 style="text-align:center; margin-top:10px;">
            HBR - UBER Case Study Dashboard
        </h1>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.image("Data files/rice-logo.jpg", width=120)

st.write("---")

# ---------------------------------------------------------
# Tabs
# ---------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["📄 Metadata", "📚 Data Dictionary", "📊 Visualizations"])


# ---------------------------------------------------------
# Tab 1 — Metadata
# ---------------------------------------------------------
with tab1:
    st.header("Metadata")

    st.write(
        """
        This section provides the general metadata for the  
        **HBR – UBER Case Study Dataset**.
        """
    )

    metadata = {
        "Source": "HBR Case Study",
        "Date Retrieved": "2025-01-01",
        "Observations": 10_000,
        "Variables": 12,
        "Description": "Dataset describing Uber ride patterns, fares, and operational factors."
    }

    st.json(metadata)


# ---------------------------------------------------------
# Tab 2 — Data Dictionary
# ---------------------------------------------------------
with tab2:
    st.header("Data Dictionary")

    data_dict = pd.DataFrame({
        "Variable": ["trip_id", "driver_id", "timestamp", "distance", "fare"],
        "Type": ["string", "string", "datetime", "float", "float"],
        "Description": [
            "Unique identifier of the trip",
            "Unique identifier for the driver",
            "Timestamp marking the beginning of the trip",
            "Distance traveled (miles)",
            "Fare amount charged (USD)"
        ]
    })

    st.dataframe(data_dict, use_container_width=True)


# ---------------------------------------------------------
# Tab 3 — Visualizations
# ---------------------------------------------------------
with tab3:
    st.header("Visualizations")

    st.write(
        "Use the slider to filter the rows of the dataset. "
        "The left column shows the filtered data; the middle and right columns show simple charts."
    )

    # -------------------------------------------------
    # Load or create data
    # Replace this with your real Uber dataframe
    # -------------------------------------------------
    # Example structure; make sure your real data has a 'Switchbacks' column
    data = pd.DataFrame({
        "Switchbacks": range(1, 101),
        "distance": [1, 2, 3, 4, 5] * 20,
        "fare": [5, 7, 9, 13, 17] * 20
    })

    # Your function style adapted for Streamlit
    def load_data(df):
        # Show only the 'Switchbacks' column as a table
        st.dataframe(df[['Switchbacks']], use_container_width=True)

    # 3 columns layout
    left_col, mid_col, right_col = st.columns(3)

    # -------------------------
    # LEFT COLUMN — Table + Slider
    # -------------------------
    with left_col:
        st.subheader("Filtered Data Table")

        # Double int slider for row range
        max_index = len(data) - 1
        start_idx, end_idx = st.slider(
            "Select row range (by index):",
            min_value=0,
            max_value=max_index,
            value=(0, min(10, max_index)),
            step=1
        )

        # Filter dataframe
        filtered_df = data.iloc[start_idx:end_idx + 1]

        # Use your function to show the data
        load_data(filtered_df)

        # Optional: show full filtered df below
        st.caption("Full filtered rows:")
        st.dataframe(filtered_df, use_container_width=True)

    # -------------------------
    # MIDDLE COLUMN — Line Chart
    # -------------------------
    with mid_col:
        st.subheader("Line Chart (Distance vs Fare)")
        if not filtered_df.empty:
            st.line_chart(filtered_df.set_index("distance")[["fare"]])
        else:
            st.info("No data in the selected range.")

    # -------------------------
    # RIGHT COLUMN — Bar Chart
    # -------------------------
    with right_col:
        st.subheader("Bar Chart (Distance vs Fare)")
        if not filtered_df.empty:
            st.bar_chart(filtered_df.set_index("distance")[["fare"]])
        else:
            st.info("No data in the selected range.")
