import logging

import wingdbstub

LOGGER = logging.getLogger(__file__)

class Company(object):
    def __init__(self, revenue, costs):
        self.revenue = revenue
        self.costs = costs

    @property
    def profit(self):
        return self.revenue - self.costs

