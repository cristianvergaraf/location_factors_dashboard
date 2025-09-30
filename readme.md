Location Factors Dashboard
Relative importance of location factors in the Lingue basin in south central Chile.

🚀 Overview

This project provides an interactive visualization dashboard designed to visualize the results of the relative importance analysis of variables spatial variables for the expansion forest plantation in the Lingue basin of South-Central Chile. 

In spatial analysis, understanding which location factors significantly influence the spatial pattern of the expansion of forest plantation. This dashboard helps to undestand spatial validation of models used to predicted or understand spatial phenomenon. 

The core objective is to translate complex model output into an accessible, intuitive visual format.

✨ Features

The feat/dashboard-visualization branch currently focuses on establishing the core visual and interactive components:

    Interactive Variable Importance: Visualize a ranked list (e.g., using permutation importance or coefficients) of input variables with corresponding metrics (e.g., bar charts).

    Geographic Heatmaps/Choropleths: Display the spatial distribution of selected variable metrics or model residuals on an interactive map (e.g., utilizing Leaflet or Mapbox).

    Factor Sensitivity View: A dedicated view to explore how a change in a specific location factor impacts the model outcome across different geographic regions.

    Dynamic Data Filtering: Ability to filter data based on spatial aggregation levels (e.g., city, district, block) or statistical significance.

    Export Capabilities: Functionality to download the generated visualizations and data subsets for reports.

🛠️ Installation and Setup

Follow these steps to set up the project environment and run the dashboard locally.
Prerequisites

    Python (3.8+)

    Node.js (for frontend dependencies, if applicable)

    Git

Steps

    Clone the repository:

    git clone [https://github.com/cristianvergaraf/location_factors_dashboard.git](https://github.com/cristianvergaraf/location_factors_dashboard.git)
    cd location_factors_dashboard

    Switch to the development branch:

    git checkout feat/dashboard-visualization

    Set up the Python environment and install dependencies:
    (Assuming a Python-based backend/data processing)

    # Create a virtual environment (optional but recommended)
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    # Install Python dependencies (replace with your actual requirements file)
    pip install -r requirements.txt

    Run the application:
    (Specify the command to launch your dashboard, e.g., if using Dash/Streamlit/Flask)

    # Example for a Streamlit app:
    streamlit run dashboard.py

    # Example for a Dash/Flask app:
    python app.py

The dashboard will typically be available at http://localhost:8050 (or similar, depending on the framework).
📊 Usage
Data Format

The dashboard expects input data to be structured as follows:

    Spatial Data: A GeoJSON or shapefile containing the geographic units (geometry and a unique ID).

    Model Output Data: A CSV or database connection containing:

        ID (matching the spatial data).

        VARIABLE_NAME_1, VARIABLE_NAME_2, ... (The location factor values).

        IMPORTANCE_SCORE (The calculated importance metric for each factor).

Step-by-Step Guide

    Load Data: Use the provided data loader interface (or edit the default data source in config.py).

    Select Metric: Choose the variable importance metric you wish to display (e.g., "Gini Importance," "Permutation Score," "Coefficients").

    Explore Ranking: Analyze the main bar chart to identify the top-contributing factors.

    Map Visualization: Click on any variable in the ranking to display its underlying raw values or its influence score across the interactive map.

🤝 Contributing

We welcome contributions to enhance the visualization features and add support for more spatial modeling techniques!

    Fork the repository.

    Create your feature branch (git checkout -b feature/AmazingFeature).

    Commit your changes (git commit -m 'Add some AmazingFeature').

    Push to the branch (git push origin feature/AmazingFeature).

    Open a Pull Request to the feat/dashboard-visualization branch.

⚖️ License

Distributed under the MIT License. See LICENSE for more information.
📧 Contact

Cristian Vergara F.
Project Link: https://github.com/cristianvergaraf/location_factors_dashboard/