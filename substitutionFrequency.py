"""
Program shows the frequency of the characters in the english language using a substitution cipher
"""
import random
import string


class SubstitutionCipher:

    def __init__(self):

        self.alphabet = list(string.ascii_lowercase)
        self.key = []
        self.ecryptedText = ""
        self.letterFrequencies = []

        self.createKey()

        for x in range(26):
            self.letterFrequencies.append(
                [string.ascii_lowercase[x], self.key[x][1], 0, 0])

        """
        reading in text from file
        """
        # open text file in read mode
        text_file = open("plainText.txt", "r")

        # read whole file to a string
        data = text_file.read()

        # close file
        text_file.close()

        self.textToEncrypt = data.lower()

    # creates a key from scrambled alphabet
    def createKey(self):

        # new list with random key order
        scrambledList = self.alphabet.copy()
        random.shuffle(scrambledList)

        # matching key with
        for x in range(26):
            self.key.append([self.alphabet[x], scrambledList[x]])

    # encrypting the text from file
    def encryptingText(self):

        # looping through every character in text
        for character in self.textToEncrypt:

            # finding letter from key
            for x in range(26):
                if character == self.key[x][0]:

                    # adding to encrypted stirng
                    self.ecryptedText += self.key[x][1]
                    continue

                # adding spaces to the encrypted text
                elif character == ' ':
                    self.ecryptedText += ' '
                    break

    def getCharFrequencies(self):

        totalChars = 0

        # iterating through every char in text
        for character in self.ecryptedText:

            for x in range(26):

                # totalling letter numbers
                if character == self.letterFrequencies[x][1]:
                    self.letterFrequencies[x][2] += 1
                    totalChars += 1

        for x in range(26):
            # working out percentages
            self.letterFrequencies[x][3] = round(
                ((self.letterFrequencies[x][2]/totalChars)*100), 2)


testCipher = SubstitutionCipher()
testCipher.encryptingText()
testCipher.getCharFrequencies()

for x in range(26):
    print(testCipher.letterFrequencies[x], end=' ')
    print("%")
