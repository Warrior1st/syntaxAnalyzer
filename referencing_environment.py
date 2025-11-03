class Symbol:
    def __init__(self):
        self.type = ""
        self.name = ""
        self.value = ""


class SymbolTable:
    def __init__(self):
        self.symbols = [Symbol() for _ in range(MAX_SYMBOLS)]
        self.count = 0
        self.parent = None

    #Insere les symboles si y a de la place
    def insert(self, symbol_type, symbol_name, symbol_value):
        if self.count < MAX_SYMBOLS:
            self.symbols[self.count].type = symbol_type
            self.symbols[self.count].name = symbol_name
            self.symbols[self.count].value = symbol_value
            self.count += 1
            return True
        return False
    
    #Recherche; Pouvons nous faire mieux?
    def find(self, name):
        for i in range(self.count):
            if self.symbols[i].name == name:
                return self.symbols[i]
    
    def print_table(self):
        for i in range(self.count):
            print(f"  {self.symbols[i].type} {self.symbols[i].name} = {self.symbols[i].value}")

class Node:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.parent = None
        self.children = []


    def push_scope(self):
        new_node = Node()
        new_node.parent = self
        self.children.append(new_node)
        return new_node

    def pop_scope(self):
        if self.parent:
            return self.parent
        return self

    def print_current_scope(self):
        print("Current scope:")
        self.symbol_table.print_table()

    def print_all_scopes(self):
        current = self
        scope_level = 0
        
        while current:
            print(f"Scope level {scope_level}:")
            current.symbol_table.print_table()
            print()
            current = current.parent
            scope_level += 1

    def insert_symbol(self, symbol_type, symbol_name, symbol_value):
        return self.symbol_table.insert(symbol_type, symbol_name, symbol_value)

    def symbol_exists(self, name):
        current = self
        while current:
            if current.symbol_table.find(name):
                return current.symbol_table.find(name)
            current = current.parent

    
    def symbol_existsInCurrent(self, name):
        return self.symbol_table.find(name)


def free_environment(head):
    def cleanup(node):
        for child in node.children:
            cleanup(child)
        node.children.clear()
        node.parent = None
    
    cleanup(head)

MAX_SYMBOLS = 100

