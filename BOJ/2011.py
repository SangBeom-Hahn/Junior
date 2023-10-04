'''
1. 모든 경우의 수
1) dp에 뭐 들가자
2) 점화식
3) 베이스   S[0] = 1 / S[1] = 0이면 0  그외면 1
    
    01234
arr 251121

n   dp      종류
0   1        B
1   2         BE / Y    현재가 0이 아니면 DP[I] += DP[I-1], 
                        현재와 N-1이 11 ~ 26이면 DP[I] += DP[I-1] * DP[I-2]
2   2        BEA / YA
3   4        BEAA / BEK / YAA / YK
4   6         BEAAD / BEKD / BEAN / YAAD / YAN / YKD

5           BEAADA / BEKDA / BEANA / BEAAV / BEKV / 
            YAADA / YANA / YKDA / YKV / YAAV
            
안되는 경우            
arr 2040
         
n   dp      종류            
0    1       B
1    1       U  현재가 0이면 현재와 N-1이 10이나 20이면 DP[I] += DP[I-1], 
2    1       UD 
3    0           현재가 0인데 현재와 N-1이 20 이상이면 0

QRSTU VWXYN

* 암호
출력 : 해석의 가짓수를 구해라(해석 불가면 0)

2. 무지막지
'''

s = input()
s = ' ' + s
dp = [0] * 5001
dp[0] = 1
dp[1] = 1
flag = False

if(s[1] == '0'):
    print(0)
else:
    for i in range(2, len(s)):
        if(s[i] > '0'):
            dp[i] = dp[i-1]
        if(s[i-1] != '0' and s[i-1] + s[i] < '27'):
            dp[i] += dp[i-2]

print(dp[len(s)-1] % 1000000)