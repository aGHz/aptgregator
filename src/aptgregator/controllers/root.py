from web.core import Controller

from aptgregator.scrapers.kijiji import listings as kijiji_listings
from aptgregator.util.response import *

log = __import__('logging').getLogger(__name__)


class RootController(Controller):
    def __default__(self, *args, **kwargs):
        # Kijiji
        area = "ville-de-montreal"
        price_from = 600
        price_to = 900
        kijiji_url = "http://www.kijiji.ca/b-appartement-condo/{area}/c37l1700281?price={from_}.00__{to}.00".format(
            from_=price_from,
            to=price_to,
            area=area)
        kijiji = kijiji_listings(kijiji_url)

        return TEMPLATE('listings', {'kijiji': kijiji})

