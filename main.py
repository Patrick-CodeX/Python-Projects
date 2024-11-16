
# import tkinter as tk
#
# import requests
#
# import time

# def getweather():
#     city = textfield.get()
#
#
# canvas = tk.Tk()
# canvas.geometry("600x500")
# canvas.title("Weather App")
#
# f = ("poppins", 15, "bold")
# t = ("poppins", 35, "bold")
#
# textfield = tk.Entry(canvas, font = t)
# textfield.pack(pady = 20)
# textfield.focus()
#
# label1 = tk.Label(canvas, font = t)
# label1.pack()
# label2 = tk.Label(canvas, font = f)
# label2.pack()
#
# canvas.mainloop()
#

import requests
import json

url = "https://foreca-weather.p.rapidapi.com/current/102643743"

querystring = {"alt":"0","tempunit":"C","windunit":"MS","tz":"Europe/London","lang":"en"}

headers = {
	"X-RapidAPI-Key": "e95643c781msh2725b48cb3b6d9ap132673jsn8f51b838b52d",
	"X-RapidAPI-Host": "foreca-weather.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Check if the request was successful
if response.status_code == 200:
    # Open a file in write mode
    with open("weather_data.txt", "a") as file:
        # Format the JSON data with indentation and write it to the file
        formatted_data = json.dumps(response.json(), indent=4)
        file.write(formatted_data)
        print("Data written to weather_data.txt")
else:
    print("Request failed with status code:", response.status_code)


