# Import necessary libraries

Import HttpClientLibrary
Import JSONLibrary
Import EmailLibrary
Import SMSLibrary
Import SchedulerLibrary
Import WeatherDataParser

# Define constants and configuration

CONST WEATHER_API_SOURCES = ["https://api.weather1.com", "https://api.weather2.com", "https://api.weather3.com"]
CONST EMAIL_SERVER_CONFIG = {SMTP_SERVER: "smtp.example.com", PORT: 587, USERNAME: "user", PASSWORD: "pass"}
CONST SMS_SERVICE_CONFIG = {API_KEY: "sms_api_key", API_URL: "https://smsprovider.com/api"}
CONST SEVERE_WEATHER_THRESHOLD = {TEMPERATURE: 40, WIND_SPEED: 20, PRECIPITATION: 50}
CONST USER_CONTACTS = [{NAME: "User1", EMAIL: "user1@example.com", PHONE: "+1234567890"}, {...}]

# Function to fetch weather data

Function fetchWeatherData(sourceUrl):
    response = HttpClientLibrary.get(sourceUrl)
    If response.status_code == 200:
        return JSONLibrary.parse(response.body)
    Else:
        Log("Failed to fetch data from " + sourceUrl)
        return None
EndFunction

# Function to aggregate data from multiple sources

Function aggregateWeatherData():
    aggregatedData = []
    For source in WEATHER_API_SOURCES:
        data = fetchWeatherData(source)
        If data is not None:
            aggregatedData.append(data)
    Return WeatherDataParser.parse(aggregatedData)
EndFunction

# Function to check for severe weather conditions

Function checkSevereWeather(weatherData):
    If weatherData.temperature > SEVERE_WEATHER_THRESHOLD.TEMPERATURE:
        Return True, "High temperature alert!"
    If weatherData.wind_speed > SEVERE_WEATHER_THRESHOLD.WIND_SPEED:
        Return True, "High wind speed alert!"
    If weatherData.precipitation > SEVERE_WEATHER_THRESHOLD.PRECIPITATION:
        Return True, "Heavy precipitation alert!"
    Return False, ""
EndFunction

# Function to send email alerts

Function sendEmailAlert(user, message):
    emailClient = EmailLibrary.connect(EMAIL_SERVER_CONFIG)
    emailClient.send(to=user.EMAIL, subject="Severe Weather Alert", body=message)
EndFunction

# Function to send SMS alerts

Function sendSMSAlert(user, message):
    SMSLibrary.send(SMS_SERVICE_CONFIG.API_URL, API_KEY=SMS_SERVICE_CONFIG.API_KEY, to=user.PHONE, message=message)
EndFunction

# Function to alert users

Function alertUsers(weatherData):
    isSevere, message = checkSevereWeather(weatherData)
    If isSevere:
        For user in USER_CONTACTS:
            sendEmailAlert(user, message)
            sendSMSAlert(user, message)
EndFunction

# Main function to schedule and run the weather alert system

Function main():
    SchedulerLibrary.schedule(interval="1 hour", task=runWeatherAlertSystem)
EndFunction

Function runWeatherAlertSystem():
    weatherData = aggregateWeatherData()
    If weatherData is not None:
        alertUsers(weatherData)
EndFunction

# Start the system
main()
