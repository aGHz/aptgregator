from web.core import Controller

from aptgregator.util.response import *

log = __import__('logging').getLogger(__name__)


class RootController(Controller):
    def __default__(self, *args, **kwargs):
        return TEMPLATE('index', {})

