import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "VP0NZYy2qFvRtu6DD1MZxmh8IGUeUaC9"

while True:
    orig = input("Starting Location: ")
    if orig == "q" or orig == "Q" or orig == "quit" or orig == "Quit" or orig == "QUIT":
        break
    dest = input("Destination: ")
    if dest == "q" or dest == "Q" or dest == "quit" or dest == "Quit" or dest == "QUIT":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")
