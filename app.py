import math

varInput = input("Enter some phrases ")
varJoin = varInput.replace(" ", "")
varCount = len(varJoin)
varSqrt = math.sqrt(varCount)
varCeiling = math.ceil(varSqrt)
varOutput = []

for i in range(0, varCount, varCeiling):
    substring = varJoin[i:i + varCeiling]
    varOutput.append(substring)

result = ' '.join(varOutput)

print(result)