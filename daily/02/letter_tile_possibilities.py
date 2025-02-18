# 17/2/25
# https://leetcode.com/problems/letter-tile-possibilities/

def numTilePossibilities(tiles: str) -> int:
    def backtrack(t: str) -> set[str]:
        if len(t) == 1:
            return set({ t })
        
        l = t[0]
        tile_set = backtrack(t[1:])

        # A new set is initialised with 'l' to prevent
        # concurrent modification.
        additions: set[str] = set({ l })
        for tile in tile_set:
            for i in range(len(tile) + 1):
                additions.add(tile[:i] + l + tile[i:])

        tile_set |= additions

        return tile_set

    tile_seq = backtrack(tiles)
    return len(tile_seq)

print(numTilePossibilities("AAB"))
print(numTilePossibilities("V"))
print(numTilePossibilities("AAABBC"))
print(numTilePossibilities("ABCDEFG"))