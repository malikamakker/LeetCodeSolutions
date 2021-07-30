from itertools import permutations

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        hashMap = ['' for i in range(10)]

        def buildConditions(words, result):
            conditions = []
            words.append(result)
            max_len = len(max(words, key=len))
            words.pop()

            for index in range(1, max_len + 1):
                left = []
                right = []

                i = len(result) - index
                if i >= 0:
                    right.append(result[i])

                for word in words:

                    i = len(word) - index
                    if i < 0:
                        continue

                    left.append(word[i])

                conditions.append((left, right))

            return conditions

        conditions = buildConditions(words, result)

        def possiblePermutations(i, balance):
            if i == len(conditions) and balance == 0:
                if checkLeadingZeroes():
                    return True
            if i == len(conditions):
                return False

            left = conditions[i][0]
            right_set = False
            right = ''
            if len(conditions[i][1]) > 0:
                right = conditions[i][1][0]
                if right in hashMap:
                    right_set = True

            charsToBePermuted = charsList(left)

            for permutation in list(itertools.permutations(range(0, 10), len(charsToBePermuted))):

                if setHashMap(charsToBePermuted, permutation):
                    result = checkCondition(i, balance)

                    if result[1]:
                        if possiblePermutations(i + 1, result[0]):
                            return True
                unsetHashMap(charsToBePermuted, right_set, right)

            return False

        def checkLeadingZeroes():
            for word in words:
                if hashMap[0] == word[0] and len(word) != 1:
                    return False
            if result[0] == hashMap[0]:
                return False
            return True

        def setHashMap(charList, permutation):
            # print(hashMap)
            for i, c in enumerate(charList):
                if hashMap[permutation[i]] == '':
                    hashMap[permutation[i]] = c
                else:
                    return False
            return True

        def unsetHashMap(charList, right_set, right):
            for c in charList:
                if c in hashMap:
                    hashMap[hashMap.index(c)] = ''
            if not right_set and right in hashMap:
                hashMap[hashMap.index(right)] = ''

        def checkCondition(i, balance):
            left = conditions[i][0]
            right = conditions[i][1]

            sum = balance
            for c in left:
                sum += hashMap.index(c)

            if len(right) > 0 and right[0] not in hashMap and hashMap[sum % 10] == '':
                hashMap[sum % 10] = right[0]
                return [int(sum / 10), True]

            if len(right) > 0 and right[0] in hashMap and (sum % 10) == hashMap.index(right[0]):
                return [int(sum / 10), True]

            return [0, False]

        def charsList(left):
            chars = set()
            for c in left:
                if c not in hashMap:
                    chars.add(c)

            return list(chars)

        return possiblePermutations(0, 0)
