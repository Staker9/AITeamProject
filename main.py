import Wumpus
import Agent

# GridWorld 인스턴스 생성
world = Wumpus.GridWorld()
world.setup_grid()

# Agent 인스턴스 생성
agent = Agent.Agent(grid_size=world.grid_size)

# 수정된 print_grid 호출 방식
world.print_grid(agent.x, agent.y)
