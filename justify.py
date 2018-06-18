def justify(words, width):
    """Divide words (an iterable of strings) into lines of the given
    width, and generate them. The lines are fully justified, except
    for the last line, and lines with a single word, which are
    left-justified.

    >>> words = "This is an example of text justification.".split()
    >>> list(justify(words, 16))
    ['This    is    an', 'example  of text', 'justification.  ']

    """
    line = []             # List of words in current line.
    col = 0               # Starting column of next word added to line.
    for word in words:
        if line and col + len(word) > width:
            if len(line) == 1:
                yield left_justify(line, width)
            else:
                # After n + 1 spaces are placed between each pair of
                # words, there are r spaces left over; these result in
                # wider spaces at the left.
                n, r = divmod(width - col + 1, len(line) - 1)
                narrow = ' ' * (n + 1)
                if r == 0:
                    yield narrow.join(line)
                else:
                    wide = ' ' * (n + 2)
                    yield wide.join(line[:r] + [narrow.join(line[r:])])
            line, col = [], 0
        line.append(word)
        col += len(word) + 1
    if line:
        yield left_justify(line, width)
