# prime_number_finder  
A fun project exploring the world of prime numbers and their relationship with composite numbers.  

## Algorithmic optimizations to check if current_number is a prime number
(1) Assuming we know all the prime numbers smaller than current_number, we can use dynamic programming to only consider prime numbers as possible denominators.
(2) Skip all even-number candidates.
(3) Only check for possible denominators in the range of [3, sqrt(current_number)].

## Interesting "discovery"
The composite : prime ratio increases very slowly. When we got to the tens of millions, that ratio was still at around 20:1. It does increase fairly consistently though.   
