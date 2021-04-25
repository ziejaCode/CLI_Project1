import sys

# this will print all arguments 
#print(sys.argv)

def sayHello(name):
    print("Hello {}".format(name))

def sayGoodbye(name):
    print("Goodbye {}".format(name))

command = sys.argv[1]

if command == "hello":
    sayHello(sys.argv[2])
elif command == "goodbye":
    sayGoodbye(sys.argv[2])