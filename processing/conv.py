for i in range(13100,234201,50):
    with open(f'messages{i}.html', 'r') as file:
        with open(f'mmessages{i}.html', 'wb') as out:
            out.write(file.read().encode('utf-8'))
            print(i)