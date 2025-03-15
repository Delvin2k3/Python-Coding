from tqdm import tqdm
import time
for i in tqdm(range(1000), desc= "Loading . . . . ."):
    time.sleep(0.01)

people_names = ["alex", "boby", "cart"]

[print(name) for name in tqdm(people_names, desc = "people names")]