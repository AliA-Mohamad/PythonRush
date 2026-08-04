def findMissingElements(nums: List[int]) -> List[int]:
    numeroMaior = max(nums)
    numeroMenor = min(nums)

    listaCompleta = list(range(numeroMenor, numeroMaior+1))
    resultado = [num for num in listaCompleta if num not in nums]
    return resultado

def findMissingElements2(nums: List[int]) -> List[int]:
    numsSet = set(nums)
    return [ num for num in range(min(nums), max(nums) + 1) if num not in numsSet]

print(findMissingElements2([1,4,2,5]))
print(findMissingElements2([7,8,6,9]))
print(findMissingElements2([5,1]))