def tower(n: int, source: str, target: str, auxiliary: str):
    if n == 1:
        print(f'Move disk 1 from {source} to {target}')
        return
    tower(n-1, source, auxiliary, target)
    print(f'Move disk {n} from {source} to {target}')
    tower(n-1, auxiliary, target, source)

def main():
    try:
        n = int(input("Enter the number of disks for Tower of Hanoi: "))
        tower(n, 'A', 'C', 'B')
    except ValueError:
        print("Please enter Integer number.")

if __name__ == "__main__":
    main()
