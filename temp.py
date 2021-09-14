def camelSplitter(label):
    upper_idx = []
    s = ''
    for i in range(len(label)):
        if label[i].isupper():
            upper_idx.append(i)

    for i in range(len(label)):
        if i in upper_idx:
            s += ' '

        s += label[i]

    return s.title()
