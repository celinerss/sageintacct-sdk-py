"""
Sage Intacct purchasing
"""
from typing import Dict

from .api_base import ApiBase


class Purchasing(ApiBase):
    """Class for Purchasing APIs."""
    def __init__(self):
        ApiBase.__init__(self, dimension='PODOCUMENT', post_legacy_method='create_potransaction')
