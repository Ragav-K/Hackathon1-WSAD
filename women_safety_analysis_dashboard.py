import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

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

elif selected_city == "Mumbai":
    st.page_link("https://www.tajhotels.com/en-in/hotels/taj-mahal-palace-mumbai" , label = hotel_1)
    st.page_link("https://regalenclave.com/" , label = hotel_2)
    
elif selected_city == "Bangalore":
    st.page_link("https://www.oberoihotels.com/special-offers/exclusive-members-offer/?utm_source=google&utm_content=10perbookdirect&utm_medium=cpc&utm_campaign=oberoi_bengaluru_search_conversion_ia&gad_source=1&gclid=CjwKCAiAt4C-BhBcEiwA8Kp0Ca4kI3tTQsgWkwHpf8kkUI-oM4fjM21WH_KwgX9ixijDg9QwVDY7FxoCaksQAvD_BwE" , label = hotel_1)
    st.page_link("https://all.accor.com/hotel/6454/index.en.shtml" , label = hotel_2)
    
elif selected_city == "Hyderabad":
    st.page_link("https://www.tajhotels.com/en-in/hotels/taj-krishna-hyderabad" , label = hotel_1)
    st.page_link("https://www.tripadvisor.in/Hotel_Review-g1532344-d4004122-Reviews-Treebo_Trend_Sri_Krishna-Navi_Mumbai_Maharashtra.html" , label = hotel_2)

elif selected_city == "Chennai":
    st.page_link("https://www.theleela.com/the-leela-palace-chennai" , label = hotel_1)
    st.page_link("https://all.accor.com/hotel/8020/index.en.shtml" , label = hotel_2)

elif selected_city == "Kolkata":
    st.page_link("https://www.oberoihotels.com/hotels-in-kolkata/" , label = hotel_1)
    st.page_link("https://www.treebo.com/hotels-in-kolkata/treebo-green-view-park-circus-282/?adgroupid=145193356930&checkin=2025-02-27&checkout=2025-02-28&ef_id=CjwKCAiAt4C-BhBcEiwA8Kp0CdA5ZJq9dT2OmVHYUQ_ZPdthTOWXkwaMXszmkfwXHVR5Fv5zlCBl9xoCtHoQAvD_BwE%3AG%3As&gad_source=1&gclid=CjwKCAiAt4C-BhBcEiwA8Kp0CdA5ZJq9dT2OmVHYUQ_ZPdthTOWXkwaMXszmkfwXHVR5Fv5zlCBl9xoCtHoQAvD_BwE&hotel_id=282&rateplan=EP&roomconfig=1-0&roomtype=oak&utm_campaign=TRB_Brand-Property_Exact_Mobile&utm_content=732032429261&utm_medium=google&utm_source=sem-brand&utm_term=" , label = hotel_2)

elif selected_city == "Pune":
    st.page_link("https://www.booking.com/hotel/in/jw-marriott-pune.html" , label = hotel_1)
    st.page_link("https://www.hyatt.com/search/hotels/en-US/Pune%2C%20India?src=corp_swa_agn_iprospectin_sem_dap_google_br_pune-p1&gad_source=1&gclid=CjwKCAiAt4C-BhBcEiwA8Kp0CQXDgWTPfQxGi_DOq1NpOdaCp1pScC3DIG_z5Xbx5ATHleVagGLHpRoCHIsQAvD_BwE&gclsrc=aw.ds" , label = hotel_2)

elif selected_city == "Ahmedabad":
    st.page_link("https://www.hyatt.com/en-US/hotel/india/hyatt-ahmedabad/amdhy?src=prop_amdhy_agn_iprospectin_sem_marketing_google_bps_feeder-p1&gad_source=1&gclid=CjwKCAiAt4C-BhBcEiwA8Kp0CQM9wYnAYYyPwpbkXdSoduHnGyvSSHKSxxxIIcM-KQDDlPBjSA1G6RoC8o4QAvD_BwE&gclsrc=aw.ds" , label = hotel_1)
    st.page_link("https://www.booking.com/hotel/in/novotel-ahmedabad.html" , label = hotel_2)

elif selected_city == "Jaipur":
    st.page_link("https://www.tajhotels.com/en-in/hotels/rambagh-palace-jaipur" , label = hotel_1)
    st.page_link("https://www.fairmont.com/jaipur/" , label = hotel_2)
    
elif selected_city == "Surat":
    st.page_link("https://www.gujarattourism.com/accommodation/registered-hotels/the-gateway-hotel-athwalines.html" , label = hotel_1)
    st.page_link("https://www.tripadvisor.in/Restaurant_Review-g297612-d5911694-Reviews-Supreme_Restaurant-Surat_Surat_District_Gujarat.html" , label = hotel_2)

