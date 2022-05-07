
def most_common_words(filepath, number_of_words=3):
    with open(filepath, 'r') as text:
        words_number = {}
        for word in text.read().split():
            words_number[word.strip(',.!:;').lower()] = words_number.get(word.strip(',.!:;').lower(), 0) + 1
        return sorted(words_number, reverse=True, key=words_number.get)[:number_of_words]

print(most_common_words('data/lorem_ipsum.txt'))