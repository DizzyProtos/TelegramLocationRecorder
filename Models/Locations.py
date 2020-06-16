class LocationCreateModel:
    def __init__(self,
                 chat_link: str,
                 lat: float,
                 long: float,
                 timestamp: str = ''):
        self.chat_link = chat_link
        self.lat = lat
        self.long = long
        self.timestamp = timestamp


class LocationResponceModel:
    def __init__(self,
                 row_number: int,
                 is_succesful: bool):
        self.row_number = row_number
        self.is_succesful = is_succesful


class LocationUpdateModel:
    def __init__(self,
                 chat_link: str,
                 comment: str):
        self.chat_link = chat_link
        self.comment = comment
