#! /usr/bin/env python3
with open('input.txt', mode='r') as f:
    numbers = map(int, f.readlines())
    numbers = list(map(str, numbers))


def make_IPs(nums):
    if len(nums) > 4:
        ips = [".".join(nums[:4]), ]
        ips = ips + make_IPs(nums[4:])
        return ips
    else:
        return [".".join(nums), ]

with open('output.txt', mode='r+') as f:
    f.write("\n".join(make_IPs(numbers)))
