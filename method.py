def get_words(word, model):
    words = model.wv.most_similar(positive=word, topn=15)
    return words
