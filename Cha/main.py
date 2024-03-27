# main.py

import Wumpus
import Agent

# GridWorld 인스턴스 생성
world = Wumpus.GridWorld()
world.setup_grid()

# Agent 인스턴스 생성
agent = Agent.Agent(grid_size=world.grid_size)

# 에이전트가 금을 가지고 있고 (1, 1) 위치에 있는지 확인하는 조건으로 게임 루프 시작
while not (agent.has_gold and agent.x == 1 and agent.y == 1):
    # 에이전트를 움직입니다.
    agent.move(world.grid)

    # 수정된 print_grid 호출 방식
    world.print_grid(agent.x, agent.y)

    # 에이전트가 죽었을 경우, (1, 1) 위치로 리셋
    if not agent.is_alive:
        agent.reset()
        print("에이전트가 (1, 1) 위치로 리셋되었습니다.")

# 게임 종료 조건에 도달했을 때 실행될 코드
print("게임 종료: 에이전트가 금을 가지고 시작 위치로 돌아왔습니다!")
