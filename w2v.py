import sys
sys.path.insert(0, './head')
import word2vec
from scipy import spatial
import numpy
import json
import re

def getWords(data):
    return re.compile(r"[\w']+").findall(data)
def save_latent_features_of_tagsjson():
    model = word2vec.load('../lib/word2vec/vectors.bin')
    all_tags = []
    with open('tags.json', 'r') as f:
         data = json.load(f)

    i=0
    while i < len(data['item']):
        all_tags = all_tags + data['item'][i]['tag_text'].replace('"','').lower().split('|')
        all_tags = all_tags + data['item'][i]['tag_query'].replace('"','').lower().split('|')
        i=i+1
    print all_tags
    latent_tags=[]
    latent_model=[]
    for i in all_tags:
        try:
            a=model[str(i)]
            latent_tags.append(str(i))
            latent_model.append(a)
        except Exception, e:
            print i
            print e
    obj = open('latent_tags.txt', 'w')
    for i in latent_tags:
        obj.write(i + '\n')
    obj.close
    numpy.savetxt('latent_model.txt', latent_model)
#save_latent_features_of_tagsjson()

def matcher(line, context):
    model = word2vec.load('./latents.bin')
    #clusters = word2vec.load_clusters('../lib/word2vec/text8-clusters.txt')
    a = numpy.loadtxt('latent_model.txt')
    with open('latent_tags.txt') as f:
        b = f.readlines()

    #print clusters['dog']
    #indexes, metrics = model.cosine(a)
    #print model.vocab[indexes]
    #a=model[a]

    words = line
    for i in words:
        try:
            i2 = model[i]
            for j in range(len(a)):
                result = 1 - spatial.distance.cosine(i2, a[j])
                #print result
                if result > 0.75:
                    #print i, b[j][:-1]
                    return b[j][:-1]
        except Exception, e:
            k=0
    return 'jankiap50'
#matcher(str(sys.argv[1]), 0)
