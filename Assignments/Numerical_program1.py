#  1. Keith Number  
# A Keith number is a number that appears in a Fibonacci-like sequence where the initial terms are its digits.  
# Example: 197 → Sequence: 1, 9, 7, 17, 33, 57, 97, 187... (contains 197).  
# Write a function to check if a number is a Keith number.  



#  2. Disarium Number  
# A Disarium number is a number whose sum of digits powered with their position equals the number itself.  
# Example: 89 → \( 8^1 + 9^2 = 89 \).  
# Write a function to check if a number is a Disarium number.



#  3. Niven (Harshad) Number  
# A Niven number is a number that is divisible by the sum of its digits.  
# Example: 18 → \( 1 + 8 = 9 \), and \( 18 \div 9 = 2 \).  
# Write a function to check if a number is a Niven number.



#  4. Smith Number  
# A Smith number is a composite number whose sum of digits equals the sum of the digits of its prime factors.  
# Example: 666 → \( 6+6+6 = 18 \), and prime factors: \( 2, 3, 3, 37 \) → \( 2+3+3+3+7 = 18 \).  
# Write a function to check if a number is a Smith number.



#  5. Automorphic Number  
# An Automorphic number is a number whose square ends with the number itself.  
# Example: \( 25^2 = 625 \), so 25 is Automorphic.  
# Write a function to check if a number is Automorphic.



#  6. Kaprekar Number  
# A Kaprekar number is a number where its square, when split into two parts, sums to the original number.  
# Example: \( 45^2 = 2025 \), and \( 20 + 25 = 45 \).  
# Write a function to check if a number is a Kaprekar number.



#  7. Perfect Digital Invariant (Armstrong Number - Generalized)  
# A Perfect Digital Invariant is a number that is equal to the sum of its digits each raised to a fixed power p.  
# Example: \( 9474 \) for \( p=4 \) → \( 9^4 + 4^4 + 7^4 + 4^4 = 9474 \).  
# Write a function to check for a given p.



#  8. Harshad-Happy Number  
# A Harshad-Happy number is both a Harshad (Niven) number and a Happy number.  
# A Happy number is a number where the sum of the squares of its digits eventually equals 1.  
# Write a function to find Harshad-Happy numbers.



#  9. Circular Prime  
# A Circular prime is a prime number where all rotations of its digits are also prime.  
# Example: 197 → 197, 971, and 719 are all prime.  
# Write a function to check if a number is a Circular prime.



#  10. Lychrel Number  
# A Lychrel number is a number that does not form a palindrome even after repeated reversal and addition.  
# Example: 196 is a Lychrel candidate as it never forms a palindrome.  
# Write a function to check if a number is a Lychrel number (with a given iteration limit).



#  11. Carmichael Number  
# A Carmichael number is a composite number that satisfies Fermat's Little Theorem for all integers a coprime to it.  
# Write a function to check if a number is a Carmichael number.



#  12. Recurring Cycle in Decimal Fractions  
# Find the number between 1 and N that has the longest recurring cycle in its decimal fraction representation.  
# Example: \( 1/7 = 0.\overline{142857} \) (cycle length = 6).  
# Write a function to find the number with the longest recurring cycle.



#  13. Ulam Number  
# An Ulam number sequence starts with \( U_1 = 1, U_2 = 2 \), and each subsequent number is the smallest integer that is the sum of two distinct earlier Ulam numbers in only one way.  
# Find the first N Ulam numbers.



#  14. Truncatable Prime  
# A Truncatable prime is a prime number that remains prime when digits are removed one by one from left to right or right to left.  
# Example: 3797 is left-truncatable (797, 97, 7 are prime) and right-truncatable (379, 37, 3 are prime).  
# Write a function to check if a number is a Truncatable prime.



#  15. Pronic Number  
# A Pronic number (also called Rectangular number) is a number that is the product of two consecutive integers.  
# Example: 6 = \( 2 \times 3 \), 12 = \( 3 \times 4 \).  
# Write a function to check if a number is Pronic.
