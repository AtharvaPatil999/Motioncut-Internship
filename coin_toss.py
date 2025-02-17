import random

def flip_coin():
    return random.choice(["Heads", "Tails"])

def coin_toss_simulation():
    while True:
        try:
            num_flips = int(input("Enter the number of times you want to flip the coin: "))
            if num_flips <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        
        heads_count = 0
        tails_count = 0
        
        for _ in range(num_flips):
            result = flip_coin()
            print(result)
            if result == "Heads":
                heads_count += 1
            else:
                tails_count += 1
        
        total = heads_count + tails_count
        print("\nResults:")
        print(f"Heads: {heads_count} ({(heads_count / total) * 100:.2f}%)")
        print(f"Tails: {tails_count} ({(tails_count / total) * 100:.2f}%)")
        
        again = input("Do you want to flip again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for playing!")
            break

coin_toss_simulation()
