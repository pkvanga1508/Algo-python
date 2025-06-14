# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def pre_order(self, root, serialize_str):
        if not root:
            serialize_str += "null,"
        else:
            serialize_str += str(root.val) + ","
            serialize_str = self.pre_order(root.left, serialize_str)
            serialize_str = self.pre_order(root.right, serialize_str)
        return serialize_str

    def serialize(self, root):
        string_val = self.pre_order(root, "")
        print(string_val)
        return string_val


    def str_to_tree(self, tokens):  #We Tokenize the serialize_str
        if tokens[0] == "null": #Original tree is None
            return None

        root = TreeNode(int(tokens[0]))
        tokens.pop(0) #remove that token
        root.left = self.str_to_tree(tokens)
        root.right = self.str_to_tree(tokens)
        return root



    def deserialize(self, data):
        tokens = data.split(',')
        print(tokens)
        return self.str_to_tree(tokens)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))