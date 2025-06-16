/**
 * A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
 *
 * Implement the Trie class:
 *
 * Trie() Initializes the trie object.
 * void insert(String word) Inserts the string word into the trie.
 * boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
 * boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 *
 *
 * Example 1:
 *
 * Input
 * ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
 * [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
 * Output
 * [null, null, true, false, true, null, true]
 *
 * Explanation
 * Trie trie = new Trie();
 * trie.insert("apple");
 * trie.search("apple");   // return True
 * trie.search("app");     // return False
 * trie.startsWith("app"); // return True
 * trie.insert("app");
 * trie.search("app");     // return True
 *
 *
 * Constraints:
 *
 * 1 <= word.length, prefix.length <= 2000
 * word and prefix consist only of lowercase English letters.
 * At most 3 * 104 calls in total will be made to insert, search, and startsWith.
 */


class Trie {

    private TrieNode root;
    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode node = this.root;
        for(char ch : word.toCharArray()) {
            if (!node.contains(ch)) {
                node.put(ch, new TrieNode());
            }
            node = node.get(ch);
        }
        node.setEnd();
    }

    public TrieNode prefixSearch(String word) {
        TrieNode node = this.root;
        for (char ch : word.toCharArray()) {
            if(node.contains(ch)) {
                System.out.println("Char is in Prefix: " + ch);
                node = node.get(ch);
            } else{
                System.out.println("Char is not in Prefix: " + ch);
                return null;
            }
        }
        return node;
    }

    public boolean search(String word) {
        TrieNode node = prefixSearch(word);
        return node != null && node.isEnd();
    }

    public boolean startsWith(String prefix) {
        TrieNode node = prefixSearch(prefix);
        return node != null;
    }
}

class TrieNode {
    private final int count = 26;
    private TrieNode[] links;
    private boolean end;

    public TrieNode() {
        this.links = new TrieNode[count];
    }

    public void put(char ch, TrieNode node) {
        this.links[ch - 'a'] = node;
    }

    public boolean contains(char ch) {
        return this.links[ch - 'a'] != null;
    }

    public TrieNode get(char ch) {
        return this.links[ch - 'a'];
    }

    public boolean isEnd() {
        return this.end;
    }

    public boolean setEnd() {
        return this.end = true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */