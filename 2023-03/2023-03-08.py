# 프로그래머스 - 여행경로
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43164

# 문제 : 
# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.
# 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항 :
# 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
# 주어진 공항 수는 3개 이상 10,000개 이하입니다.
# tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
# 주어진 항공권은 모두 사용해야 합니다.
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
# 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

def dfs(v, candi, tk):
    global answer
    if not 0 in v:
        c = candi[:]
        answer.append(c)
        return

    for i, t in enumerate(tk):
        if candi[-1] == t[0] and v[i] == 0:
            candi.append(t[1])
            v[i] = 1
            dfs(v, candi, tk)
            candi.pop()
            v[i] = 0

            
def solution(tickets):
    global answer
    answer = []
    v = [0] * len(tickets)
    start = []
    for i, cities in enumerate(tickets):
        if cities[0] == "ICN":
            start.append(i)
            
    for idx in start:
        cand = []
        cand.append(tickets[idx][0])
        cand.append(tickets[idx][1])
        v[idx] = 1
        dfs(v, cand, tickets)
        v[idx] = 0
        
    res = answer[0]
    if len(answer) > 1:
        for i in range(1,len(answer)):
            for j in range(len(answer[i])):
                check = 0
                for k in range(len(answer[i][j])):
                    if ord(res[j][k]) < ord(answer[i][j][k]):
                        check = 1
                        break
                    elif ord(res[j][k]) > ord(answer[i][j][k]):
                        res = answer[i]
                        check = 1
                        break
                if check == 1:
                    break
    
    return res
