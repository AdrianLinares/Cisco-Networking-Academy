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
