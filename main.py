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
    st.image("Data files/Uber-logo.png", width=120)   # UPDATED LOGO PATH

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
    st.image("Data files/rice-logo.jpg", width=120)   # UPDATED LOGO PATH

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
    st.write("Below are basic example visualizations using Streamlit components.")

    # Placeholder demo data
    sample_data = pd.DataFrame({
        "distance": [1, 2, 3, 4, 5],
        "fare": [5, 7, 9, 13, 17]
    })

    st.subheader("Line Chart: Distance vs Fare")
    st.line_chart(sample_data.set_index("distance"))

    st.subheader("Bar Chart: Distance vs Fare")
    st.bar_chart(sample_data.set_index("distance"))
