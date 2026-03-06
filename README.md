# Programming Assignment 2

Name: Zarraf Rayan UFID: 8963 2275

The example input and output is found in the files folder where there are 3 example input files and corresponding 3 example output files

Assumptions:
The input file is formatted according to the programming 2 assignments instructions.

Instructions to reproduce the output:
1) Make sure you are in the src folder 
2) Make sure you have the filepath ready for the input file
3) Run this command in the terminal:```py evictions.py \<filePath>```
   For example: ```py evictions.py ../files/example1.in``` will reproduce the output for example1.in (shown in example1.out)

Answers to the three questions will be found in the PDF titled "answers.pdf" and also this README since it is a requirement.

Programming Assignment 2

Question 1)
These files can be found in the files folder where File1, File2, and File3 correspond to
example1.in, example2.in, and example3.in.
Input File k m FIFO LRU OPTFF
File1 12 50 31 30 22
File2 9 50 41 41 25
File3 15 50 30 28 23
Brief Comments:
- OPTFF does have the fewest misses
- FIFO tends to have a bit more misses compared to LRU.

Question 2)
There exists a request sequence for which OPTFF incurs strictly fewer misses than LRU
reqs = {21, 4, 1, 24, 9, 8, 8, 5, 24, 4, 22, 24, 18, 3, 19, 14, 2,1, 3, & 7}
Missed Counts Computation
FIFO : 16
LRU : 16
OPTFF : 12
I think there exists a request sequence for which OPTFF incurs strictly fewer misses than
LRU because all the examples I came up with had OPTFF incurring less misses than the
other two cache eviction policies, which leads me to believe it is more optimal.

Question 3)
Let OPTFF be Belady’s Farthest-in-Future algorithm.
Let ( A ) be any offline algorithm that knows the full request sequence.
Claim: the number of misses of OPTFF is no larger than that of ( A ) on any fixed sequence.
(i.e. Misses(OPTFF) ≤ Misses(A))
Assumptions:
- The offline algorithm A has the optimal (or in this case minimum) number of cache
misses for the full request sequence
Proof by Exchange Theorem:
- Let B = OPTFF or Belady’s Farthest-In-Future Algorithm
- Consider a list of requests R = {r1, r2, r3, … rk}
- Let X be the cache for A (the offline algorithm) and Y be cache for OPTFF
- Consider that up to some request ri, the two algorithms produce the same eviction
schedule (i.e. steps in A= steps in B until ri+1)
- Consider the (i+1)th request ri+1 , in which X and Y share the same contents since
their eviction schedules are the same up until this point
- Case 1: ri+1 is already in the cache in which case neither A or B have to evict anything
- Case 2: ri+1 is not in the cache but both algorithms A and B evict the same thing, in
which case we X=Y again since we replace the same item with request ri+1 .
- Case 3: ri+1 is not in the cache but algorithm A evicts some item c and while
algorithm B evicts some item d, s.t. c≠d.
- Since B evicts the item that is requested furthest in the future, we know that
the time when d is requested is after or at the same time when cis
requested. (i.e. TimeOfNextRequest(c) ≤ TimeOfNextRequest(d))
- So currently X contains c but not d and Y contains d but not c
- If we continue through the sequence of requests until c is requested (which
occurs first as mentioned above)
- Cache X (corresponding to A) occurs a cache miss since it doesn’t have c
- Cache Y (corresponding to B)occurs a hit since it does contain c
- Since X incurred a miss and Y didn’t, replacing the eviction choice of A with B
(OPTFF) algorithm doesn’t increase number of misses. Transforming X back into Y
(i.e. X=Y once again)
- Repeat the argument for case 3 every time the algorithm A and B decide to evict
different items until the requests are all processed and X = Y.
- Since can transform the cache X (gotten from A) into Y (gotten from OPTFF) without
increasing number of misses -> (Misses(OPTFF) ≤ Misses(A))
