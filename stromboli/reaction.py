from numpy.random import uniform as uni
from math import log
from heapq import heappush

class Reaction(object):
    """Reaction object to hold exactly one reaction with an arbitrary number of
    participant and product species.
    """

    def __init__(self, participants, products, rate):
        """Initialize a reaction object. participants and products are lists of tuples
        (m, species) and (n, species), where m and n correspond to the number of the
        chemical species on the left hand and right hand side of the reaction equation,
        respectively."""

        self.participants = participants
        self.products = products

        # Calculate the change in each species and store
        self._to_update = {}
        for m,s in participants:
            self._to_update[s] = -m
        for m,s in products:
            if s in self._to_update:
                self._to_update[s] += m
            else:
                self._to_update[s] = m

        # Register the reaction with the species
        for s in self._to_update:
            s._register_reaction(self)

        self.rate = rate

        # Initialize the queue variables
        self._queue_ref = None
        self._queue_entry = [-1, self]

    def _set_queue_ref(self, queue, time):
        # Set reference to the priority queue
        self._queue_ref = queue
        self._update_next_time(time)

    def _invalidate_queue_entry(self):
        # Invalidate previous queue entry
        self._queue_entry[1] = None

    def _update_queue(self):
        # Update queue
        self._queue_entry = [self.next_time, self]
        heappush(self._queue_ref, self._queue_entry)        

    def _update_next_time(self, time):
        # Invalidate the current entry
        self._invalidate_queue_entry()

        # Calculate the reaction propensity
        p = self.rate
        for m,s in self.participants:
            N = s.number
            for n in range(m):
                p *= N-n

        # Update the queue with the next reaction time only if the reaction
        # actually occurs
        if p>0.:
            self.next_time = time - log(uni())/p
            self._update_queue()

    def _react(self, time):
        # Update species numbers
        # Gather affected reactions and invalidate their next_time's
        reactions = set()
        for s,m in self._to_update.iteritems():
            if (m!=0):
                s._change(m)
                reactions.update(s._get_dependent_reactions())

        # Update the affected reactions next_time and update the priority queue
        for r in reactions:
            r._update_next_time(time)

    def __str__(self):
        return str(self.participants) + "-- " + self.rate + " --> " + str(self.products)
