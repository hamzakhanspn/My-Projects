import requests

def get_location_from_ip(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        country = data.get("country")
        region = data.get("region")
        city = data.get("city")
        location = f"{city}, {region}, {country}"
        return location
    else:
        return "Unable to retrieve location information."

# Example usage
ip_address = "112.79.166.127"  # Replace with the desired IP address
location = get_location_from_ip(ip_address)
print(f"Location for IP Address {ip_address}: {location}")
