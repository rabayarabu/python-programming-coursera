# 6.5 Write code using find() and string slicing (see section 6.10)
# to extract the number at the end of the line below. Convert the 
# extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
# find the starting of float number
start_pos = text.find(':')
# remove the whitespace before the float number
number_str = text[start_pos+1:].strip()
# convert string into float number
float_number = float(number_str)
# print the float number that found
print(float_number)
