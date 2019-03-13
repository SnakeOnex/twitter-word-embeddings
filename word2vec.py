from input_data import InputData
from model import SkipGramModel
import numpy
import torch

from tqdm import tqdm
import sys

class Word2Vec:
    def __init__(self,
            input_file_name,
            output_file_name,
            emb_dimension=100,
            batch_size=50,
            window_size = 5,
            iteration=5,
            initial_lr=0.025,
            min_count=5):

        self.data = InputData(input_file_name, min_count)
        self.output_file_name = output_file_name

        # number of unique words
        self.emb_size = len(self.data.word2id)

        self.emb_dimension = emb_dimension
        self.batch_size = batch_size
        self.window_size = window_size
        self.iteration = iteration
        self.initial_lr = initial_lr

        self.device = torch.device('cpu')
        self.skip_gram_model = SkipGramModel(self.emb_size, self.emb_dimension)
        self.use_cuda = torch.cuda.is_available()
        if self.use_cuda:
            self.skip_gram_model.cuda()
            self.device = torch.device('cuda')
        
        # pytorch way of getting an optimizer
        self.optimizer = torch.optim.SGD(self.skip_gram_model.parameters(), lr=self.initial_lr)

    def train(self):
        # number of pairs in one epoch
        pair_count = self.data.evaluate_pair_count(self.window_size)
            
        # number of batches in one epoch
        batch_count = self.iteration * pair_count / self.batch_size

        process_bar = tqdm(range(int(batch_count)))

        for i in process_bar:
            # batch of word pairs
            pos_pairs = self.data.get_batch_pairs(self.batch_size, self.window_size)
            
            # vector of pairs that will get updated negatively
            # maybe its not pairs but words
            neg_v = self.data.get_neg_v_neg_sampling(pos_pairs, 5)

            # vector of center words
            pos_u = [pair[0] for pair in pos_pairs]

            # vector of context words
            pos_v = [pair[1] for pair in pos_pairs]

            pos_u = torch.LongTensor(pos_u, device=self.device)
            pos_v = torch.LongTensor(pos_v, device=self.device)
            neg_v = torch.LongTensor(neg_v, device=self.device)

            self.optimizer.zero_grad()
            loss = self.skip_gram_model.forward(pos_u, pos_v, neg_v)
            loss.backward()
            self.optimizer.step()

            process_bar.set_description("Loss: %0.8f, lr: %0.6f" % 
                    (loss.item(), self.optimizer.param_groups[0]['lr']))

            if i * self.batch_size % 1e5 == 0:
                lr = self.initial_lr * (1.0 - 1.0 * i / batch_count)
                for param_group in self.optimizer.param_groups:
                    param_group['lr'] = lr
        self.skip_gram_model.save_embedding(self.data.id2word, self.output_file_name)


if __name__ == '__main__':
    w2v = Word2Vec(input_file_name=sys.argv[1], output_file_name=sys.argv[2])
    w2v.train()
