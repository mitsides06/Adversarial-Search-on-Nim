# I ASSUME THAT ALL INPUTS ARE VALID, SHOULD I NOT?

# class Game
class Game:

    def __init__(self):
        # see what do add hee throughout

        #self.heaps_num = None
        #self.objects_num = None
        self.state = None
        self.max_removal = None

    def play(self):
        n = int(input("Please enter the number of heaps: \n"))
        m = int(input("Please enter the number of objects in each heap: \n"))
        k = int(input("Please enter the maximum number of objects that can be removed from a single heap: \n"))

        self.state = self.initialize_game(n, m)
        self.max_removal = k

        winner = 0
        print("This is the initial structure of the heaps: \n")
        self.drawheaps()
        while not self.is_terminal(self.state):
            action = self.max_decision(self.state)
            print(f"I recommend you to remove {action[1]} objects from heap {action[0]}\n")
            heap_num = int(input("Please enter from which heap you want to remove objects: \n"))
            objects_num = int(input("PLease enter how many objects you want to remove: \n"))
            self.update_state((heap_num, objects_num))
            print("\nThe current structure of the heaps looks like this: \n")
            self.drawheaps()
            winner = 0
            if not self.is_terminal(self.state):
                computer_action = self.min_decision(self.state)
                print(f"Computer removes {computer_action[1]} from heap {computer_action[0]}\n")
                self.update_state(computer_action)
                print("The current structure of the heaps looks like this: \n")
                self.drawheaps()
                winner = 1

        print("End of game!\n")
        if winner == 1:
            print("Well done! you won!")
        else:
            print("Sorry! You lost!")   
        






        
    def update_state(self, action):
        self.state[action[0]] -= action[1]

        


    def initialize_game(self, n, m):
        # this should intiliaze the n heaps and m objects
        """ Initializes the n heaps with m objects at the
            beginning of the game.   WHAT ABOUT MAX REMOVAL?

            Args:
                n (int) : number of heaps
                m (int) : number of objects per heap
                k (int) : numebr of maximum objects to be removed each time
            
            Returns:
                None
        """
        """
        if type(n) != int or type(m) != int \
            or type(k) != int:
            return "Please insert only integer inputs!"
        self.heaps_num = n
        self.objects_num = m
        self.max_removal = k
        """

        return [m] * n



    def drawheaps(self):
        # this should show the heaps on the screen

        
        heaps = self.state

        for idx, heap in enumerate(heaps):
            print(f"Heap {idx}:", end="")
            for num in range(heap):
                print("o", end=" ")
            print()


    def max_decision(self, state):
        n = 0
        #state = state.copy()
        best_action = None
        max_value = -float("inf")
        for action in self.action(state):
            if self.min_value(self.result(state, action), n) > max_value:
                best_action = action
                max_value = self.min_value(self.result(state, action), n)
        
        return best_action
            
    def min_value(self, state, n):
        n += 1
        if self.is_terminal(state):
            if n % 2 == 0:
                return 1
            else:
                return -1
        value = float("inf")
        
        for action in self.action(state):
            value = min(value, self.max_value(self.result(state, action), n))
        
        return value
    
    def min_decision(self, state):
        n = 1
        #state = state.copy()
        best_action = None
        min_value = float("inf")
        for action in self.action(state):
            if self.max_value(self.result(state, action), n) < min_value:
                best_action = action
                min_value = self.max_value(self.result(state, action), n)

        return best_action
    
    def max_value(self, state, n):
        n += 1
        if self.is_terminal(state):
            if n % 2 == 0:
                return 1
            else:
                return -1
        value = -float("inf")
        
        for action in self.action(state):
            value = max(value, self.min_value(self.result(state, action), n))
        
        return value


    # helper funtions

    def action(self, state):
        action_space = []
        for idx, object_num in enumerate(state):
            if object_num == 0:
                pass
            elif object_num < self.max_removal:
                for i in range(1, object_num+1):
                    action_space.append((idx, i))
            else:
                for i in range(1, self.max_removal+1):
                    action_space.append((idx,i))

        return action_space
    
    def is_terminal(self, state):
        return sum(state) == 0
    

    
    def result(self, state, action):
        state = state.copy()
        state[action[0]] -= action[1]
        
        return state

if __name__ == "__main__":
    test = Game()

    test.play()
