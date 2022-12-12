import random

from tests.BasicTest import BasicTest


class SackFuckedUpLink(BasicTest):
    def __init__(self, forwarder, input_file):
        super(SackFuckedUpLink, self).__init__(forwarder, input_file, sackMode=True)

    def handle_packet(self):
        random.shuffle(self.forwarder.in_queue)
        for p in self.forwarder.in_queue:
            for i in range(random.randint(0, 2)):
                self.forwarder.out_queue.append(p)

        random.shuffle(self.forwarder.out_queue)
        # empty out the in_queue
        self.forwarder.in_queue = []
