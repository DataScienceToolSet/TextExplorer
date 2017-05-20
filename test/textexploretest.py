import unittest
from lib.textexplore import TextExplorer


class TestTextExploreMethods(unittest.TestCase):

    def test_commonwordList(self):
        wordlist=[]
        wordlist.append("Hi what's up")
        wordlist.append("Hi there are news")
        wordlist.append("Hi what do you want to do")
        wordlist.append("Hi what do you want to do")
        nro_class=2
        class_size=2
        te=TextExplorer()
        arr=te.getComonWordList(wordlist, nro_class, class_size)
        assert arr == sorted(["Hi"]), "The list is not correct"

if __name__ == '__main__':
    unittest.main()
