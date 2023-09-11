def inverteDigito(n, reverse = 0):
    if n == 0:
        return reverse
    return inverteDigito(n // 10, reverse * 10 + n % 10)

print(inverteDigito(12345))