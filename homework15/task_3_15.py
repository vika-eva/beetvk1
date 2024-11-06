
CHANNELS = ["BBC", "Discovery", "TV1000"]
class TVController:

    def __init__(self, channel):
        self.channel = channel
        self.channel_number = 0
        self.number_or_channel = None
        self.N = None

    def __str__(self):
        return str(self.channel)

    def first_channel(self):
        self.channel_number = 0
        return self.channel[self.channel_number]

    def last_channel(self):
        self.channel_number -= 1
        return self.channel[self.channel_number]

    def next_channel(self):
        self.channel_number += 1
        return self.channel[self.channel_number % len(self.channel)]

    def previous_channel(self):
        self.channel_number -= 1
        return self.channel[self.channel_number % len(self.channel)]

    def current_channel(self):
        return self.channel[self.channel_number % len(self.channel)]

    def exists(self, number_or_channel):
        if number_or_channel in self.channel or number_or_channel in range(1, len(self.channel)+1):
            return "yes"
        else:
            return "no"

    def turn_channel(self, N):
        if N in range(1, len(self.channel)+1):
            self.channel_number = N - 1
            return self.channel[self.channel_number]
        else:
            return -1


'''
if __name__ == "__main__":


    CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"
assert controller.last_channel() == "TV1000"
assert controller.turn_channel(1) == "BBC"
assert controller.next_channel() == "Discovery"
assert controller.previous_channel() == "BBC"
assert controller.current_channel() == "BBC"
assert controller.exists(4) == "no"
assert controller.exists("BBC") == "yes"
'''
