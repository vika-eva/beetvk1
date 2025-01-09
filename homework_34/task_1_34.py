from threading import Thread


class Counter(Thread):

    counter = 0
    rounds = 1000000

    def run(self):
        for i in range(self.rounds):
            Counter.counter += 1

t = Counter()
t1 = Counter()
t.start()
t1.start()
t.join()
t1.join()
#t,t1.join()

print(Counter.counter)