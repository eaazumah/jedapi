__author__ = 'Ebenezer Adelwin Azumah'

import os
from .config import Development, Production, Config


def is_in_development():
    # type: () -> bool
    return False if os.environ.get('MODE') == 'PROD' else True


def load_config():
    # type: () -> [Development, Production]
    return Development if is_in_development() else Production
