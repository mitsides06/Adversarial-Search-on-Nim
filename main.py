# class Game
class Game:

    def __init__(self):
        # see what do add hee throughout
        self.heaps_num = None
        self.objects_num = None
        self.max_removal = None 

    def initialize_game(self, n, m, k):
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
        if type(n) != int or type(m) != int \
            or type(k) != int:
            return "Please insert only integer inputs!"
        self.heaps_num = n
        self.objects_num = m
        self.max_removal = k

    def drawheaps(self):
        # this should show the heaps on the screen
        if self.heaps_num == None:
            return "Game hasn't been initiliazed yet!"
        
        heaps = [self.objects_num] * self.heaps_num

        for idx, heap in enumerate(heaps):
            print(f"Heap {idx+1}:", end="")
            for num in range(heap):
                print("o", end=" ")
            print()

    def play(self):
        # to actually start playing the game
        pass


if __name__ == "__main__":
    test = Game()
    test.initialize_game(8,4,2)
    test.drawheaps()