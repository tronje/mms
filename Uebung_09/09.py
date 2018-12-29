#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt


class GameState(object):
    def __init__(self):
        self.shell_with_ball = np.random.randint(3)
        self.picked_shell = np.random.randint(3)

        possible_uncovers = [0, 1, 2]
        possible_uncovers.remove(self.shell_with_ball)

        if self.picked_shell != self.shell_with_ball:
            possible_uncovers.remove(self.picked_shell)

        self.unconvered_shell = np.random.choice(possible_uncovers)

    def win(self):
        if self.shell_with_ball == self.picked_shell:
            return True
        else:
            return False

    def switch_choice(self):
        possible_shells = [0, 1, 2]
        possible_shells.remove(self.picked_shell)
        possible_shells.remove(self.unconvered_shell)
        self.picked_shell = possible_shells[0]


def main():
    wins_without_switching = 0
    wins_over_number_of_trials = []

    for i in range(10000):
        gs = GameState()
        if gs.win():
            wins_without_switching += 1
        wins_over_number_of_trials.append(wins_without_switching)

    plt.plot(wins_over_number_of_trials, label="Without switching")

    wins_with_switching = 0
    wins_over_number_of_trials = []

    for i in range(10000):
        gs = GameState()
        gs.switch_choice()
        if gs.win():
            wins_with_switching += 1
        wins_over_number_of_trials.append(wins_with_switching)

    plt.plot(wins_over_number_of_trials, label="With switching")

    print(f"Without switching: {wins_without_switching} wins out of 10000")
    print("Relative frequency of winning without switching: "
          f"{wins_without_switching / 10000}")

    print()

    print(f"With switching: {wins_with_switching} wins out of 10000")
    print("Relative frequency of winning with switching: "
          f"{wins_with_switching / 10000}")

    plt.xlabel("games played")
    plt.ylabel("wins")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
