import collections
import multiprocessing
import datetime

Scientist = collections.namedtuple('Scientist', [
    'name',
    'born',
])

scientists = (
    Scientist(name='Ada Lovelace', born=1815),
    Scientist(name='Emmy Noether', born=1882),
    Scientist(name='Marie Curie', born=1867),
    Scientist(name='Tu Youyou', born=1930),
    Scientist(name='Ada Yonath', born=1939),
    Scientist(name='Vera Rubin', born=1928),
    Scientist(name='Sally Ride', born=1951),
)


def process_item(item):
    print('Process {} Waiting {} seconds'.format(item.name, datetime.datetime.now()))
    return {
        'name': item.name,
        'age': 2019 - item.born
    }


def handler():
    pool = multiprocessing.Pool()
    result = pool.map(process_item, scientists)
    print(tuple(result))


if __name__ == '__main__':
    handler()
