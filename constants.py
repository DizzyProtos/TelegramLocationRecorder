import sys
import os

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
_const.telegram_token = os.environ.get('TELEGRAM_TOKEN')
_const.telegram_base_link = 'https://t.me/'

_const.google_token_file = r'token.json'
# todo: add token as env var
# create token.json
# token = os.environ.get('GOOGLE_TOKEN', '')
# if token != '':
#     with open(_const.google_token_file, 'w') as f:
#         f.writelines(token)

_const.google_credentials_path = r'credentials.json'
# Create credentials.json
creds = os.environ.get('GOOGLE_CREDENTIALS_JSON')
# with open(_const.google_credentials_path, 'w') as f:
#     f.writelines(creds)
_const.google_client_id = '1245254582:AAEIi4tOehSlfSe1tBmC5MF_O3n8KA3Nn8o'
_const.client_secret = os.environ.get('GOOGLE_SECRET')
_const.google_sheet_id = '1E8KubS7U05pVPtmZ7AtSWlAAEQgtINaqy4RtNDoKemE'

_const.app_port = os.environ.get('PORT', 5000)


sys.modules[__name__] = _const
