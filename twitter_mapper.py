import locations
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import folium as fl


def do_geocode(geopy_object: object, address: str):
    """ str -> str

    Does geocode. This functions retries the request if a timeout occured.
    This will happen until the request goes through successfully.
    """
    try:
        return geopy_object.geocode(address)
    except GeocoderTimedOut:
        return do_geocode(geopy_object, address)


def revise_users(user_list: list):  # REMAKE INTO A DICT AND OTHER STUFF
    """ list -> list

    Modifies the input list. The new list looks like
    [(lat, long), 'username'].

    If any number of users happen to share the same location,
    this function will shift their latitudes by 0.0001 degrees each
    until no users are in the same spot.
    """
    revised_users = {}
    for user in user_list:
        revised_users[user[0]] = ' '.join([revised_users.get(user[0], ''), user[1]])
    return revised_users


def processing(geopy_object: object, user_info: list):
    """ list -> list

    Returns a processed user_info list.

    First, it maps the locations of list items to coordinates
    using geopy.
    Then, it filters the ones that didn't work.
    (no location data, or weird data that can not be transformed by geopy)
    Lastly, it searches for duplicate locations
    and each duplicate 0.0001 degrees to the east.
    """
    users = list(map(lambda x: (do_geocode(geopy_object, x[0]), x[1]), user_info))
    users = list(filter(lambda x: bool(x[0]), users))
    users = list(map(lambda x: ((x[0].latitude, x[0].longitude), x[1]), users))
    return revise_users(users)


def create_map(coordinates: list, my_loc: tuple):
    """ list -> None

    Creates a folium lib map centered on your location.
    On the map are markers of all users in your coordinates list.

    The map is then saved in index.html in your working directory.
    """
    if my_loc is not None:
        location = (my_loc.latitude, my_loc.longitude)
        zoom = 6
    else:
        location = (0, 0)
        zoom = 3
    world = fl.Map(location=location, zoom_start=zoom)

    for follower in coordinates:
        fl.Marker(
                location = (follower[0], follower[1]),
                popup = coordinates[follower],
                icon=fl.Icon(icon='user', prefix='fa')
        ).add_to(world)

    return world._repr_html_()


def user_analysis(username: str):
    """ str -> object

    Returns a folium.Map based on a twitter username.
    """
    geolocator = Nominatim(user_agent='twitter_locations')
    follower_info, my_loc = locations.get_locations(name=username)
    coordinates = processing(geolocator, follower_info)
    return create_map(coordinates, do_geocode(geolocator, my_loc))


if __name__ == "__main__":
    user_analysis('androy777')