from copy import deepcopy

class Tic_Tac_Toe:
    def __init__(self, size):  
        self.size = size
   
    def Display_Current_State(self, curr_state):
        print("\n")
        print('[' + curr_state[0][0] + ' ' + curr_state[0][1] + ' ' + curr_state[0][2] + "]")
        print('[' + curr_state[1][0] + ' ' + curr_state[1][1] + ' ' + curr_state[1][2] + "]")
        print("[" + curr_state[2][0] + ' ' + curr_state[2][1] + ' ' + curr_state[2][2] + "]")
       
    def Success(self, state):
        for i in range(self.size):
            if (state[i][0] == 'X' and state[i][1] == 'X' and state[i][2] == 'X'):
                return True
        for i in range(self.size):
            if (state[0][i] == 'X' and state[1][i] == 'X' and state[2][i] == 'X'):
                return True
        if (state[0][0] == 'X' and state[1][1] == 'X' and state[2][2] == 'X'):
            return True
        if (state[0][2] == 'X' and state[1][1] == 'X' and state[2][0] == 'X'):
            return True
        return False
   
    def Lose(self, state):
        for i in range(self.size):
            if (state[i][0] == 'O' and state[i][1] == 'O' and state[i][2] == 'O'):
                return True
        for i in range(self.size):
            if (state[0][i] == 'O' and state[1][i] == 'O' and state[2][i] == 'O'):
                return True
        if (state[0][0] == 'O' and state[1][1] == 'O' and state[2][2] == 'O'):
            return True
        if (state[0][2] == 'O' and state[1][1] == 'O' and state[2][0] == 'O'):
            return True
        return False
   
    def Draw(self, state):
        for i in range(self.size):
            for j in range(self.size):
                if(state[i][j] == '_'):
                    return False
        return True
   
    def aimove(self, state):
        minv = 1
        mini = 0
        index = 0
        for i in range(self.size):
            for j in range(self.size):
                index += 1
                if (state[i][j] == '_'):
                    temp_state = deepcopy(state)
                    temp_state[i][j] = 'O'
                    val = self.Best_Move(temp_state, 'min')
                    if (val < minv):
                        minv = val
                        mini = index
        return mini
   
    def Best_Move(self, state, player):
        if(self.Success(state)):
            return 1
        if(self.Lose(state)):
            return -1
        if(self.Draw(state)):
            return 0
        if(player == 'min'):
            maxv = -1
            for i in range(self.size):
                for j in range(self.size):
                    if(state[i][j] == '_'):
                        temp_state = deepcopy(state)
                        temp_state[i][j] = 'X'
                        val = self.Best_Move(temp_state, 'max')
                        if(val > maxv):
                            maxv = val
            return maxv
        if(player == 'max'):
            minv = 1
            for i in range(self.size):
                for j in range(self.size):
                    if (state[i][j] == '_'):
                        temp_state = deepcopy(state)
                        temp_state[i][j] = 'O'
                        val = self.Best_Move(temp_state, 'min')
                        if (val < minv):
                            minv = val
            return minv
   
    def Start_Game(self):
        curr_state = [['_','_','_'] for i in range(self.size)]
        self.Display_Current_State(curr_state)
        for i in range(9):
            if(i%2 == 0):
                user_move = int(input("\n User's turn :"))
                while(curr_state[int((user_move-1)/self.size)][int((user_move-1)%self.size)] != '_'):
                    user_move = int(input("\n Enter a valid move :"))
                curr_state[int((user_move-1)/self.size)][int((user_move-1)%self.size)] = 'X'
                self.Display_Current_State(curr_state)
               
            else:
                print("\n System's turn.....")
                system_move = self.aimove(curr_state)
                curr_state[int((system_move-1)/self.size)][int((system_move-1)%self.size)] = 'O'
                self.Display_Current_State(curr_state)
               
            if (self.Success(curr_state)):
                print("\n You win the game!")
                return
            elif(self.Lose(curr_state)):
                print("\n You lose the game!")
                return
            elif(self.Draw(curr_state)):
                print("\n Match draw!")
                return

t = Tic_Tac_Toe(3)
t.Start_Game()