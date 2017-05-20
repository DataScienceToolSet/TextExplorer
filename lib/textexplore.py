import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


class TextExplorer():
    def generatewordcloud(self, text, filename):
        """
        :param text: text for to get the wordcloud 
        :param filename: imagen file name
        :return: save a image woth the wordcloud of the text
        """
        wordcloud = WordCloud(relative_scaling=1.0,
                              stopwords=STOPWORDS
                              ).generate(text)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.savefig(filename + '.png')
        pass

    def getwordsmostused(self, wordlist):
        """
        :param wordlist: original word list of the corpus
        :return: list  of all words sorted by frecuency
        """
        dict = {}
        for l in wordlist:
            wordl = l.split(" ")
            for word in wordl:
                if word not in dict.keys():
                    dict[word] = 1
                else:
                    dict[word] += 1

        sortedlist = sorted(dict, key=dict.get, reverse=True)
        return sortedlist

    def getcommonwordlist(self, wordlist, nro_class, class_size):
        """
        :param wordlist: the list of all documents 
        :param nro_class: the number of clases in the corpus
        :param class_size: The size of the each class 
        :return: a sorted list with all common word between all classes
        """
        dict = {}
        for l in wordlist:
            wordl = l.split(" ")
            for word in wordl:
                if word not in dict.keys():
                    dict[word] = [0] * nro_class

        for i in xrange(nro_class):
            ini = i * class_size
            for j in xrange(ini, ini + class_size):
                t = wordlist[j]
                wordl = t.split(" ")
                for word in wordl:
                    if word in dict.keys():
                        dict[word][i] = 1
        anslist = []
        for w in dict.keys():
            arr = dict[w]
            flag = True
            for e in arr:
                if e == 0:
                    flag = False
                    break
            if flag:
                anslist.append(w)

        anslist = sorted(anslist)
        return anslist
