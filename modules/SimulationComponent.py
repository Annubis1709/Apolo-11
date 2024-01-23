import random


class SimulationComponent:
    def __init__(self, component_type):
        self.component_type = component_type
        self.statuses = ['excellent', 'good', 'warning', 'faulty', 'killed', 'unknown']

    def generate_status(self):
        return random.choice(self.statuses)
