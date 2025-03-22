from textnode import *
def main():

    print ("hello world")
    Node1 = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    Node2 = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print (Node1.__repr__())

main()