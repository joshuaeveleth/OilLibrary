import os
from pkg_resources import get_distribution

from sqlalchemy import create_engine
from sqlalchemy.exc import UnboundExecutionError

from .models import DBSession

import sample_oils

try:
    __version__ = get_distribution('oil_library').version
except:
    __version__ = 'not_found'

'''
currently, the DB is created and located when package is installed
'''
_oillib_path = os.path.dirname(__file__)
_db_file = os.path.join(_oillib_path, 'OilLib.db')


def _get_db_session():
    'we can call this from scripts to access valid DBSession'
    # not sure we want to do it this way - but let's use for now
    session = DBSession()

    try:
        session.get_bind()
    except UnboundExecutionError:
        session.bind = create_engine('sqlite:///' + _db_file)

    return session

_sample_oils = {}

from .factory import get_oil, get_oil_props

_sample_oils.update({k: get_oil(v, max_cuts=2)
                     for k, v in sample_oils._sample_oils.iteritems()})