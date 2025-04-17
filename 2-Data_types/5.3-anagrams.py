# check for Anagrams

s1 = (input('Enter first string: ').lower()).strip()
s2 = (input('Enter second string: ').lower()).strip()

s3 = sorted(s1)
s4 = sorted(s2)

if s3 == s4:
    print(f'{s1} and {s2} are Anagrams.')
else:
    print(f'{s1} and {s2} are not Anagrams.')

# Enter first string: silent
# Enter second string: listen
# silent and listen are Anagrams.