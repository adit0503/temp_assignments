def processLine(sentence):
    tokens = sentence.split(' ')

    prevTag = START_STATE
    for token in tokens:
        token = token.split('/')
        word, tag = token[0], token[1]

        WORDS[word] = WORDS.get(word, 0) + 1
        TAGS[tag] = TAGS.get(tag, 0) + 1

        _temp = TRANSITION.get(prevTag, {})
        _temp[tag] = _temp.get(tag, 0) + 1
        TRANSITION[prevTag] = _temp

        prevTag = tag

    _temp = TRANSITION.get(prevTag, {})
    _temp[END_STATE] = _temp.get(END_STATE, 0) + 1
    TRANSITION[prevTag] = _temp


if __name__ == "__main__":
    INPUT = 'Data/en_train_tagged.txt'

    START_STATE = 'START'
    END_STATE = 'END'

    WORDS = {}
    TAGS = {}
    TRANSITION = {}

    with open(INPUT, 'r') as f:
        for _ in range(5):
            processLine(f.readline().strip())

    print(TRANSITION)