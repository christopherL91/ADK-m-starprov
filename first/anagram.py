#!/usr/bin/env python3

from collections import defaultdict

primes = {
	'a': 2,'b': 3,'c': 5,'d': 7,'e': 11,'f': 13,'g': 17, 'h':19,'i':23,
	'j':29,'k':31,'l':37,'m':41,'n':43,'o':47,'p':53,'q':59,'r':61,'s':71,
	't':73,'u':79,'v':83,'w':89,'x':97,'y':101,'z':103,'å':107,'ä':109,'ö':113,
	'é': 127
}

#	Cost: O(max(m,n))
def setup(wordfile):
	wordlist = defaultdict(list)
	f = open(wordfile)
	for word in f:
		res = 1
		for ch in word.rstrip():
			if ch not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','å','ä','ö']:
				continue
			res *= primes[ch.lower()]
		wordlist[res].append(word.rstrip())
	return wordlist

	# Runs in O(n*log(n))
if __name__ == '__main__':
wordlist = setup('new.txt')
	data = [
		'logaritm','algoritm','dator','komplexitet','ordat','sloka',
		'solka','kolas','loska','lycke'
	]
	result = defaultdict(set)
	for word in data: #	O(n)
		res = 1
		for ch in word: # O(m)
			res *= primes[ch.lower()]
		old = result[res]
		result[res] = (set([word] + wordlist[res] + list(old))) #	O(log(n))
	for val in result.items(): # O(n)
		print(sorted(val[1]))	#	We can assume we have access to a sorted set.
