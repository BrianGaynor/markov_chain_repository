# for tying he flow of the application together

from markov_python.cc_markov import MarkovChain

for i in range (1,12):
  if i % 2 == 0:
    print i ** 2
	
mc = MarkovChain()