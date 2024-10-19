class TODO:
    def __init__(self, list = []):
        self.list = list

    def add_item(self, item):
        self.list.append(item)

    def display_list(self, isReverseSorted=False):
        print(sorted(self.list, key=lambda i:i['color'], reverse=isReverseSorted))

todo = TODO()
todo.add_item({'color': 'black'})
todo.add_item({'color': 'blue'})
todo.display_list(True)