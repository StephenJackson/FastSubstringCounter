
# first we take the length of the input string. Then we subtract from that the length
# of the same string without any instances of the substring
# (we split out the substring and then rejoin the result).
# then we divide the difference by the length of the substring.
# the quotient is the number of times that substring occurs in input string.
def substring_counter(string_in, sub_string):
  if sub_string:
    return (len(string_in) - len("".join(string_in.split(sub_string)))) / len(sub_string)
  else:
    return 0