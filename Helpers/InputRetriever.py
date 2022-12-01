import requests
import json

class InputRetriever:

    def __init__(
        self,
        year,
        day
    ):
        self.year = year
        self.day = day
        self.sessionID = '53616c7465645f5f5e641891906daa826ea62a9097bd8c46539f0ec5e63519891410e21bfb36c8f7678d557fb29c789069007b33e03ab9db471dc9cbe240f51f'
    
    def get_data(
        self
    ):
        r = requests.get(
            f"https://adventofcode.com/{self.year}/day/{self.day}/input",
            cookies={
                'session' : self.sessionID
            }
        )
        return r.text

    def save(
        self,
        data,
        test=False
    ):
        zero_padded = f"0{self.day}" if len(str(self.day)) == 1 else self.day
        T = "Test" if test else ""
        file_path = fr"C:\Dev\AdventOfCodePython\{self.year}\Day{zero_padded}\data{T}.json"
        with open(file_path,'w') as f:
            json.dump(data,f)

    def save_both(
        self,
        callback,
        data_list
    ):
        for i,D in enumerate(data_list):
            processed_data = callback(D)
            self.save(
                processed_data,
                i == 0
            )
