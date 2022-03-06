import requests
import json
import socket
import netifaces
from geopy.geocoders import Nominatim

'''
Calculating distance between two locations
'''

def get_coords_by_addr(address):
    try:
        nifti_locator_app = Nominatim(user_agent="nifti_web_app")
        location = nifti_locator_app.geocode(address)
        print(location)
        return (location.latitude, location.longitude)
    except Exception as e:
        print(e)
        return "Invalid Address"

start_coord = get_coords_by_addr("100 Gulf Fwy") 
end_coord = get_coords_by_addr("500 Baybrook Mall")

#float types
lat1 = str("{:.6f}".format(start_coord[0]))
long1 = str("{:.6f}".format(start_coord[1]))
lat2 = str("{:.6f}".format(end_coord[0]))
long2 = str("{:.6f}".format(end_coord[1]))

# call the OSMR API
req_string =f"http://router.project-osrm.org/route/v1/car/{long1},{lat1};{long2},{lat2}?overview=false"
res = requests.get(req_string)
routes = json.loads(res.content)
route1 = routes.get("routes")[0] #arr of routes
print(route1)

