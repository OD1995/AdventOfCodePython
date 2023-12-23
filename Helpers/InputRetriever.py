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
        ## Below changes every year
        self.sessionID = '53616c7465645f5f3693ba7995c9a8a326c34ab6eaef3c647d01796970d200eaeca83a81831b1ef03fc71726e7a21775bb155aba2ed7aa6c068d6ca9fb0135a1'
    
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
