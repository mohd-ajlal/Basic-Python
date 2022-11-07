# Program to input the number of overs in a Cricket match and output the maximum runs a
# player can score in the match. Assume that there are no extra runs or NO balls in the match
# played. For example, in a 50 over match, the maximum runs scored are 1653.

# Input Format
# The first line contains the number of overs in the match.
# The second line contains the number of runs in the match.
# The third line contains the maximum runs scored.

over = int(input("Enter the number of overs in the match: "))

# a batsman can score a maximum of 1653 runs from 300 balls (or fifty overs). Now, let’s see how: in every over from the first to the forty-ninth, the batsman must hit sixes off the first five deliveries and take three off the last. In other words, in each of the first 49 overs, the batsman must score 33 runs: 30 runs by sixes off the first five balls and three off the last ball. In the last over, the batsman will get to face all six balls without having to worry about retaining the strike. In other words, he can score 36 runs off the last over by six runs on every delivery. Thus, the batsman can score 1617 off the first 49 overs (49 multiplied by 33). We add 36 (scored in the 50th over) to that number and get the answer: 1617 plus 36 equals 1653.

total = ((over - 1) * 33) + 36


# Output Format


print(f"The maximum runs scored is {total}")
