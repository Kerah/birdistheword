#!/usr/bin/env python
import string
import sys
import functools

_ignore = set(string.punctuation)


def process(data):
    """
    proccessing data string and counting words in text

    :param data: string with text for analyze
    :return: dict with words
    """
    result = {}
    for el in data.split():
        el = el.strip().lower().rstrip(string.punctuation)
        if not el or el in _ignore:
            continue
        if el in result:
            result[el] += 1
        else:
            result[el] = 1
    return result


def compare(x, y):
    """

    :param x: tuple with word and count
    :param y: tuple with word and count
    :return:
    """
    if x[1] > y[1]:
        return -1
    if x[1] < y[1]:
        return 1
    if x[0] < y[0]:
        return -1
    if x[0] > y[0]:
        return 1
    return 0


def order(result):
    """
    transform dict with words and counts to ordered list
    :param result: map with counted words
    :return: list with pairs (word, count)
    """
    result = [(el, result[el]) for el in result]
    result.sort(key=functools.cmp_to_key(compare))
    return result


def out(result):
    """
    output result

    :param result: list with  pairs (word, count)
    """
    for el in result:
        print(u'{}: {}'.format(*el))


def main(file_path):
    with open(file_path) as f:
        result = process(f.read())
        result = order(result)
        out(result)


def cli_args():
    """
    process command line arguments and get file path
    :return: path to file
    """
    args = sys.argv[1:]
    if len(args) != 1:
        usage = u'''birdistheword analyze text for statistics of word occurrences.
        
             usage: birdistheword.py /path/to/text/file/with/words.txt
        '''
        print(usage)
        sys.exit(1)
    return args[0]


if __name__ == "__main__":
    fp = cli_args()
    main(fp)
