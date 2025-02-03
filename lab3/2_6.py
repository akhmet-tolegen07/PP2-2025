def reverse(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence

print(reverse(input("The sentence: ")))
