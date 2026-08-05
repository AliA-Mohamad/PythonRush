def findMissingElements(nums: List[int]) -> List[int]:
    numeroMaior = max(nums)
    numeroMenor = min(nums)

    listaCompleta = list(range(numeroMenor, numeroMaior+1))
    resultado = [num for num in listaCompleta if num not in nums]
    return resultado

def findMissingElements2(nums: List[int]) -> List[int]:
    numsSet = set(nums)
    return [ num for num in range(min(nums), max(nums) + 1) if num not in numsSet]

def findMissingElements3(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        indice = abs(nums[i]) - 1

        if nums[indice] > 0:
            nums[indice] *= -1

    resultado = []

    for i in range(len(nums)):
        if nums[i] > 0:
            resultado.append(i + 1)

    return resultado


print(findMissingElements3([1,4,2,5]))
print(findMissingElements3([7,8,6,9]))
print(findMissingElements3([5,1]))