from __future__ import division  # Python 2 users only
import random

class Markov:
    def __init__(self, filename, chain_length):
        self.data = {}
        self.STOPWORD = 'STOP'
        self.filename = filename
        self.chain_length = chain_length

    def make_chain(self):
        f = open(self.filename)
        ret = {}
        for line in f:
            words = line.split()
            if len(words) > self.chain_length:
                words.append(self.STOPWORD)
            for i in range(len(words) - self.chain_length):
                if tuple(words[i:i + self.chain_length]) not in ret:
                    ret[tuple(words[i:i + self.chain_length])] = [words[i+self.chain_length]]
                else:
                    ret[(tuple)(words[i:i + self.chain_length])].append(words[i+self.chain_length])
        self.data = ret

    def genText(self):
        out = []
        seed = random.randint(0, len(self.data)-2)
        seed_word, next_word = self.data.keys()[seed]
        word = str(self.data[(seed_word, next_word)][random.randint(0, len(self.data[(seed_word, next_word)])-1)])
        out.append(seed_word)
        out.append(next_word)
        out.append(word)
        counter = 0
        while word != "STOP":
            keys = [item for item in list(self.data.keys()) if word in (item)]
            random_key = keys[random.randint(0, len(keys)-1)]
            # print str(random_key) + '\t' + str(self.data[random_key])
            if(random_key[0] == word):
                out.append(random_key[1])
            words = self.data[random_key]
            word = words[random.randint(0,len(words)-1)]
            out.append(word)
            counter += 1
        print ' '.join(out[:len(out)-2])

if __name__ == '__main__':
    markov = Markov('gselevator_tweets.txt', 2)
    markov.make_chain()
    # for line in markov.data:
    #     if(len(markov.data[line])) > 1:
    #         print str(line) + '\t' + str(markov.data[line])
    markov.genText()