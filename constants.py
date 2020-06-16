import sys


class _const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise self.ConstError("Can't rebind const(%s)" % key)
        self.__dict__[key] = value

    def __delattr__(self, item):
        if item in self.__dict__:
            raise self.ConstError("Can't unbind const(%s)" % item)
        raise NameError(item)

_const = _const()
_const.telegram_token = ''
_const.telegram_base_link = 'https://t.me/'

_const.google_token_file = r'C:\Users\user\PycharmProjects\okolobot\token.pickle'
_const.google_credentials_path = r'C:\Users\user\PycharmProjects\okolobot\credentials.json'
_const.google_client_id = '1245254582:AAEIi4tOehSlfSe1tBmC5MF_O3n8KA3Nn8o'
_const.client_secret = ''
_const.google_sheet_id = '1E8KubS7U05pVPtmZ7AtSWlAAEQgtINaqy4RtNDoKemE'

sys.modules[__name__] = _const
