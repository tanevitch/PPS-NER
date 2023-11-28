import os

folder_path = "./pruebas"
output_file_path = "combined_output.txt"

file_list = os.listdir(folder_path)
combined_content = ""
for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)

    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding="utf8") as file:
            content = file.read()
            content = content.replace('\n', '. ')
            combined_content += content + "^"
            # content = content.replace('-', '')
            # content = content.replace('  ', '')
            # content = content.replace('         ', ' ')
            # content = content.replace('*', '')
            # print(f"Contents of {file_name}:")
            # print(content)
            # print("\n" + "-"*30 + "\n")
with open(output_file_path, 'w', encoding="utf8") as output_file:
    output_file.write(combined_content)