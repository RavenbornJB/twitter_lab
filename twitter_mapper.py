import locations
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import folium as fl


def do_geocode(address: str):
    """ str -> str

    Does geocode. This functions retries the request if a timeout occured.
    This will happen until the request goes through successfully.
    """
    try:
        return geolocator.geocode(address)
    except GeocoderTimedOut:
        return do_geocode(address)


def revise_users(user_list: list):
    """ list -> list

    Modifies the input list. The new list looks like
    [(lat, long), 'username'].

    If any number of users happen to share the same location,
    this function will shift their latitudes by 0.0001 degrees each
    until no users are in the same spot.
    """
    revised_user_list = []
    locations = []
    for user in user_list:
        title = user[1]
        repetitions = locations.count(user[0])
        coordinates = (int(user[0][0]), int(user[0][1]) + repetitions / 10000)
        locations.append(user[0])
        revised_user_list.append((coordinates, title))
    return revised_user_list


def processing(user_info: list):
    """ list -> list

    Returns a processed user_info list.

    First, it maps the locations of list items to coordinates
    using geopy.
    Then, it filters the ones that didn't work.
    (no location data, or weird data that can not be transformed by geopy)
    Lastly, it searches for duplicate locations
    and each duplicate 0.0001 degrees to the east.
    """
    users = list(map(lambda x: (do_geocode(x[0]), x[1]), user_info))
    users = list(filter(lambda x: bool(x[0]), users))
    users = list(map(lambda x: ((x[0].latitude, x[0].longitude), x[1]), users))
    return revise_users(users)


def create_map(coordinates: list):
    """ list -> None

    Creates a folium lib map.
    On the map are markers of all users in your coordinates list.

    The map is then saved in index.html in your working directory.
    """
    world = fl.Map()

    for follower in coordinates:
        fl.Marker(
                location = (follower[0][0], follower[0][1]),
                popup = follower[1],
                icon=fl.Icon(icon='user', prefix='fa')
        ).add_to(world)

    world.save('index.html')


if __name__ == '__main__':
    geolocator = Nominatim(user_agent='twitter_locations')
    follower_info = locations.get_locations()
    coordinates = processing(follower_info)
    create_map(coordinates)
    print('HTML map created! Open index.html in your browser to view it.')