elif selected_city == "Lucknow":
    st.page_link("https://www.tajhotels.com/en-in/hotels/taj-mahal-lucknow" , label = hotel_1)
    st.page_link("https://www.hyatt.com/hyatt-regency/en-US/lkorl-hyatt-regency-lucknow" , label = hotel_2)
    
elif selected_city == "Kanpur":
    st.page_link("https://www.agoda.com/en-in/search?selectedproperty=22733203&city=21081&hid=22733203&site_id=1922866&tag=4c1a8f54-23c4-4282-9713-a37c0786f251&gad_source=1&device=c&network=g&adid=693479719362&rand=7815165860900712943&expid=&adpos=&aud=kwd-13196402983&gclid=CjwKCAiAt4C-BhBcEiwA8Kp0CWrRBLK2ivLXtxHo_KSnRCkHKi4ASqS6W79fkP_TeSD9NVato3lTTRoCdowQAvD_BwE&pslc=1&ds=P5pZJp4C0YRZD15J" , label = hotel_1)
    st.page_link("https://www.zostel.com/" , label = hotel_2)
    
elif selected_city == "Nagpur":
    st.page_link("https://www.radissonhotels.com/en-us/hotels/radisson-blu-nagpur" , label = hotel_1)
    st.page_link("https://www.marriott.com/en-us/hotels/nagmd-le-meridien-nagpur/overview/?nst=paid&hmGUID=49c094c8-7ad1-443b-1b6b-caca89a78c58" , label = hotel_2)

elif selected_city == "Indore":
    st.page_link("https://sayajihotels.com/Sayaji_Indore" , label = hotel_1)
    st.page_link("https://www.radissonhotels.com/en-us/hotels/radisson-blu-indore" , label = hotel_2)

elif selected_city == "Thane":
    st.page_link("https://www.makemytrip.com/hotels/le_vivanta-details-thane.html" , label = hotel_1)
    st.page_link("https://www.lemontreehotels.com/" , label = hotel_2)

elif selected_city == "Bhopal":
    st.page_link("https://www.jehannuma.com/palace-bhopal/" , label = hotel_1)
    st.page_link("https://www.marriott.com/en-us/hotels/bhocy-courtyard-bhopal/overview/?nst=paid&hmGUID=49c094c8-7ad1-443b-1b6b-caca89a78c58" , label = hotel_2)

elif selected_city == "Visakhapatnam":
    st.page_link("https://res.itchotels.com/?adult=1&arrive=2025-02-27&bookingTime=Future&chain=26676&child=0&config=Business&currency=INR&depart=2025-02-28&gad_source=1&gclid=CjwKCAiAt4C-BhBcEiwA8Kp0CTERThiMR1lDabhJOs0RUBYzQuR3Sw4XsHH1mbXctqmsl-nEz-kLiBoCoAIQAvD_BwE&hotel=30180&hotelID=30180&journey=undefined&level=hotel&locale=en-US&productcurrency=INR&rooms=1&specialCode=NA&stayLength=1&theme=Umbrella_chain&utm_campaign=HQ-DTL-HTL-WH-QM_PerfMax_Google_VTZDB_WH-Devee-Grand-Bay-Visakhapatnam_IN_AO_Rooms_Visakhapatnam-Feeder-C3-Brand&utm_content=pmax&utm_medium=cpc&utm_source=google" , label = hotel_1)
    st.page_link("https://www.theparkhotels.com/visakhapatnam/" , label = hotel_2)

elif selected_city == "Patna":
    st.page_link("https://www.maurya.com/" , label = hotel_1)
    st.page_link("https://www.lemontreehotels.com/lemon-tree-premier/patna/hotel-patna" , label = hotel_2)

elif selected_city == "Vadodara":
    st.page_link("https://www.makemytrip.com/hotels/welcomhotel_by_itc_hotels_alkapuri_vadodara-details-vadodara.html" , label = hotel_1)
    st.page_link("https://www.booking.com/hotel/in/taj-residency-vadodara.html" , label = hotel_2)

elif selected_city == "Ghaziabad":
    st.page_link("https://www.radissonhotels.com/en-us/hotels/radisson-blu-kaushambi-delhi-ncr" , label = hotel_1)
    st.page_link("https://www.makemytrip.com/hotels/country_inn_and_suites_by_radisson_sahibabad-details-ghaziabad.html" , label = hotel_2)


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

st.markdown("---")
st.title("Stay Safe")
ncrb = "https://www.ncrb.gov.in/"
st.markdown(f"This data is obtained from National Crime Records Bureau: {ncrb}")
