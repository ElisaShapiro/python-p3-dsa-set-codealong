class MySet:
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
    def has(self, value):
        return value in self.dictionary
    def add(self, value):
        self.dictionary[value] = True
        return self
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    def size(self):
        return len(self.dictionary)
    def clear(self):
        self.dictionary.clear()
    def __str__(self):
        list_of_items = []
        for key, value in self.dictionary.items():
            list_of_items.append(str(key))
        return f'MySet: {{{",".join(list_of_items)}}}'