import sys
def input():return sys.stdin.readline().rstrip()

while True:
    a = input()

    if a[0]=="-":
        break
    a = float(a)
    print(f"Objects weighing {a:.2f} on Earth will weigh {a*0.167:.2f} on the moon.")
    
    
