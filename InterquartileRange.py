# Function to compute median of a given list
def med(a):
    if len(a) % 2 == 1:
        return a[int(len(a)/2)]
    else:
        return (a[int(len(a)/2-1)] + a[int(len(a)/2)])/2
# Consume n from input
n = input()
# Integer list
X = [int(num) for num in input().split()]
# Frequency list
F = [int(num) for num in input().split()]
# Create dataset
S = []
for i in range(len(F)):
    for _ in range(F[i]):
        S.append(X[i])
S.sort()
#q1
q1 = med(S[:int(len(S)/2)])
#q3
q3 = med(S[-int(len(S)/2):])
# Print interquartile range
print(q3-q1)
