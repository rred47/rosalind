from collections import Counter

seq = open('input/rosalind_ini.txt', 'r').read()

out = Counter(seq)
print("%d %d %d %d" % (out['A'], out['C'], out['G'], out['T']))