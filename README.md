# 🌤️ Weather App

A modern, visually appealing weather application built with Streamlit. Instantly get current weather information for any city, with beautiful icons and a responsive UI.

---

## Features

- **Real-time Weather:** Fetches current weather data for any city using the OpenWeatherMap API.
- **Modern UI:** Clean, mobile-friendly interface with custom weather, humidity, and wind icons.
- **Error Handling:** Graceful error cards with custom 404 image for city not found.
- **Fast Search:** Search bar with instant results and a stylish search button.
- **No API Key in Code:** (Optional) Easily configure your own OpenWeatherMap API key for production use.

---

## Screenshots

![Weather Card Example](images/clear.png)

![404 City Not Found](images/404.png)

---

## Getting Started

### Prerequisites
- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [Requests](https://pypi.org/project/requests/)
- [Pandas](https://pypi.org/project/pandas/)
- [NumPy](https://pypi.org/project/numpy/)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Prath-Digital/Python_Streamlit_Pr.-2-Weather-App.git
   cd Python_Streamlit_Pr.-2-Weather-App
   ```

2. **Install dependencies:**
   ```bash
   python -m pip install -r requirements.txt
   ```
   **Or manualay:**
   ```bash
   python -m pip install streamlit requests base64
   ```

3. **Add your OpenWeatherMap API key:**

Open `app.py` and replace the `API_KEY `value with your own key, you can get one free at [OpenWeatherMap API](https://openweathermap.org/api).

4. **Run the app:**
    ```bash
    python -m streamlit run app.py
    ```

## Project Structure
```.
├── images/
│   ├── clear.png
│   ├── clouds.png
│   ├── drizzle.png
│   ├── humidity.png
│   ├── mist.png
│   ├── rain.png
│   ├── snow.png
│   ├── wind.png
│   └── 404.png
├── requirements.txt
├── app.py
├── README.md
```

## Customization
- Icons: Replace images in the images folder to change the look.

- Styling: Edit the CSS in app.py for further UI tweaks.

- API: Use your own API key for higher rate limits and reliability.

## License
This project is licensed under the MIT License. See LICENSE for details.

## Contact
For questions or suggestions, open an issue or contact Prath-Digital.
