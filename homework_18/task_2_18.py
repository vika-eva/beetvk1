
class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def __repr__(self):
        return f"name boss: {self.name}, company: {self.company}"

    @property
    def boss_workers(self):
        return self.workers

    @boss_workers.setter
    def boss_workers(self, new_workers):
        if isinstance(new_workers, Worker):
            self.workers.append(new_workers)
        else:
            raise TypeError


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    def __repr__(self):
        return f"name worker - {self.name}, company: {self.company}, id: {self.id}, boss: {self.boss}"

    @property
    def my_boss(self):
        return self.boss

    @my_boss.setter
    def my_boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self.boss = new_boss
        else:
            raise TypeError





if __name__=="__main__":
    w = Boss(8, "eliot", "CE")
    v = Worker(5, "vik", "CE", w)
    n = Worker(7, "iva", "CE", w)
    m = Worker(9, "kaktus", "CE", w)
    f = Worker(3, "kia", "CE", w)

    w.boss_workers = v
    w.boss_workers = n
    #w.boss_workers.append(v)
    #w.boss_workers.append(v)
    print(f"{w.boss_workers}")





