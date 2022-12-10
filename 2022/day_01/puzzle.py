"""."""

if __name__ == '__main__':

    input = []
    with open('input.txt', 'r') as f:
        for line in f:
            input.append(line.rstrip())

    results = []
    local_sum = 0
    for entry in input:
        if entry != '':
            local_sum += int(entry)
        else:
            results.append(local_sum)
            local_sum = 0

    results.sort()
    results.reverse()
    print('The 3 elves carrying more calories carry ' +
         f'{results[0]}, {results[1]}, and {results[2]}' +
         f' respectively, which yields a total of {sum(results[:3])}')
