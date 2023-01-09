import random
import pprint
import tqdm

d = {}
for _ in tqdm.tqdm(range(20)):
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0,
         1, 1, 1, 1, 1, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 2, 2, 2]

    random.shuffle(a)
    a9 = a[:9]
    c = tuple(sorted((a9.count(0), a9.count(1), a9.count(2)), reverse=True))

    d[c] = d.get(c, 0)+1

pprint.pprint(d)
