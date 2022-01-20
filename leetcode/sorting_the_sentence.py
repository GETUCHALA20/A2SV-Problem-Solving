class Solution(object):
    def sortSentence(self, s):
        word_list = s.split(" ")
        res = ['']*len(word_list)
        for elem in word_list:
            res[int(elem[-1])-1] = elem[:-1]
        return " ".join(res)