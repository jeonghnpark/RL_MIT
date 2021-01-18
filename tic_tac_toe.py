import numpy as np
import pickle

BOARD_ROWS = 3
BOARD_COLS = 3
BOARD_SIZE = BOARD_ROWS * BOARD_COLS


class State:
    def __init__(self):
        # 1:first player's move
        # -1:another player's move
        # 0:empty
        self.data = np.zeros((BOARD_ROWS, BOARD_COLS))
        self.winner = None
        self.hash_val = None
        self.end = None

    def hash(self):
        if self.hash_val is None:
            self.hash_val = 0
            for el in np.nditer(self.data):
                self.hash_val = self.hash_val * 3 + el + 1
        return self.hash_val

    def is_end(self):
        if self.end is not None:  # self.end값이 있다면 새로 값을 업데이트하지 않음
            return self.end
        results = []
        for i in range(BOARD_ROWS):
            results.append(np.sum(self.data[i, :]))
        for i in range(BOARD_COLS):
            results.append(np.sum(self.data[:, i]))
        # diagonal
        trace = 0
        reverse_trace = 0
        for i in range(BOARD_ROWS):
            trace += self.data[i, i]
            reverse_trace += self.data[i, BOARD_ROWS - 1 - i]

        results.append(trace)
        results.append(reverse_trace)

        for result in results:
            if result == 3:
                self.winner = 1
                self.end = True
                return self.end
            if result == -3:
                self.winne = -1
                self.end = True
                return self.end

        # when tie
        sum_values = np.sum(np.abs(self.data))
        if sum_values == BOARD_SIZE:  # every move is done
            self.winner = 0
            self.end = True
            return self.end

        # game is now going
        self.end = False
        return self.endmeiummedium

    def next_state(self, i, j, symbol):
        # return next State
        new_state = State()
        new_state.data = np.copy(self.data)  # difference btn self.data
        new_state.data[i, j] = symbol
        return new_state

    def print_state(self):
        for i in range(BOARD_ROWS):
            print('----------')
            out = '|'
            for j in range(BOARD_COLS):
                if self.data[i, j] == 1:
                    token = "*"
                elif self.data[i, j] == -1:
                    token = "x"
                else:
                    token = '0'
                out += token + '|'
            print(out)
        print('----------')
