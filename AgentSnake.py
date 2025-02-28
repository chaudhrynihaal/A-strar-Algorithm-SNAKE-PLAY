from queue import PriorityQueue
import copy

class AgentSnake:
    def __init__(self):
        pass
    
    def cost(self, state, action):
        # Cost function: constant cost for each action
        return 1

    def SearchSolution(self, state, max_depth=100):
        visited = set()
        queue = PriorityQueue()
        queue.put((0, state, []))  # (cost, state, plan)
        
        while not queue.empty():
            cost, current_state, current_plan = queue.get()
            
            if current_state.snake.HeadPosition.X == current_state.FoodPosition.X and current_state.snake.HeadPosition.Y == current_state.FoodPosition.Y:
                return current_plan
            
            if (current_state.snake.HeadPosition.X, current_state.snake.HeadPosition.Y) in visited:
                continue
            
            visited.add((current_state.snake.HeadPosition.X, current_state.snake.HeadPosition.Y))
            
            if len(current_plan) >= max_depth:
                return []  
        
        
            for move in [0, 3, 6, 9]:  # Up, Down, Right, Left
                new_state = copy.deepcopy(current_state)
                new_plan = current_plan + [move]
                new_state.snake.HeadDirection.Update(0, 0)  # Reset direction
                if move == 0:
                    new_state.snake.HeadDirection.Y = -1
                elif move == 6:
                    new_state.snake.HeadDirection.Y = 1
                elif move == 3:
                    new_state.snake.HeadDirection.X = 1
                elif move == 9:
                    new_state.snake.HeadDirection.X = -1
                
                new_state.snake.moveSnake(new_state)
                
                action_cost = self.cost(new_state, move)
                total_cost = cost + action_cost
                queue.put((total_cost, new_state, new_plan))
                
        return []  # If no solution is found
