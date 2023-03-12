import time
import tqdm
import sksound
from playsound import playsound
from ctypes import *
from ctypes import wintypes as w

dll = WinDLL('winmm')

# sounds from https://pixabay.com/sound-effects/call-to-attention-123107/ and https://pixabay.com/sound-effects/success-fanfare-trumpets-6185/


# sksound.sounds.Sound("sounds/success-fanfare-trumpets-6185.mp3")

longbreak = 30
shortbreak = 5
work = 60
interval = 4
total_time = 0

work_dict = {"personal projects": 120, "open source":30, "research":30}
math = {"udemy": 120, "reading":60, "brilliant":60}
home = {"chores": 30, "exercise":30}
hobby = {"duolingo":15, "reading":20, "random discovery":120}

tasks = {
    "Work": dict(work_dict),
    "Math": dict(math),
    "home": dict(home),
    "hobby": dict(hobby),
}




cycle_num = 1
prev_chunk = 0

def break_time(cycle_num, total_time):
    playsound("sounds/success-fanfare-trumpets-6185.mp3")

    if cycle_num % interval == 0:
        print("Long break")
        for _ in tqdm.trange(longbreak*60):
            time.sleep(1)
            
        total_time += longbreak

    else:
        print("Short break")
        for _ in tqdm.trange(shortbreak*60):
            time.sleep(1)
        total_time += shortbreak
    playsound("sounds/call-to-attention-123107.mp3")

    return total_time

for i in tasks:
    cycle_num += 1
    for j in tasks[i]:
        print(int(tasks[i][j]))
        chunk = int(tasks[i][j]) / work
        print(chunk)
        # if chunk is less than 1, then combine it with the next task


        for l in range(int(chunk)):
            print(f"Task: {i}: {j}, Chunk: {l+1}/{int(chunk)}")
            if chunk < 1:
                new_work = work * chunk
            else:
                new_work = work
                print(new_work)

            for _ in tqdm.tqdm(range(new_work*60)):
                time.sleep(1)
            total_time = break_time(cycle_num, total_time)
            total_time += new_work

            cycle_num += 1

print(total_time)
print(total_time/60)
