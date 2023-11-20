# I ASSUME THAT ALL INPUTS ARE VALID, SHOULD I NOT?

# class Game
class Game:

    def __init__(self):
        # see what do add hee throughout

        #self.heaps_num = None
        #self.objects_num = None
        n = int(input("Please enter the number of heaps: \n"))
        m = int(input("Please enter the number of objects in each heap: \n"))
        k = int(input("Please enter the maximum number of objects that can be removed from a single heap: \n"))

        self.state =  self.initialize_game(n, m)
        self.max_removal = k
        

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
            print(f"Heap {idx+1}:", end="")
            for num in range(heap):
                print("o", end=" ")
            print()

    def play(self):
        # to actually start playing the game
        pass

    def max_decision(self, state):
        best_action = None
        max_value = -float("inf")
        for action in self.action(state):
            if self.min_value(self.result(state, action)) > max_value:
                best_action = action
                max_value = self.min_value(self.result(state, action))
        
        return best_action
            
    def min_value(self, state):
        if self.is_terminal():
            return -1
        value = float("inf")
        
        for action in self.action(state):
            value = min(value, self.max_value(self.result(state, action)))
        
        return value
    
    def min_decision(self, state):
        best_action = None
        min_value = float("inf")
        for action in self.action(state):
            if self.max_value(self.result(state, action)) < min_value:
                best_action = action
                min_value = self.max_value(self.result(state, action))

        return best_action
    
    def max_value(self, state):
        if self.is_terminal():
            return 1
        value = -float("inf")
        
        for action in self.action(state):
            value = max(value, self.min_value(self.result(state, action)))
        
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
    
    def is_terminal(self):
        return sum(self.state) == 0
    

    
    def result(self, state, action):
        state[action[0]] -= action[1]
        
        return state

if __name__ == "__main__":
    pass