from heapq import *

class Algorithm(object):
    """Algorithm object that holds all the reactions in the system."""
    def __init__(self, reactions):
        """Initialize a new algorithm object. Expects a list of Reactions."""
        self.time = 0.

        # Initialize priority queue
        self._queue = []
        # Initialize reactions
        for r in reactions:
            r._set_queue_ref(self._queue, self.time)

    def step(self):
        """Execute the next reaction in the list"""
        r = None
        # Loop over invalidated priority queue entries
        while r==None:
            try:
                self.time, r = heappop(self._queue)
            except IndexError:
                raise RuntimeError("No possible reactions!")

        # Execute reaction
        r._react(self.time)
        return self.time
