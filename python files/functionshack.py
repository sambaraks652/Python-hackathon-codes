def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_term = sequence[i-1] + sequence[i-2]
        sequence.append(next_term)

    return sequence

n = int(input("Enter the value of n: "))

fibonacci_sequence = generate_fibonacci_sequence(n)
print(fibonacci_sequence)