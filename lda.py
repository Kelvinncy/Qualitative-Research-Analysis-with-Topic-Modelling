from gensim import corpora
from gensim.models.ldamodel import LdaModel

def ldaPreprocess (docs):
    # Create Dictionary
    id2word = corpora.Dictionary(docs)

    # id2word.filter_extremes(no_below=0.1*len(docs), no_above=0.8)

    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in docs]

    return corpus, id2word

def computeLDA (corpus, dictionary, k, a, b, passes):
    ldamodel = LdaModel(corpus=corpus,
                        id2word=dictionary,
                        num_topics=k, 
                        random_state=100,
                        passes=passes,
                        alpha=a,
                        eta=b)
    
    return ldamodel