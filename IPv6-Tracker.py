import requests

def track_ipv6_location(ipv6_address):
    url = f"https://ipinfo.io/{ipv6_address}?token=0d5b28b7f5c655"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        location = data.get("loc", "Unknown")
        city = data.get("city", "Unknown")
        region = data.get("region", "Unknown")
        country = data.get("country", "Unknown")
        return f"Location: {location}, City: {city}, Region: {region}, Country: {country}"
    else:
        return "Failed to retrieve location information."

# Usage example
ipv6_address = input("Enter the IPv6 address: ")
location_info = track_ipv6_location(ipv6_address)
print(location_info)
