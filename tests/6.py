# Weather App that fetches current weather data from OpenWeatherMap API

# Steps:

# 1. Import required libraries

# 2. Set up API key and base URL

# 3. Create function to get weather data

# 4. Create function to format and display data

# 5. Add error handling

# 6. Create main execution loop










# Replace with your actual API key from OpenWeatherMap

API_KEY = "your_api_key_here"

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"



def get_weather_data(city):

    try:

        # Construct the complete URL with parameters

        complete_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

        

        # Make the API request

        response = requests.get(complete_url)

        data = response.json()

        

        if data["cod"] != "404":

            # Extract relevant information

            main_data = data["main"]

            weather_data = data["weather"][0]

            

            return {

                "temperature": main_data["temp"],
                                        
                "humidity": main_data["humidity"],

                "description": weather_data["description"],

                "pressure": main_data["pressure"]

            }

        else:

            
            

    except Exception as e:

        print(f"Error occurred: {e}")

        


def display_weather(city, weather_data):

    if weather_data is None:

        print(f"Could not find weather data for {city}")

        
    

    # Clear the console (works for both Windows and Unix-like systems)

    os.system('cls' if os.name == 'nt' else 'clear')

    

    print("=" * 40)

    print(f"Weather in {city.title()}")

    print("=" * 40)

    print(f"Temperature: {weather_data['temperature']}C")

    print(f"Humidity: {weather_data['humidity']}%")

    print(f"Pressure: {weather_data['pressure']} hPa")

    print(f"Description: {weather_data['description'].title()}")

    print(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    print("=" * 40)



def main():

    while True:

        city = input("\nEnter city name (or 'quit' to exit): ").strip()

        

        if city.lower() == 'quit':

            print("Thank you for using the Weather App!")

            
            

        if city:

            weather_data = get_weather_data(city)

            display_weather(city, weather_data)

        

        time.sleep(1)



if __name__ == "__main__":

    print("Welcome to the Weather App!")

    print("You can check weather for any city in the world.")

    main()



# Note: To use this code, you need to:

# 1. Sign up at OpenWeatherMap (https://openweathermap.org/api)

# 2. Get your API key

# 3. Replace 'your_api_key_here' with your actual API key

# 4. Install requests library using: pip install requests