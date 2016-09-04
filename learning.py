import sys
sys.path.insert(0, './head')
import numpy
from scipy import spatial
import word2vec
a = numpy.loadtxt('latent_model.txt')
with open('latent_tags.txt') as f:
    b = f.readlines()
print len(a)
print len(b)
def matcher(line, context):
    model = word2vec.load('../lib/word2vec/vectors.bin')
    #clusters = word2vec.load_clusters('../lib/word2vec/text8-clusters.txt')
    a = numpy.loadtxt('latent_model.txt')
    with open('latent_tags.txt') as f:
        b = f.readlines()


    a = model['love']
    print a
    b = model['hate']
    print b
    result = 1 - spatial.distance.cosine(a, b)
    print result
    return 'jankiap50'
matcher('a', 0)
