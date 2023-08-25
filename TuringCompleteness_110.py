import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def apply_rule(rule, state, idx):
    key = str(state[max(idx - 1, 0)]) + str(state[idx]) + str(state[(idx + 1) % len(state)])
    return int(rule[key])

def generate_next_state(rule, current_state):
    return [apply_rule(rule, current_state, idx) for idx in range(len(current_state))]

def simulate_rule_110(steps, width):
    rule110 = {
        "111": 0, "110": 1, "101": 1, "100": 0,
        "011": 1, "010": 1, "001": 1, "000": 0
    }
    
    initial_state = [0] * width
    initial_state[width // 2] = 1
    
    states = [initial_state]
    for _ in range(steps):
        next_state = generate_next_state(rule110, states[-1])
        states.append(next_state)
    
    return states

def animate(states):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("Rule 110 Cellular Automaton")
    ax.set_xlabel("Cell")
    ax.set_ylabel("Time Step")
    
    def update(frame):
        ax.cla()
        ax.imshow([states[frame]], cmap="binary", aspect="auto", extent=[-0.5, len(states[frame]) - 0.5, len(states) - frame - 0.5, len(states) - frame + 0.5])
        ax.set_title(f"Time Step {frame}")
        ax.set_xlabel("Cell")
        ax.set_ylabel("Time Step")
    
    ani = FuncAnimation(fig, update, frames=len(states), interval=500)
    plt.show()

def main():
    steps = 50
    width = 101
    
    states = simulate_rule_110(steps, width)
    animate(states)

if __name__ == "__main__":
    main()
