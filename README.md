# Hackathon1-WSAD: Women Safety Analysis Dashboard

## Introduction

The Women Safety Analysis Dashboard is a Streamlit application designed to provide users with insights and resources related to women's safety in various Indian cities. It visualizes crime rate data, identifies safe and unsafe areas, suggests recommended hotels in safer zones, and offers quick access to emergency contact numbers. Additionally, the dashboard includes features for users to report transport-related discomfort, flag unsafe locations, and provide feedback for service improvement.

This project was developed as part of a hackathon.

## Features

*   **Crime Rate Visualization:** Displays a bar chart of crime rates across different cities.
*   **Safe/Unsafe Zones:** Shows designated safe and unsafe places for a user-selected city.
*   **Hotel Recommendations:** Provides a list of recommended hotels in safer areas of the selected city, with direct links to booking sites.
*   **Emergency Contacts:** Displays emergency helpline numbers specific to the selected city.
*   **Transport Complaint Submission:** Allows users to submit complaints regarding any discomfort experienced during travel. These are logged for potential review.
*   **Unsafe Location Reporting:** Enables users to report locations they perceive as unsafe, alerting relevant authorities (in a real-world scenario).
*   **Feedback Mechanism:** Collects user feedback for future improvements and enhancements to the dashboard.

## Data Sources

*   **Crime Data:** The crime rate information visualized in the dashboard is primarily sourced from the National Crime Records Bureau (NCRB).
*   **Hotel Information & Other Data:** Details regarding safe/unsafe places, hotel recommendations, and emergency numbers are currently hardcoded within the application for demonstration purposes.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
2.  **Install dependencies:**
    Make sure you have Python and pip installed. Then, install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Streamlit application:**
    ```bash
    streamlit run women_safety_analysis_dashboard.py
    ```
    The application should open in your default web browser.

## File Structure

*   `women_safety_analysis_dashboard.py`: The main Python script containing the Streamlit application logic.
*   `requirements.txt`: Lists all Python dependencies required to run the project.
*   `feedback.txt`: A text file where user-submitted feedback is stored.
*   `report.txt`: A text file used to log user-reported unsafe locations.
*   `transport_compliant.txt`: A text file for storing user complaints related to transport.
*   `README.md`: This file, providing an overview and instructions for the project.
*   `.devcontainer/`: Contains configuration for developing in a Docker container (e.g., for VS Code Remote - Containers).

**Note on data storage:** The use of `.txt` files for storing complaints, reports, and feedback is for simplicity in this hackathon project. For a production application, a more robust database solution would be recommended.
