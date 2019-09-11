volume_max = 1000
volume_min = 0

volume_data = 500
volume_range = volume_max - volume_min
volume_section = 5

if volume_range < 0:
    # at 0% volume
    if volume_data <= (volume_range/5):
        print("volume at 0%-20%")
    # at 20% volume
    if volume_data > (volume_range/5) and volume_data <= (volume_range/5)*2:
        print("volume at 20%-40%")
    # at 40% volume
    if volume_data > (volume_range/5)*2 and volume_data <= (volume_range/5)*3:
        print("volume at 40%-60%")
    # at 60% volume
    if volume_data > (volume_range/5)*3 and volume_data <= (volume_range/5)*4:
        print("volume at 60%-80%")
    # at 100% volume
    if volume_data > (volume_range / 5)*4:
        print("volume at 80%-100%")




#
#
# # at 40% volume
# if volume_data <= (volume_range/5)*2:
#     print("volume at 20%")
# if volume_data > (volume_range/5)*2 and volume_data <= (volume_range/5)*2:
#     print("volume at 40%")
#
# # at 60% volume
# if volume_data <= (volume_range/5)*3:
#     print("volume at 40%")
# if volume_data > (volume_range/5)*3:
#     print("volume at 60%")
#
# # at 80% volume
# if volume_data <= (volume_range/5)*4:
#     print("volume at 60%")
# if volume_data >= (volume_range/5)*4:
#     print("volume at 80%")
#
# # at 100% volume
# if volume_data <= (volume_range/5)*5:
#     print("volume at 80%")
# if volume_data >= (volume_range/5)*5:
#     print("volume at 100%")

b=b'hello'
a = [b'123',b'a',b'234',b'778']
xb=[]
for x in a:
	try:
		decoded_val = x.decode("utf-8")
		if decoded_val=="a":
			print(decoded_val)
		elif int(decoded_val):
			print(decoded_val)
		else:
			print("n")
		# print(int(decoded_val))
	except ValueError as e:
		print(e)