import numpy
a = numpy.loadtxt('latent_model.txt')
with open('latent_tags.txt') as f:
    b = f.readlines()
print len(a)
print len(b)
