# Write a program that can perform a letter frequency attack on an additive cipher without human intervention.Your software should produce possible plain text in rough order of likelihood .it would be good if your user interface allow user to specify 'Give me top 10 possible plain  texts '.  
import operator
Text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
def get_key(iteration: int, ch: str) -> int:
    return ord(ch) - ord(Text[iteration])


def decryption(message, key):
    decode = ""
    for ch in message:
        if ch.isspace():
            decode += " "
        else:
            decode += chr(((ord(ch) - ord('A') - key) % 26) + ord('A'))
    return decode


def freqattack(message: str) -> str:
    frequency = {}
    for ch in message:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    sorted_x = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(10):
        if i == len(sorted_x):
            break
        key = get_key(i, sorted_x[i][0])
        print(decryption(message, key))

    


def menu():
    words = 'A GFNZMO NFVVYTO'
    print("\nFirst 10 possible plain texts are : ")
    freqattack(words)
menu()
