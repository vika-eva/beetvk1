def with_index(iterable, start = 0):
    number = start
    object_ = iter(iterable)
    while True:
        try:
            yield number, next(object_)
            number += 1
            #print(index, next(object_))
        except StopIteration:
            break


for i in with_index(["jkhv,j", "ujg,"]):
    print(i)
