# PhoneBook
In this implementation, the TRIE data structure is used to store the contacts in the phone book. The PhoneBook class contains a root instance variable that represents the root of the TRIE. The TRIE is made up of TrieNode objects, which are stored as attributes of each other to form a hierarchical structure.

The TrieNode class represents a node in the TRIE. Each TrieNode has a children dictionary that maps characters to child nodes. Each child node is also a TrieNode. Each TrieNode has a is_word attribute, which is True if the node represents the end of a word (i.e., a contact name), and a number attribute, which contains the phone number associated with the word represented by the node.

The PhoneBook class contains a root instance variable, which represents the root of the TRIE. The insert method is used to add a new contact to the phone book. It iterates over each character in the name, and creates a new TrieNode for each character that doesn't already exist. It then sets the is_word attribute of the final node to True, and sets the number attribute to the phone number associated with the contact.

The search method is used to look up a contact by name. It iterates over each character in the name, following the child nodes of the current node for each character. If a character is encountered that doesn't have a corresponding child node, the search terminates and returns None. If the search reaches a node with is_word set to True, it returns the number attribute of that node, which is the phone number associated with the contact.

Overall, the TRIE data structure provides an efficient way to store and search for contacts by name in the phone book. By storing the contacts in a hierarchical structure, the search can quickly traverse the TRIE to find the desired contact.
