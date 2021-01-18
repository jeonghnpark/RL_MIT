import numpy as np
import pickle
import sys

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
                self.winner = -1
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
        return self.end

    def next_state(self, i, j, symbol):
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


def get_all_states_impl(current_state, current_symbol, all_states):
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if current_state.data[i, j] == 0:
                new_state = current_state.next_state(i, j, current_symbol)
                new_hash = new_state.hash()
                if new_hash not in all_states:  # if yes, when?
                    is_end = new_state.is_end()
                    all_states[new_hash] = (new_state, is_end)
                    if not is_end:
                        get_all_states_impl(new_state, -current_symbol, all_states)
                else:
                    # print("found states !")
                    pass



def get_all_states():
    current_state = State()
    current_symbol = 1
    all_states = dict()
    all_states[current_state.hash()] = (current_state, current_state.is_end())
    get_all_states_impl(current_state, current_symbol, all_states)
    return all_states

all_states=get_all_states()

class Player:
    def __init__(self,step_size=0.1,epsilon=0.1):
        self.estimations=dict()
        self.step_size=step_size
        self.epsilon=epsilon
        self.states=[]
        self.greedy=[]
        self.symbol=0

    def reset(self):
        self.states=[]
        self.greedy=[]

    def set_state(self,state):
        self.states.appen(state)
        self.greedy.append(True)

    def set_symbol(self,symbol):
        #player의 symbol과 초기 estimation을 설정함
        self.symbol=symbol
        for hash_value in all_states:
            state, is_end=all_states[hash_value]
            if is_end:
                if state.winner==self.symbol:
                    self.estimations[hash_value]=1.0
                elif state.winner==0:
                    self.estimations[hash_value]=0.5
                else: #when lose
                    self.estimations[hash_value]=0
            else:
                self.estimations[hash_value]=0.5

    def backup(self):
        pass

    def act(self):
        #list all possible position and it's stata
        state=self.states[-1]
        next_states=[]
        next_positions=[]
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if self.data[i,j]==-0:
                    next_states.append(state.next_state(i,j,self.symbol).hash())
                    next_positions.append([i,j])

        #choose position
        if np.random.rand() < self.epsilon:
            action=next_positions[np.random.randint(len(next_positions))]

def train(epochs,print_every_n=500):
    pass

def compete(turns):
    pass

def play():
    pass

if __name__=="__main__":
    train(int(1e5))
    compete(int(1e3))
    play()
