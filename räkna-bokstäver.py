import sys

def __main__():
    text_file = sys.argv[1]

    total = dict()
    total_count = 0

    with open(text_file) as text:
        for line in text:
            for c in line:
                if c.isalpha():
                    total_count = total_count + 1
                    result = total.get(c)
                    if result == None:
                        total[c] = 1
                    else:
                        total[c] = result + 1

    sorted_total = dict(sorted(total.items(), key=lambda item: item[1]))

    for thing in sorted_total.items().__reversed__():
        percent = (thing[1] / total_count) * 100
        print(thing[0], ":", thing[1], "-", percent, "%")

__main__()
