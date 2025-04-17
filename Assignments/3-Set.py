'''
1. Pirate's Treasure Map:  
   A pirate's treasure map is stored as a list of lists:  
   map = [['G', 'X', 'X'], ['X', 'T', 'X'], ['X', 'X', 'S']]  
   Slice the map to extract only the treasure "T" and the symbols around it in a 3x3 grid.
   Modify the map to replace "T" with a treasure chest symbol "$".
'''
map = [['G', 'X', 'X'], ['X', 'T', 'X'], ['X', 'X', 'S']]

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 'T':
            sliced_map = [row[max(0, j-1):min(len(row), j+2)] for row in map[max(0, i-1):min(len(map), i+2)]]
            # Modifying the map to replace 'T' with '$'
            map[i][j] = '$'

print("Original Map:")
for row in map:
    print(row)

print("\nSliced Map around 'T':")
for row in sliced_map:
    print(row)


'''
2. Mutation in an Alien Code:  
   An alien code uses a list alien_code = ['A', 'B', ['X', 'Y'], 'C'].
   The alien wants to mutate the inner list ['X', 'Y'] to ['P', 'Q'].  
   - Write the mutated alien code.  
   - Slice the modified list to get only ['B', 'C'].
'''
alien_code = ['A', 'B', ['X', 'Y'], 'C']
alien_code[2] = ['P', 'Q']
print(alien_code[2])

print(alien_code[1], alien_code[3])


'''
3. Split the Train Cars:  
   A train is represented as train = [101, 102, [103, 104], 105].  
   - Slice the train to get only the middle two cars.  
   - Mutate the inner list [103, 104] to include car 106 after 104.
'''
train = [101, 102, [103, 104], 105]
print(train[2])

train[2].append(106)
print(train)


'''
4. Nested List of Villages:  
   Given a list of village populations:  
   villages = [[120, 80], [150, 90], [200, 300]].  
   Slice the list to get only the populations of the second and third villages.  
   Mutate the first village population by increasing each value by 10.
'''
villages = [[120, 80], [150, 90], [200, 300]]
print(villages[1], villages[2])

villages[0][0] += 10
villages[0][1] += 10
print(villages)


'''
5. Extracting a Torn Map:  
   A torn piece of the pirate map is stored as a nested list:  
   map_piece = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']].  
   - Slice to extract only the diagonal elements ['A', 'E', 'I'].  
'''
map_piece = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
print(map_piece[0][0], map_piece[1][1], map_piece[2][2])


'''
6. Lost Pages of the Codex:  
   A set of pages found in a lost codex is pages = {'A1', 'B2', 'C3'}.  
   - Mutate the set to add new pages {'D4', 'E5'}.  
   - Slice the first two elements from the sorted version of the set.
'''
pages = {'A1', 'B2', 'C3'}
pages.update({'D4', 'E5'})
print(pages)

print(sorted(pages)[:2])


'''
7. Joining Rare Ingredients:  
   Two sets of rare ingredients for a potion are given:  
   ingredients1 = {'eye_of_newt', 'frog_leg'}  
   ingredients2 = {'bat_wing', 'frog_leg'}  
   - Join the sets and find only the common ingredients.
'''
ingredients1 = {'eye_of_newt', 'frog_leg'}
ingredients2 = {'bat_wing', 'frog_leg'}
print(ingredients1.intersection(ingredients2))


'''
8. Breaking the Cipher:  
   A cipher key uses unique symbols:  
   key_part1 = {'$', '#', '@'}  
   key_part2 = {'$', '&', '%'}  
   - Mutate key_part1 to include the symbols from key_part2.  
   - Find the symbols that are only in key_part1 after mutation.
'''
key_part1 = {'$', '#', '@'}
key_part2 = {'$', '&', '%'}
key_part1.update(key_part2)
print(key_part1)

print(key_part1.difference(key_part2))


'''
9. Forest Mushroom Hunt:  
   Two sets of mushroom locations are given:  
   locations1 = {101, 102, 103}  
   locations2 = {102, 104, 105}  
   - Find all unique mushroom locations.  
   - Mutate locations2 to add a new location 106.
'''
locations1 = {101, 102, 103}
locations2 = {102, 104, 105}

print(locations1.union(locations2))

locations2.add(106)
print(locations2)


'''
10. Magical Token Sets:  
    A wizard's token collection is represented as two sets:  
    setA = {'fire', 'water'}  
    setB = {'earth', 'fire'}  
    - Join the two sets to find all magical tokens.  
    - Slice the set to keep only the tokens starting with 'f'.
'''
setA = {'fire', 'water'}
setB = {'earth', 'fire'}
print(setA.union(setB))

print(setA.intersection(setB))


'''
11. Ancient Scroll Pieces:  
    An ancient scroll is represented as a tuple:  
    scroll = ('A', ('B', 'C', 'D'), 'E').  
    - Slice the tuple to extract only ('B', 'C', 'D').  
    - Reassemble the scroll by replacing 'C' with 'Z'.
'''
scroll = ('A', ('B', 'C', 'D'), 'E')
print(scroll[1])

scroll1 = list(scroll[1])
print(scroll1)
scroll1[1] = 'Z'
scroll1 = tuple(scroll1)

scroll = list(scroll)
scroll[1] = scroll1
print(tuple(scroll))


'''
12. Mystic Necklace Stones:  
    A mystic necklace contains stones represented as a tuple:  
    necklace = ('ruby', ('emerald', 'sapphire'), 'diamond').  
    - Slice the tuple to extract only 'emerald' and 'sapphire'.  
'''
necklace = ('ruby', ('emerald', 'sapphire'), 'diamond')
print(necklace[1])


'''
13. Treasure Chest Locks:  
    A tuple of lock codes is given:  
    locks = (1001, (2002, 3003), 4004)  
    - Slice to get the second lock code 2002.  
    - Try to mutate 2002 to 2005 and explain the result.
'''
locks = (1001, (2002, 3003), 4004)
print(locks[1][0])

# locks[1][0] = 2005
# TypeError: 'tuple' object does not support item assignment
# tuples are immutable so we can't update 2002 to 2005.


'''
14. Frozen Lake Coordinates:  
    Coordinates of a frozen lake are stored as a nested tuple:  
    lake = ((0, 0), (1, 2), (2, 3), (3, 4)).  
    - Slice the tuple to get the last two coordinates.  
'''
lake = ((0, 0), (1, 2), (2, 3),(3, 4))
print(lake[-2:])


'''
15. Combining Token Tuples:  
    Two sets of tokens are represented as tuples:  
    tokens1 = ('alpha', 'beta')  
    tokens2 = ('gamma', 'delta')  
    - Join the tuples and slice the result to get only 'beta' and 'gamma'.
'''
tokens1 = ('alpha', 'beta')
tokens2 = ('gamma', 'delta')
t = tokens1 + tokens2
print(t[1:3])