
#Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. 
#For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). 
#We'll call such a concatenation, the transformation of a word.

#Return the number of different transformations among all words we have.

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        if len(words) == 0:
            return 0
        vlist = []
        olist = []
        maps = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for x in words:
            estring = ""
            for y in x:
                estring += (maps[ord(y) - 97])
            olist.append(estring)
        for x in olist:
            if x in vlist:
                continue
            else:
                vlist.append(x)
        return len(vlist)
                