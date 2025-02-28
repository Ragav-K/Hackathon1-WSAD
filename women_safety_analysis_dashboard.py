import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

# Admin password (you can change this to something more secure)
ADMIN_PASSWORD = "Hackrizz"  # Replace with a strong password

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    
    # Create tables if they don't exist
    c.execute('''CREATE TABLE IF NOT EXISTS complaints 
                 (id INTEGER PRIMARY KEY, complaint TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS reports 
                 (id INTEGER PRIMARY KEY, location TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS feedback 
                 (id INTEGER PRIMARY KEY, feedback TEXT)''')
    
    conn.commit()
    conn.close()

# Function to insert data into the database
def insert_data(table_name, data):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO {table_name} ({table_name[:-1]}) VALUES (?)", (data,))
    conn.commit()
    conn.close()

# Function to fetch data from the database
def fetch_data(table_name):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table_name}")
    data = c.fetchall()
    conn.close()
    return data

# Initialize the database
init_db()

# Your existing data and UI code
data = {
    "City": ["Delhi", "Mumbai", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Surat", "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Visakhapatnam", "Patna", "Vadodara", "Ghaziabad"],
    "Crime rate": [13000, 5000, 3500, 2800, 2000, 1800, 2200, 1500, 1200, 900, 2000, 1300, 1100, 1000, 800, 900, 700, 1500, 800, 1200],
    "Emergency number": ["1091", "103", "1091", "1091", "1091", "1091", "1091", "1091", "1091", "1091", "1091", "1091", "1091", "1091", "1091", "1091", "1091", "1091", "1091", "1091"],
    "Safe place": ["Connaught Place", "Marine Drive", "Indiranagar", "Banjara Hills", "T Nagar", "Park Street", "Koregaon Park", "SG Highway", "Vaishali Nagar", "Vesu", "Gomti Nagar", "Civil Lines", "Ramdaspeth", "Vijay Nagar", "Hiranandani Estate", "Arera Colony", "Rushikonda Beach Area", "Boring Road", "Alkapuri", "Vaishali"],
    "Unsafe place": ["Paharganj", "Kurla", "Majestic", "Old City (Charminar Arer)", "Washermanpet", "Barabazar", "Hadapsar (Industrial Area)", "Naroda", "Ramganj", "Limbayat", "Charbagh", "Panki", "Kamptee Road", "Banganga", "Mumbra", "Bairagarh", "Gajuwaka", "Patna Junction Aarea", "Fatehpura", "Loni"]
}

Hotels = {
    "Delhi": ["The Lalit New Delhi", "Bloomrooms @ Janpath"],
    "Mumbai": ["Taj Mahal Palace", "Hotel Regal Enclave"],
    "Bangalore": ["The Oberoi Bangalore", "Ibis Bangalore City Centre"],
    "Hyderabad": ["Taj Krishna", "Treebo Trend Sri Krishna Residency"],
    "Chennai": ["The Leela Palace", "Ibis Chennai City Centre"],
    "Kolkata": ["The Oberoi Grand", "Treebo Trend Vedanta"],
    "Pune": ["JW Marriott Pune", "Hyatt Pune"],
    "Ahmedabad": ["Hyatt Ahmedabad", "Novotel Ahmedabad"],
    "Jaipur": ["Rambagh Palace", "Fairmont Jaipur"],
    "Surat": ["The Gateway Hotel", "Hotel Supreme"],
    "Lucknow": ["Taj Mahal Lucknow", "Hyatt Regency Lucknow"],
    "Kanpur": ["Hotel Landmark", "Zostel Kanpur"],
    "Nagpur": ["Radisson Blu Nagpur", "Le Meridien Nagpur"],
    "Indore": ["Sayaji Indore", "Radisson Blu Indore"],
    "Thane": ["Vivanta Thane", "Lemon Tree Thane"],
    "Bhopal": ["Jehan Numa Palace", "Courtyard by Marriott Bhopal"],
    "Visakhapatnam": ["Taj Visakhapatnam", "The Park Visakhapatnam"],
    "Patna": ["Hotel Maurya Patna", "Lemon Tree Premier Patna"],
    "Vadodara": ["WelcomHotel Vadodara", "Taj Vivanta Vadodara"],
    "Ghaziabad": ["Radisson Ghaziabad", "Country Inn & Suites Ghaziabad"]
}

data_frame = pd.DataFrame(data)
data_frame_1 = pd.DataFrame(Hotels)

st.title("Women Safety Analysis Dashboard")

red_color = ["#FFCCCB", "#FF6666", "#FF0000", "#CC0000", "#800000"]
graph = px.bar(data_frame, x="City", y="Crime rate", title="Crime Rate in Different Areas", color="Crime rate", color_continuous_scale=red_color, height=500)
st.plotly_chart(graph)

st.subheader("Safe & Unsafe Area")
selected_city = st.selectbox("Select a city", data_frame["City"])
city_data = data_frame[data_frame["City"] == selected_city].iloc[0]

st.write(f"Safe Place in {selected_city}: {city_data['Safe place']}")
st.write(f"Unsafe Place in {selected_city}: {city_data['Unsafe place']}")

hotel_1, hotel_2 = Hotels[selected_city]

st.subheader("Recommended Hotels in Safe Places:")
st.write("Note: Click on the Hotel name to access the hotel booking site.")

if selected_city == "Delhi":
    st.page_link("https://www.thelalit.com/the-lalit-delhi/" , label = hotel_1)
    st.page_link("https://staybloom.com/hotels/delhi/bloomrooms-janpath?utm_source=Google&utm_medium=cpc&utm_campaign=gb-delhi&couponCode=BLOOM15&gad_source=1&gclid=CjwKCAiAt4C-BhBcEiwA8Kp0Ccjpo00GSPPKo24GqEirXvS2BMQRkxcEuIeO-LJueE-FggEf4OvNMxoCzRYQAvD_BwE" , label = hotel_2)

# ... (rest of the hotel links remain the same)

# Transport Complaints
st.subheader("Enter the discomfort you feel during your travel:")
st.warning("Enter your details along with the vehicle info (Like: Registration number).")
comp = st.text_area("Enter the complaint")
if st.button("Submit Complaint"):
    if comp:
        insert_data("complaints", comp)
        st.success("Your complaint has been informed to the Police and Emergency Response Support Team (Helpline:112).")
    else:
        st.warning("Enter the complaint before submitting.")

# Unsafe Location Reports
st.subheader("Report if you feel any location is unsafe:")
unsafe_location = st.text_input("Enter the unsafe location:")
if st.button("Submit Report"):
    if unsafe_location:
        insert_data("reports", unsafe_location)
        st.success(f"Reported the place *{unsafe_location}* as unsafe. Authorities will be alerted.")
    else:
        st.warning("Please enter a location before reporting.")

# Feedback
feedback = st.text_area("Provide feedback to see improvement:")
if st.button("Submit Feedback"):
    if feedback:
        insert_data("feedback", feedback)
        st.success("Thank you for your feedback! We have received it.")
    else:
        st.warning("Please enter feedback before submitting.")

# Admin Section (Restricted Access)
st.markdown("---")
st.subheader("Admin Login")
admin_password = st.text_input("Enter Admin Password", type="password")

if admin_password == ADMIN_PASSWORD:
    st.success("Admin access granted!")
    
    # Export Data
    st.subheader("Export Data")
    table_name = st.selectbox("Select a table to export", ["complaints", "reports", "feedback"])
    if st.button("Export Data"):
        data = fetch_data(table_name)
        if data:
            df = pd.DataFrame(data, columns=["ID", table_name[:-1]])
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"{table_name}.csv",
                mime="text/csv",
            )
        else:
            st.write("No data found in the selected table.")
else:
    if admin_password:  # Only show warning if the user has entered something
        st.error("Incorrect password. Access denied.")

st.markdown("---")
st.title("Stay Safe")
ncrb = "https://www.ncrb.gov.in/"
st.markdown(f"This data is obtained from National Crime Records Bureau: {ncrb}")
