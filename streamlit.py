import streamlit as st 
import pickle

model = pickle.load(open('model.pkl', 'rb'))

def main(): 
    st.title("Housing Price Predictor")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Housing Price Prediction App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    ocean_proximity_island = st.selectbox("Ocean Proximity Island", [0, 1])
    ocean_proximity_inland = st.selectbox("Ocean Proximity Inland", [0, 1])
    median_income = st.number_input("Median Income", value=0.0)
    longitude = st.number_input("Longitude", value=0.0)
    latitude = st.number_input("Latitude", value=0.0)
    
    if st.button("Predict"): 
        features = [[ocean_proximity_island, ocean_proximity_inland, median_income, longitude, latitude]]
        prediction = model.predict(features)
        
        st.success(f"The predicted housing price is {prediction[0]}")
      
if __name__=='__main__': 
    main()