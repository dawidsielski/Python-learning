import os, datetime, re

print(os.getcwd())
os.chdir("/Users/Dawid/Google Drive/Multimodal Multitouch Interactive Surfaces/Microsoft Surface/Input lag measurements/Click/pomiar 20")
print(os.getcwd())

directory_files_names = os.listdir()

time_stamp = []
for element in directory_files_names:
    # print(element)
    if "Image" in element:
        filename = re.findall(r"\d{4}_\d{2}_\d{2}_\d{6},\d{3}", element)
        without_underscore = (filename[0].split("_"))
        without_comma = (without_underscore[-1].split(","))
        x = without_underscore[:-1]
        # print(without_comma)
        date = [without_comma[0][:2], without_comma[0][2:4], without_comma[0][4:6]]
        # print(date)
        x.extend(date)
        x.extend([without_comma[-1]])
        print(x)
        time_stamp.append(x)


date1 = datetime.datetime(*(list(map(int, time_stamp[0]))))
# date2 = datetime.datetime((time_stamp[-1]))

print(date1)