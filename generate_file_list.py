import os
import yaml

def generate_file_list(directory, output_file):
    file_data = {'images': [], 'videos': []}

    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            file_data['images'].append(filename)
        elif filename.endswith('.MOV'):
            file_data['videos'].append(filename)

    with open(output_file, 'w') as outfile:
        yaml.dump(file_data, outfile, default_flow_style=False)

if __name__ == "__main__":
    generate_file_list('images/tri3natm', '_data/files.yml')
