'''
int main(){
    Pokemon p1("Pikachu", 5);
    Pokemon p2("Squirtle", 5);

    cout << p1;
    cout << p2;
}
'''

class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def getName(self):
        return self.name

    def getLevel(self):
        return self.level

    #print 연산자 오버로딩
    #magic method라고 한다.
    def __str__(self):
        #return "%s(%s)" %(str(self.name), str(self.level))
        #return "{}({})".format(self.name, self.level)
        return f"{self.name}({self.level})"


p1 = Pokemon("Pikachu", 5)
p2 = Pokemon("Squirtle", 3)



print(p1) # cout << p1
print(p2) # cout << p2

