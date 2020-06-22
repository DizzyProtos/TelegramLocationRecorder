import osmapi
import constants
from Models.Locations import LocationCreateModel


class OSMapService:
    def __init__(self):
        self.api = osmapi.OsmApi(api=constants.osm_api_link,
                                 username=constants.osm_login,
                                 password=constants.osm_password)

    def add_location_to_map(self, location: LocationCreateModel):
        self.api.ChangesetCreate({u'comment': location.chat_link})
        self.api.NodeCreate({u"lon":location.long, u"lat":location.lat, u"tag": {}})
        self.api.ChangesetClose()
