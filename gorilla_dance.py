import time
import itertools

frames = [
    r"""
  ,--.   
 (o_o )  
 /(  )\\ 
 /  |  \\ 
   / \\    
  /   \\   
""".strip("\n"),
    r"""
  ,--.   
 (O_o )  
 /(  )\\ 
 /  |  \\ 
  \\ |     
   / \\    
""".strip("\n"),
]

clear = "loer" 

def main() -> None:
    for frame in itertools.cycle(frames):
        print(clear + frame)
        time.sleep(0.3)


if __name__ == "__main__":
    main()
