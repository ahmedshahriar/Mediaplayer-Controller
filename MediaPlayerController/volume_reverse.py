volume_max = 0
volume_min = 1000

volume_data = 801
volume_range = volume_min - volume_max
volume_section = 5

print(volume_range)
# at 100% volume
if volume_data < (volume_range/5):
    print("volume at 80%-100%")
# at 80% volume
if volume_data > (volume_range/5) and volume_data <= (volume_range/5)*2:
    print("volume at 60%-80%")
# at 60% volume
if volume_data > (volume_range/5)*2 and volume_data <= (volume_range/5)*3:
    print("volume at 40%-60%")
# at 40% volume
if volume_data > (volume_range/5)*3 and volume_data <= (volume_range/5)*4:
    print("volume at 20%-40%")
# at 20% volume
if volume_data  >= (volume_range / 5)*4:
    print("volume at 0%-20%")




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