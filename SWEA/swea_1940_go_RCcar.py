import sys
sys.stdin = open("input.txt", "r")


def go_command(com, now_speed):
    if len(com) == 1:
        return now_speed
    
    else:
        if com[0] == '1':
            now_speed += int(com[2])

        else: #com[0] == '2' 인경우
            now_speed -= int(com[2])
            if now_speed < 0:
                now_speed = 0
        
        return now_speed

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    now_speed = 0
    dis = 0
    for i in range(N):
        com = input()
        now_speed = go_command(com, now_speed)
        dis += now_speed
    
    print(f"#{tc} {dis}")

        