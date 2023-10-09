# Task1
f = open('hw_10_test.txt', 'r', encoding='utf-8')
for line in f:
    print(line.strip())
    line.split()
# Task2
def find_info(id):
    for line in f:
        line.strip()
        get_ready = line.split()
        if id == get_ready[0]:
            return f"id: {id}\ninfo: {get_ready[1]} {get_ready[2]}, {get_ready[3]}"

func = find_info("23")
print(func)

# Task3

def find_by_name(username, file_name):
    all_users = []
    with open(file_name, 'r') as f:
        for line in f:
            line.strip()
            text = line.split()
            if username == text[1]:
                info = text[0:]
                all_users.append(info)
                return all_users


func = find_by_name("Bob", "hw_10_test.txt")
print(*func)
