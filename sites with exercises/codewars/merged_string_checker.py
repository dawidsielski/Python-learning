"""
At a job interview, you are challenged to write an algorithm to check if a given string, s, can be formed from two other strings, part1 and part2.

The restriction is that the characters in part1 and part2 are in the same order as in s.

The interviewer gives you the following example and tells you to figure out the rest from the given test cases.

For example:

'codewars' is a merge from 'cdw' and 'oears':

    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears
"""

def is_merge(s, part1, part2):
    a = list(part1)
    b = list(part2)
    a.extend(b)
    return(sorted(a) == sorted(list(s)))


print(is_merge('codewars', 'code', 'wars'))
print(is_merge('codewars', 'cdw', 'oears'))
print(not is_merge('codewars', 'cod', 'wars'))
print(is_merge("codewars", "cwdr", "oeas"))