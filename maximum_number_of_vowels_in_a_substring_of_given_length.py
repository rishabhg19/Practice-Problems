class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        window = deque(s[:k])
        def count_vowels(window):
            count = 0
            for char in window:
                if char in vowels:
                    count += 1
            return count
        result = count_vowels(window)
        curr = result
        for right in range(k,len(s)):
            window.popleft()
            window.append(s[right])
            if s[right] in vowels and s[left] not in vowels:
                curr += 1
                result = max(result, curr)
            elif s[right] not in vowels and s[left] in vowels:
                curr -= 1
            left += 1
        return result
        