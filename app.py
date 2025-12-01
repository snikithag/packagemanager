# app.py
import numpy as np

def main():
    a = np.array([1, 2, 3, 4])
    print("Array:", a)
    print("Sum:", a.sum())
    return int(a.sum())

if __name__ == "__main__":
    main()   # do not call exit(main())

