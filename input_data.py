import numpy

from collections import deque

class InputData:

    def __init__(self, file_name, min_count):
        self.input_file_name = file_name
        
        # loads the data from file and removes low count words and shit
        self.get_words(min_count)

        # not sure what this is for yet
        self.word_pair_catch = deque()
        
        # creates self.sample_table
        # - numpy array with certain probability distribution based on frequency of the word
        self.init_sample_table()

        print('Word count: %d' % len(self.word2id))
        print('Sentence Length: %d' % (self.sentence_length))

    def get_words(self, min_count):
        self.input_file = open(self.input_file_name)
        
        # length of the whole dataset (number of words)
        self.sentence_length = 0

        # number of sentences in the dataset
        self.sentence_count = 0
        
        # dictionary of all unique words and their counts 
        word_frequency = dict()

        for line in self.input_file:

            self.sentence_count += 1
            line = line.strip().split(' ')
            self.sentence_length += len(line)

            for w in line:
                # if word is already in the dict add one to it
                # otherwise declare it and set it to 1
                try:
                    word_frequency[w] += 1
                except:
                    word_frequency[w] = 1
        
        # word to id dictionary
        self.word2id = dict()

        # id to word dictionary
        self.id2word = dict()
        

        wid = 0;

        # word_frequency without low count words
        # id to count dictionary
        self.word_frequency = dict()

        # iterates over dict of all unique words and their counts
        # w - word
        # c - count of the word
        for w, c in word_frequency.items():
            # if the word count is smaller than min_count
            # substracts the word_count form self.sentence_length
            # ??? honestly not sure what this does
            if c < min_count:
                self.sentence_length -= c
                continue
            
            # adds the word to the dictionaries
            self.word2id[w] = wid
            self.id2word[wid] = w
            
            self.word_frequency[wid] = c
            wid += 1
        
        # number of words in the vocabulary (unique words)
        self.word_count = len(self.word2id)

    def init_sample_table(self):
        self.sample_table = []
        sample_table_size = 1e8
        
        # puts all the values of word_frequency into numpy array
        # and makes them to the power of 0.75
        # small numbers get deacresed a bit
        # big numbers get deacreased a lot
        pow_frequency = numpy.array(list(self.word_frequency.values()))**0.75

        words_pow = sum(pow_frequency)

        # relative frequency (in % i think)
        ratio = pow_frequency / words_pow
        
        # multiplies all ratios by a big number and rounds them to a closest integer
        count = numpy.round(ratio * sample_table_size)
        
        # wid - id of word
        # c - its 'count' (ratio multiplied by 1e8)
        for wid, c in enumerate(count):
            self.sample_table += [wid] * int(c)

        self.sample_table = numpy.array(self.sample_table)

    def get_batch_pairs(self, batch_size, window_size):

        # until word_pair_catch is smaller than batch_size keep
        # appending pairs of words to word_pair_catch
        # one sentence at the time
        while len(self.word_pair_catch) < batch_size:
            sentence = self.input_file.readline()
            # kinda useless but w/e
            if sentence is None or sentence == '':
                self.input_file = open(self.input_file_name)
                sentence = self.input_file.readline()
            
            # sentence as a list of ids
            word_ids = []
            for word in sentence.strip().split(' '):
                try:
                    word_ids.append(self.word2id[word])
                except:
                    continue
            

            # for every word create pairs with adjacent words 
            for i, u in enumerate(word_ids):
                # word_ids[i - window_size: i + window_size])
                for j, v in enumerate(word_ids[max(i - window_size, 0): i + window_size]):
                    assert u < self.word_count
                    assert v < self.word_count
                    # don't want pairs of the same words
                    if i == j:
                        continue
                    self.word_pair_catch.append((u, v))

        batch_pairs = []
        for _ in range(batch_size):
            # pulls batch_size number of word_pairs to batch_pairs
            batch_pairs.append(self.word_pair_catch.popleft())

        return batch_pairs

    def get_neg_v_neg_sampling(self, pos_word_pair, count):
        neg_v = numpy.random.choice(self.sample_table, size=(len(pos_word_pair), count)).tolist()
        return neg_v
    
    # number of pairs in one epoch
    def evaluate_pair_count(self, window_size):
        return self.sentence_length * (2 * window_size - 1) - (self.sentence_count - 1) * (1 + window_size) * window_size

def test():
    a = InputData('./tweets.txt', 2)

if __name__ == '__main__':
    test()
