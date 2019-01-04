def save_to_file(content, filename):
    with open(filename, 'w') as f:
        data.write(content)

def read_file(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        return data

print('Module.py', __name__)

