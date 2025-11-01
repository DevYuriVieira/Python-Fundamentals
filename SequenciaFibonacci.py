n = int(input("Digite quantas sequencias de Fibonacci a seguir, deseja: "))

a, b = 0, 1
print("Sequencia de Fibonacci: ")

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b




