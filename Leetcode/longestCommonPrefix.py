def longestCommonPrefix(strs):
    if not strs:
        return ""

    min_length = min(len(s) for s in strs)
    result = []

    for i in range(min_length):
        current_char = strs[0][i]
        if all(s[i] == current_char for s in strs[1:]):
            result.append(current_char)
        else:
            break

    return "".join(result)


print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["interspecies","interstellar","interstate"]))
print(longestCommonPrefix(["throne","throne"]))
print(longestCommonPrefix(["throne","dungeon"]))