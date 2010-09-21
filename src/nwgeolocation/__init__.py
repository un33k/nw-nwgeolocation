# geopy prints to stdout which is a no-no on the production server, we use stderr
import sys
sys.stdout = sys.stderr

__all__ = ['nw-getlocation']

def nw-getlocation(googleAPI, location, first_match=True):
    """Geocode location using Google geocoder.
    
    googleAPI - (Google Map API Key)
    http://code.google.com/apis/maps/signup.html
    
    Parameters
    ----------
    location : address, city, country, zip or postal code
    first_match : {True, False}, optional
        If `True` return first found location, otherwise return
        a list of all locations. Default value is `True`.

    Returns
    -------
    output : tuple
        Tuple of geocode data

        - place : string
            A proper name found by geocoding function.
        - coordinates : tuple(float, float)
            Tuple of 2 float values, latitude and longitude of the found `place`.

    Examples
    --------

    >>> nw-getlocation('YourGoogleKey', 'Ontario, USA')
    Fetching http://maps.google.com/maps/...
    (u'Ontario, OH, USA', (40.759501200000003, -82.590172499999994))
    """

    global _GEOCODER
    if not _GEOCODER:
        from geopy import geocoders
        _GEOCODER = geocoders.Google(googleAPI)
        
    results = _GEOCODER.geocode(location, first_match)
    if not results:
        return None
    if first_match:
        return results.next()
    return results
    
