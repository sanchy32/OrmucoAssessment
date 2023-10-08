'''Created 2023-10-16
@author: Godswill Agbofode'''
import re


def version_compare(version1, version2):
    v1 = version1.split(".")
    v2 = version2.split(".")
    v1len = len(v1)
    v2len = len(v1)
    tlen = max(v1len, v2len)
    for i in range(tlen):
        if i < v1len: n1 = int(v1[i])
        else: n1 = 0

        if i < v2len: n2 = int(v2[i])
        else: n2 = 0

        if n1 > n2:
            return 1
        elif n2 > n1:
            return -1

    return 0


def version_compare2(version1, version2):
    v1_str = re.split(r"[\b\W\b]+|_", version1)
    v2_str = re.split(r"[\b\W\b]+|_", version2)
    v1len = len(v1_str)
    v2len = len(v2_str)
    tlen = max(v1len, v2len)
    v1 = [0]*(tlen)
    v2 = [0]*(tlen)

    for i in range(tlen):
        if i<v1len:
            if v1_str[i].isdigit():
                v1[i] = int(v1_str[i])
            else: v1[i] = v1_str[i]
        else: v1[i] = 0

        if i < v2len:
            if v2_str[i].isdigit():
                v2[i] = int(v2_str[i])
            else:
                v2[i] = v2_str[i]
        else: v2[i] = 0

        if isinstance(v1[i], int) and isinstance(v2[i], int):
            if v1[i] > v2[i]: return 1
            elif v1[i] < v2[i]: return -1

        elif isinstance(v1[i], int) and not isinstance(v2[i], int):
            return -1
        elif not isinstance(v1[i], int) and isinstance(v2[i], int):
            return 1
        elif not isinstance(v1[i], int) and not isinstance(v2[i], int):
            if v1[i] > v2[i]: return 1
            elif v1[i] < v2[i]: return -1
            elif v1[i] == v2[i]:
                if not len(v1[i]) - len(v2[i]) == 0:
                    return len(v1[i])-len(v2[i])

    return 0


