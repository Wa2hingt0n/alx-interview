#!/usr/bin/python3
""" Reads 'stdin' line by line and computes metrics """
import sys
import signal


line_count = 0
code_dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
size_list = []
print_list = list(range(10, 10001, 10))


def print_stats(size, codes):
    """ Prints the statistics """
    print("File size: {}".format(sum(size_list)))
    for code in sorted(code_dict.keys()):
        if code_dict[code] > 0:
            print("{}: {}".format(code, code_dict.get(code)))

try:
    for line in sys.stdin:
        line_count += 1
        status_code = int(line.split(" ")[-2])
        file_size = int(line.split(" ")[-1])
        if status_code in code_dict.keys():
            code_dict[status_code] += 1
            size_list.append(file_size)
            for num in print_list:
                if line_count == num:
                    print_stats(size_list, code_dict)
except KeyboardInterrupt:
    print_stats(size_list, code_dict)
