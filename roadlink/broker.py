from django_q.brokers import Broker


class RoadLinkBroker(Broker):
    def info(self):
        return 'Road Link Broker'
