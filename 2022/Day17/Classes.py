class RockPoint:

    def __init__(
        self,
        x,
        y,
        is_rock
    ):
        self.x = x
        self.y = y
        self.is_rock = is_rock

    def test_move_rp_x(
        self,
        n,
        other_rock_coords
    ):
        new_x = self.x + n
        if (
            (new_x > 6) | 
            (new_x < 0) |
            ((new_x,self.y) in other_rock_coords)
        ):
            return False
        else:
            return True

    def move_rp_x(
        self,
        n
    ):
        self.x = self.x + n

    def test_move_rp_y(
        self,
        n,
        other_rock_coords
    ):
        new_y = self.y + n
        if (
            (new_y < 0) |
            ((self.x,new_y) in other_rock_coords)
        ):
            return False
        else:
            return True

    def move_rp_y(
        self,
        n
    ):
        self.y = self.y + n
        

class Rock:

    def __init__(
        self,
        rock_index,
        starting_x,
        starting_y
    ):
        self.rock_index = rock_index
        shape_index = rock_index % 5
        rock_point_coords = self.get_rock_point_coords(shape_index)
        self.rock_points = []
        self.rock_points_dict = {}
        for y in range(4):
            for x in range(4):
                rp = RockPoint(
                    x + starting_x,
                    y + starting_y,
                    (x,y) in rock_point_coords
                )
                self.rock_points.append(rp)
                self.rock_points_dict[(x,y)] = rp
    
    def print_rock(self):
        for y in range(3,-1,-1):
            print_me = ""
            for x in range(4):
                if self.rock_points_dict[(x,y)].is_rock:
                    print_me += "#"
                else:
                    print_me += "."
            print(print_me)

    def move_rock_x(self, n, other_rock_coords):
        results = []
        for rp in self.rock_points:
            if rp.is_rock:
                res = rp.test_move_rp_x(n, other_rock_coords)
                results.append(res)
        if all(results):
            for rp in self.rock_points:
                if rp.is_rock:
                    rp.move_rp_x(n)
            return True
        else:
            return False

    def move_rock_y(self, n, other_rock_coords):
        results = []
        for rp in self.rock_points:
            if rp.is_rock:
                res = rp.test_move_rp_y(n, other_rock_coords)
                results.append(res)
        if all(results):
            for rp in self.rock_points:
                if rp.is_rock:
                    rp.move_rp_y(n)
            return True
        else:
            return False

    def get_final_coords(self):
        fc = []
        for rp in self.rock_points:
            if rp.is_rock:
                fc.append((rp.x,rp.y))
        self.final_coords = fc
        return fc

    def get_max_height(self):
        max_height = 0
        for fc in self.final_coords:
            max_height = max(max_height,fc[1])
        return max_height

    def get_rock_point_coords(self,shape_index):
        if shape_index == 0:
            rock_point_coords = [
                (i,0)
                for i in range(4)
            ]
        elif shape_index == 1:
            rock_point_coords = [
                (1,0),
                (1,1),
                (1,2),
                (0,1),
                (2,1),
            ]
        elif shape_index == 2:
            rock_point_coords = [
                (0,0),
                (1,0),
                (2,0),
                (2,1),
                (2,2)
            ]
        elif shape_index == 3:
            rock_point_coords = [
                (0,i)
                for i in range(4)
            ]
        elif shape_index == 4:
            rock_point_coords = [
                (x,y)
                for x in range(2)
                for y in range(2)
            ]
        return rock_point_coords