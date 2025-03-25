class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq

        self.left = None
        self.right = None

def build_huffman_tree(text):
    freq_map = {}
    for char in text:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1

    nodes = [Node(char, freq) for char, freq in sorted(freq_map.items(), key=lambda x: x[1])]

    while len(nodes) > 1:
        left = nodes.pop(0)
        right = nodes.pop(0)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        nodes.append(merged)
        nodes.sort(key=lambda x: x.freq)

    return nodes[0]

def build_huffman_codes(root, code='', huffman_dict={}):
    if root:
        if root.char is not None:
            huffman_dict[root.char] = code

        build_huffman_codes(root.left, code + '0', huffman_dict)
        build_huffman_codes(root.right, code + '1', huffman_dict)

        return huffman_dict

def huffman_encode(text):
    if not text:
        return "", {}

    root = build_huffman_tree(text)
    huffman_dict = build_huffman_codes(root)

    encoded_text = ''.join(huffman_dict[char] for char in text)

    return encoded_text, huffman_dict

def huffman_decode(encoded_text, huffman_dict):
    reversed_dict = {v: k for k, v in huffman_dict.items()}

    decoded_text = ""
    buffer = ""
    for bit in encoded_text:
        buffer += bit
        if buffer in reversed_dict:
            decoded_text += reversed_dict[buffer]
            buffer = ""

    return decoded_text

def main():
    text = input("input text to encode:\n")

    encoded_text, huffman_dict = huffman_encode(text)

    print("encoded text")
    print(encoded_text)
    print("codes:")
    print(huffman_dict)

    decoded_text = huffman_decode(encoded_text, huffman_dict)
    print("decoded text:")
    print(decoded_text)

if __name__ == "__main__":
    main()
