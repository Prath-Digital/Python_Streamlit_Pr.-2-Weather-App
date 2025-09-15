import streamlit as st
import requests
import pandas as pd
import numpy as np
import base64

# Page configuration
st.set_page_config(
    page_title="Weather App",
    page_icon="🌤️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS to match the original design
st.markdown(
    """
<style>
    .main {
        background-color: rgb(100, 100, 100);
    }
    
    .weather-card {
        background: linear-gradient(135deg, #00feba, #5b548a);
        color: white;
        padding: 40px 35px;
        border-radius: 20px;
        text-align: center;
        margin: 20px auto;
        max-width: 470px;
    }
    
    .weather-icon {
        font-size: 120px;
        margin: 20px 0;
    }
    
    .temperature {
        font-size: 80px;
        font-weight: 500;
        margin: 10px 0;
    }
    
    .city-name {
        font-size: 45px;
        font-weight: 400;
        margin-bottom: 30px;
    }
    
    .weather-details {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 30px;
        padding: 0 20px;
    }
    
    .detail-col {
        text-align: center;
        flex: 1;
    }
    
    .detail-icon {
        font-size: 40px;
        margin-bottom: 10px;
    }
    
    .detail-value {
        font-size: 28px;
        font-weight: bold;
        margin: 5px 0;
    }
    
    .detail-label {
        font-size: 14px;
        opacity: 0.8;
    }
    
    .stTextInput > div > div > input {
        border: none;
        padding: 10px 25px;
        height: 60px;
        font-size: 25px;
    }
    
    .stButton > button {
        background-color: #ebfffc;
        color: #555;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        border: none;
        font-size: 20px;
    }
    
    .error-message {
        color: #ff6b6b;
        font-size: 18px;
        text-align: center;
        margin: 20px 0;
    }
</style>
""",
    unsafe_allow_html=True,
)

# API configuration
API_KEY = "2c45b1409a0b712c579b8d9202a08fa7"
API_URL = "https://api.openweathermap.org/data/2.5/weather?units=metric&q="

# Weather icons mapping
WEATHER_IMAGES = {
    "Clear": "images/clear.png",
    "Clouds": "images/clouds.png",
    "Rain": "images/rain.png",
    "Drizzle": "images/drizzle.png",
    "Mist": "images/mist.png",
    "Snow": "images/snow.png",
    "Thunderstorm": "images/rain.png",
    "Haze": "images/mist.png",
    "Fog": "images/mist.png",
}


def fetch_weather_data(city):
    """Fetch weather data from OpenWeatherMap API"""
    try:
        response = requests.get(f"{API_URL}{city}&appid={API_KEY}")
        data = response.json()

        if data.get("cod") != 200:
            return None, "City not found"

        return data, None
    except requests.exceptions.RequestException:
        return None, "Network error"
    except Exception as e:
        return None, "Error fetching weather data"


def display_weather_card(weather_data):
    """Display weather information in a card format"""
    city_name = weather_data["name"]
    temperature = round(weather_data["main"]["temp"])
    humidity = weather_data["main"]["humidity"]
    wind_speed = round(weather_data["wind"]["speed"] * 3.6, 1)  # Convert m/s to km/h
    weather_main = weather_data["weather"][0]["main"]
    weather_image = WEATHER_IMAGES.get(weather_main, "images/clear.png")

    def image_to_base64(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    weather_img_b64 = image_to_base64(weather_image)
    humidity_img_b64 = image_to_base64("images/humidity.png")
    wind_img_b64 = image_to_base64("images/wind.png")

    # Create weather card HTML with embedded images
    weather_card_html = f"""
    <div class="weather-card">
        <div class="weather-icon"><img src='data:image/png;base64,{weather_img_b64}' alt='{weather_main} icon' style='width:120px;'></div>
        <div class="temperature">{temperature}°C</div>
        <div class="city-name">{city_name}</div>
        <div class="weather-details">
            <div class="detail-col">
                <div class="detail-icon"><img src='data:image/png;base64,{humidity_img_b64}' alt='Humidity Icon' style='width:40px;'></div>
                <div class="detail-value">{humidity}%</div>
                <div class="detail-label">Humidity</div>
            </div>
            <div class="detail-col">
                <div class="detail-icon"><img src='data:image/png;base64,{wind_img_b64}' alt='Wind Speed Icon' style='width:40px;'></div>
                <div class="detail-value">{wind_speed} km/h</div>
                <div class="detail-label">Wind Speed</div>
            </div>
        </div>
    </div>
    """

    st.markdown(weather_card_html, unsafe_allow_html=True)


def display_error_card(error_message):
    """Display error message in card format"""
    import base64
    def image_to_base64(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    humidity_img_b64 = image_to_base64("images/humidity.png")
    wind_img_b64 = image_to_base64("images/wind.png")

    # Show 404 image if city not found
    if error_message.strip().lower() == "city not found":
        not_found_img_b64 = image_to_base64("images/404.png")
        error_card_html = f"""
        <div class="weather-card">
            <div class="weather-icon"><img src='data:image/png;base64,{not_found_img_b64}' alt='404 City Not Found' style='width:450px;'></div>
            <div class="temperature">--°C</div>
            <div class="weather-details">
                <div class="detail-col">
                    <div class="detail-icon"><img src='data:image/png;base64,{humidity_img_b64}' alt='Humidity Icon' style='width:40px;'></div>
                    <div class="detail-value">--%</div>
                    <div class="detail-label">Humidity</div>
                </div>
                <div class="detail-col">
                    <div class="detail-icon"><img src='data:image/png;base64,{wind_img_b64}' alt='Wind Speed Icon' style='width:40px;'></div>
                    <div class="detail-value">-- km/h</div>
                    <div class="detail-label">Wind Speed</div>
                </div>
            </div>
        </div>
        """
    else:
        error_card_html = f"""
        <div class="weather-card">
            <div class="weather-icon">❌</div>
            <div class="city-name">{error_message}</div>
            <div class="temperature">--°C</div>
            <div class="weather-details">
                <div class="detail-col">
                    <div class="detail-icon"><img src='data:image/png;base64,{humidity_img_b64}' alt='Humidity Icon' style='width:40px;'></div>
                    <div class="detail-value">--%</div>
                    <div class="detail-label">Humidity</div>
                </div>
                <div class="detail-col">
                    <div class="detail-icon"><img src='data:image/png;base64,{wind_img_b64}' alt='Wind Speed Icon' style='width:40px;'></div>
                    <div class="detail-value">-- km/h</div>
                    <div class="detail-label">Wind Speed</div>
                </div>
            </div>
        </div>
        """

    st.markdown(error_card_html, unsafe_allow_html=True)

# Main application
def main():
    st.title("🌤️ Weather App")
    st.write("Enter a city name to get the current weather information.")

    # Input field and search button in a single, perfectly aligned row
    st.markdown("""
    <style>
    .search-row-container {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 24px;
        gap: 12px;
    }
    .stTextInput > div > div {
        display: flex !important;
        align-items: flex-start !important;
        height: 56px !important;
    }
    .stTextInput input {
        font-size: 20px !important;
        border-radius: 30px !important;
        background: #23242a !important;
        color: #fff !important;
        border: none !important;
        outline: none !important;
        box-shadow: 0 2px 8px rgba(91,84,138,0.10);
        width: 320px !important;
        margin-bottom: 0 !important;
        height: 44px !important;
        padding: 6px 25px 0 25px !important;
        box-sizing: border-box !important;
        display: block !important;
    }
    .stTextInput input::placeholder {
        color: #bbb !important;
        opacity: 1 !important;
        font-size: 20px !important;
        padding-top: 6px !important;
        box-sizing: border-box !important;
    }
    .search-btn button {
        background: #fff !important;
        border: 2px solid #5b548a !important;
        border-radius: 50% !important;
        padding: 0 !important;
        box-shadow: 0 2px 8px rgba(91,84,138,0.10);
        cursor: pointer;
        transition: box-shadow 0.2s, border-color 0.2s;
        outline: none;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 56px !important;
        width: 56px !important;
        margin-bottom: 0 !important;
        font-size: 28px !important;
    }
    .search-btn button:hover {
        box-shadow: 0 4px 16px rgba(91,84,138,0.18);
        border-color: #00feba;
    }
    </style>
    """, unsafe_allow_html=True)

    # Use Streamlit columns for accessibility, but wrap in a flexbox for pixel-perfect alignment
    st.markdown('<div class="search-row-container">', unsafe_allow_html=True)
    col1, col2 = st.columns([4, 1], gap="small")
    with col1:
        city = st.text_input("", value="", max_chars=50, placeholder="Enter city name", key="city_input", label_visibility="collapsed")
    with col2:
        search_clicked = st.button("🔍 Search", key="search_btn_unique", help="Search", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if search_clicked:
        if city.strip() == "":
            display_error_card("Please enter a city name")
        else:
            weather_data, error = fetch_weather_data(city)
            if error:
                display_error_card(error)
            else:
                display_weather_card(weather_data)
    elif city.strip() != "":
        weather_data, error = fetch_weather_data(city)
        if error:
            display_error_card(error)
        else:
            display_weather_card(weather_data)

if __name__ == "__main__":
    main()