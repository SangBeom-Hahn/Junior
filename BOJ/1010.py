'''

'''

def check(mid, s, n):
    cnt = 1
    max_freq = 0
    freq = [0] * 26
    
    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1
        max_freq = max(max_freq, freq[ord(s[i]) - ord('a')])

        if max_freq * cnt > mid:
            max_freq = freq[ord(s[i]) - ord('a')]
            cnt += 1
            
    return cnt <= n

def solution(s, n):
    left = 1
    right = len(s) * 26
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        if check(mid, s, n):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer // n


# "aabbbabba"
# "xyyyxxxxxx"

s = "abcd"
n = 1

print(solution(s, n))