import numpy as np 

def read_glove_vecs(glove_file):
    with open(glove_file, 'r') as f:
        words = set()
        word_to_vec_map = {}
        
        for line in f:
            line = line.strip().split()
            curr_word = line[0]
            words.add(curr_word)
            word_to_vec_map[curr_word] = np.array(line[1:], dtype=np.float64)
            
    return words, word_to_vec_map

def cosine_simi(u,v):
	return (np.dot(u,v)/((np.linalg.norm(u))*(np.linalg.norm(v))))#u and v are the vectors

def word_op(word_a,word_b,word_c):
	maxx=-99#cos sim should be more to be similar
	word_a=word_a.lower()
	word_b=word_b.lower()	
	word_c=word_c.lower()
	for key,value in word_to_vec.items():
		if key == word_a or key==word_b or key==word_c:
			continue
		dist=cosine_simi((word_to_vec[word_c]-word_to_vec[word_a]+word_to_vec[word_b]),word_to_vec[key])
		if dist>maxx:
			maxx=dist
			correct=key
	print(word_a + ":"+ word_b + " so " + word_c + ":" +correct)


words,word_to_vec=read_glove_vecs('glove.6B.50d.txt')
word_op("india","delhi","usa")

			