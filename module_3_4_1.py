def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    print(root_word)   # контроль
    for i in other_words:
        print(i)  # контроль
        other_words = list(other_words)
        #print(type(other_words))
        other_words = other_words.lower()

        if root_word in other_words:
            same_words.append(i)
            print(same_words)
    return same_words
    print(same_words)


single_root_words("Disablement", "Disablement", 'Able', 'Mable', 'Disable', 'Bagel')

