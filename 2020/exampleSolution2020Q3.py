from functools import lru_cache


@lru_cache(maxsize=None)
def count(remaining_characters, last_char, last_char_count, max_char_count, letters):
    if last_char_count is not None and last_char_count > max_char_count:
        # impossible
        return 0
    elif remaining_characters == 0:
        return 1
    else:
        total = 0

        for i in range(letters):
            if last_char is not None and last_char == i:
                total += count(
                    remaining_characters - 1,
                    last_char,
                    last_char_count + 1,
                    max_char_count,
                    letters,
                )
            else:
                total += count(remaining_characters - 1, i, 1, max_char_count, letters)

        return total


def print_letters(l):
    return "".join(chr(i + ord("A")) for i in l)


letters, max_adjacent, expected_length = tuple(int(x) for x in input().split(" "))

n = int(input()) 
prefix = []
last = None
last_count = 0

while len(prefix) < expected_length:

    for i in range(letters):
        this_last_count = last_count + 1 if i == last else 1
        prefix.append(i)
        with_prefix = count(
            expected_length - len(prefix), i, this_last_count, max_adjacent, letters
        )

        # print("%s - %d" % (print_letters(prefix), with_prefix))

        if with_prefix >= n:
            # this is the right prefix
            last = i
            last_count = this_last_count
            break

        n -= with_prefix
        prefix.pop()

print(print_letters(prefix))