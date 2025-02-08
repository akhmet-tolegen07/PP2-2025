def reverse(sentence):
    words = sentence.split()
    reversed_sentence = []
    for i in range(len(words) - 1, -1, -1):
        reversed_sentence.append(words[i])
    return " ".join(reversed_sentence)

print(reverse(input("The sentence: ")))
