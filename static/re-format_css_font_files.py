# This code gets all the font files that the css file includes
# It can replace the url of the css file to the correct file directory
import wget
print("\nImport of wget sucessful.")

chosen_file = str(input("\nInput the directory of the css file that you want to scan: "))

chosen_save_area = str(input("\nInput the directory for where the files should be downloaded to: "))

print("\nStarting read of css file...\n")

file_split = []
try:
    with open(chosen_file, "r") as f:
        content = f.read()
        lines = content.splitlines()
        for line in lines:
            print(line)
            file_split.append(line)

    print("\nFinished reading selected css file.")
except FileNotFoundError:
    print("\nCouldn't find specified css file!")
    print(chosen_file)

print("\nGetting file url links...\n")

found_links = []
file_names = []
for line in file_split:
    searched_file = line
    if "url(" in line:
        searched_file = searched_file.split("(")
        searched_file = searched_file[1]
        searched_file = searched_file.split(")")
        searched_file = searched_file[0]
        found_links.append(searched_file)

        searched_file = searched_file.split("/")
        searched_file = searched_file[-1]
        file_names.append(searched_file)

print(found_links)
print(file_names)

print("\nFinished getting file url links.")


print("\nBeginning file downloads...")

i = 0
while i != len(found_links) - 1:
    url = found_links[i]
    file_name = file_names[i]
    current_file_name = chosen_save_area + file_name
    wget.download(url, current_file_name)
    i = i + 1

print("\nCompleted all downloads.")

print("\nConverting css file url links...\n")

i = 0
while i != len(file_split) - 1:
    line = file_split[i]
    searched_file = line
    if "url(" in line: # src: url(https://fonts.gstatic.com/s/raleway/v22/1Ptug8zYS_SKggPNyCIIT5lu.woff2) format('woff2');
        searched_file = searched_file.split("(")
        searched_file = searched_file[1] # https://fonts.gstatic.com/s/raleway/v22/1Ptug8zYS_SKggPNyCIIT5lu.woff2) format('woff2');
        print(searched_file)
        searched_file = searched_file.split(")")
        searched_file = searched_file[0] # https://fonts.gstatic.com/s/raleway/v22/1Ptug8zYS_SKggPNyCIIT5lu.woff2
        print(searched_file)

        searched_file = searched_file.split("/")
        searched_file = searched_file[-1] # 1Ptug8zYS_SKggPNyCIIT5lu.woff2
        print(searched_file)


        joining = ["css-media", searched_file]
        joined = "/".join(joining) # css-media/1Ptug8zYS_SKggPNyCIIT5lu.woff2
        print(joined)


        joining = [joined, " format('woff2');"]
        joined = ")".join(joining) # css-media/1Ptug8zYS_SKggPNyCIIT5lu.woff2) format('woff2');
        print(joined)


        joining = ["src: url", joined]
        joined = "(".join(joining) # src: url(css-media/1Ptug8zYS_SKggPNyCIIT5lu.woff2) format('woff2');
        print(joined)

        file_split.pop(i)
        file_split.insert(i, joined)
        print(file_split)

    i = i + 1

chosen_css_file = open(chosen_file, "w")
text_to_write = "\n".join(file_split)
print(text_to_write)
chosen_css_file.write(text_to_write)
chosen_css_file.close()

print("\nFinished converting all url links in the file.")
print("\n\nAll completed!")
