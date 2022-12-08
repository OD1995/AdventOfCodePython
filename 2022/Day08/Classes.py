class Forest:

    def __init__(
        self,
        list_of_lists
    ):
        self.list_of_lists = list_of_lists
        self.trees = [
            Tree(x,y,list_of_lists)
            for x in range(len(list_of_lists[0]))
            for y in range(len(list_of_lists))
        ]

    def get_visible_count(self):
        count = 0
        for t in self.trees:
            if t.check_if_visible():
                count += 1
        return count

    def print_me(self):
        # return_me = ""
        # for y in range(len(self.list_of_lists)):
        #     row_str = ""
        #     for x in range(len(self.list_of_lists[0])):
        L = [
            [0] * len(self.list_of_lists[0])
            for y in range(len(self.list_of_lists))
        ]
        for t in self.trees:
            if t.check_if_visible():
                L[t.y][t.x] = 1
        return_me = ""
        for x in L:
            return_me += "".join(map(str,x)) + "\n"
        print(return_me)

    def get_max_scenic_score(self):
        max_scenic_score = 0
        for t in self.trees:
            max_scenic_score = max(max_scenic_score,t.get_scenic_score())
            # print(t.x,t.y,t.get_scenic_score())
        return max_scenic_score


class Tree:

    def __init__(
        self,
        x,
        y,
        list_of_lists
    ):
        self.x = x
        self.y = y
        self.height = list_of_lists[y][x]
        self.list_of_lists = list_of_lists
        self.sides = ['L','U','R','D']

    def check_if_visible(self):
        if self.check_if_on_edge():
            return True
        for side in self.sides:
            visible = self.check_if_visible_from_side(side)
            if visible:
                return True
        return False

    def check_if_visible_from_side(self,side):
        heights_in_front = self.get_heights_in_front()
        return not self.is_hidden(heights_in_front)
        
    def get_heights_in_front(self,side):
        if side == 'L':
            heights_in_front = self.list_of_lists[self.y][:self.x]
        elif side == "U":
            heights_in_front = [
                row[self.x]
                for row in self.list_of_lists[:self.y]
            ]
        elif side == 'R':
            heights_in_front = reversed(self.list_of_lists[self.y][self.x+1:])
        elif side == 'D':
            heights_in_front = [
                row[self.x]
                for row in reversed(self.list_of_lists[self.y+1:])
            ]
        return heights_in_front

    def is_hidden(self,heights_in_front):
        for h in heights_in_front:
            if h >= self.height:
                return True
        return False

    def check_if_on_edge(self):
        if (
            (self.x == 0) |
            (self.y == 0) |
            (self.x == len(self.list_of_lists) - 1) |
            (self.y == len(self.list_of_lists[0]) - 1)
        ):
            return True
        else:
            return False

    def get_scenic_score(self):
        if ([self.x,self.y] == [2,3]):
            a=1
        scenic_score = 1
        # X = {}
        for side in self.sides:
            scenic_score *= self.get_viewing_distance(side)
            # X[side] = self.get_viewing_distance(side)
        return scenic_score

    def get_viewing_distance(self,side):
        if self.check_if_on_edge():
            return 0
        heights_in_front = list(reversed(list(self.get_heights_in_front(side))))
        viewing_distance = 1
        for h in heights_in_front:
            if h >= self.height:
                return viewing_distance
            else:
                viewing_distance += 1
        return viewing_distance - 1