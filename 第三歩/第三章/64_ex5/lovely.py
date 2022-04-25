# lovely.py

WILL = "Where there is a will, there is a way."
MIND = 0

def lovely(arg=None):
    global MIND

    if MIND == arg:
        print(WILL)
    
    else:
        print("Thank you lovely")
        MIND += 1
        lovely(arg)

if __name__ == "__main__":
    lovely(1)