class Valve:

    def __init__(
        self,
        valve,
        # rate,
        # options,
        data
    ):
        self.valve = valve
        self.rate = data[valve]['rate']
        self.options = data[valve]['options']
        self.data = data
        self.dead_end = len(self.options) == 1

    def get_path_to(
        self,
        destination_valve,
        checked_already
    ):
        if destination_valve in self.options:
            return [self.valve, destination_valve],checked_already
        elif self.dead_end:
            return False,checked_already
        else:
            routes = []
            for opt in self.options:
                if opt not in checked_already:
                    checked_already.append(opt)
                    res,checked_already = Valve(opt,self.data).get_path_to(destination_valve,checked_already)
                    if res:
                        routes.append(routes)
            if len(routes) > 0:
                return [self.valve] + min(routes,key=len), checked_already
            else:
                return False, checked_already
