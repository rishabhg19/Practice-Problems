class Solution:
    def reverseWords(self, s: str) -> str:
        index = 0
        words = []
        while index < len(s):
            currword = ''
            while index < len(s) and s[index] != " ":
                currword += s[index]
                index += 1
            words.append(currword)
            index += 1
        final_string =""
        cleaned_words = []
        for word in words:
            if word != '':
                cleaned_words.append(word)
        for i in range(len(cleaned_words) - 1, -1, -1):
            if i > 0:
                final_string += cleaned_words[i] + " "
            else:
                final_string += cleaned_words[i]
        return final_string


        