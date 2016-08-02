"""J&M exercise 4.1 and 4.6, p. 155."""
import string

filename = "data/books.txt"

with open(filename) as f:
    lines = f.readlines()
    corpus = ""
    for line in lines:
        line = line.strip().lower()
        line = ''.join([c for c in line if c not in set(string.punctuation)])
        if len(line) != 0:
            corpus += line + " "

# Unigrams
unigram = dict()
for c in corpus:
    unigram[c] = 1 if c not in unigram else unigram[c] + 1

# Bigrams
firstchars = corpus[:-2]
secondchars = corpus[1:]
bigram_list = [x[0] + x[1] for x in zip(firstchars, secondchars)]
bigram = dict()
for b in bigram_list:
    bigram[b] = 1 if b not in bigram else bigram[b] + 1

# Good-Turing discounting
bigram_counts = dict()
for key in bigram:
    count = bigram[key]
    bigram_counts[count] = 1 if count not in bigram_counts else bigram_counts[count] + 1
print(bigram_counts)

for k in range(0, 150):
    if k not in bigram_counts:
        bigram_counts[k] = 0
    if k+1 not in bigram_counts:
        bigram_counts[k+1] = 0

    if k == 0:
        print("Prob(%d) = %.5f" % (k, bigram_counts[1] / len(bigram_list)))
    elif bigram_counts[k] == 0:
        print("Prob(%d) unreliable" % k)
    else:
        gt_estimate = float(k+1) * bigram_counts[k+1] / bigram_counts[k]
        print("Prob(%d) = %.5f" % (k, gt_estimate))