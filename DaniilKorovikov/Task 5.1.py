with open('data/unsorted_names.txt', 'r') as f:
    with open('data/sorted_names', 'w') as out:
        for line in sorted(f.readlines()):
            print(line.strip(), file=out)
