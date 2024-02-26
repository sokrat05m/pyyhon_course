def spin_words(sentence):
    sentence = sentence.split()
    for i in range(len(sentence)):
        if len(sentence[i]) > 4:
            sentence[i] = sentence[i][::-1]
    sentence = ' '.join(sentence)
    return sentence