/**
 * Design a data structure that supports adding new words and finding if a string matches any previously added string.
 *
 * Implement the WordDictionary class:
 *
 * WordDictionary() Initializes the object.
 * void addWord(word) Adds word to the data structure, it can be matched later.
 * bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 *
 *
 * Example:
 *
 * Input
 * ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
 * [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
 * Output
 * [null,null,null,null,false,true,true,true]
 *
 * Explanation
 * WordDictionary wordDictionary = new WordDictionary();
 * wordDictionary.addWord("bad");
 * wordDictionary.addWord("dad");
 * wordDictionary.addWord("mad");
 * wordDictionary.search("pad"); // return False
 * wordDictionary.search("bad"); // return True
 * wordDictionary.search(".ad"); // return True
 * wordDictionary.search("b.."); // return True
 *
 *
 * Constraints:
 *
 * 1 <= word.length <= 25
 * word in addWord consists of lowercase English letters.
 * word in search consist of '.' or lowercase English letters.
 * There will be at most 2 dots in word for search queries.
 * At most 104 calls will be made to addWord and search.
 */


class WordDictionary {

    TrieNode root;

    public WordDictionary() {
        root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode node = root;
        for(char ch : word.toCharArray()){
            if(!node.getChildren().containsKey(ch)) {
                node.getChildren().put(ch, new TrieNode());
            }
            node = node.getChildren().get(ch);
        }
        node.setEnd();
    }

    public boolean prefixSearch(String word, TrieNode root) {
        TrieNode node = root;
        for (int index = 0; index < word.length(); index++) {
            char ch = word.charAt(index);
            if(!node.getChildren().containsKey(ch)) {
                if(ch == '.') {
                    for(TrieNode childNode : node.getChildren().values()) {
                        String sufix = word.substring(index + 1);
                        if(prefixSearch(sufix, childNode)) { //return true if word is in the sufix and child node.
                            return true;
                        }
                    }
                } else {
                    return false;
                }
            } else {
                node = node.getChildren().get(ch);
            }
        }
        return node.getEnd();
    }

    public boolean search(String word) {
        return prefixSearch(word, this.root);
    }
}

class TrieNode {

    private Map<Character, TrieNode> children;
    private boolean end;

    public TrieNode() {
        this.children = new HashMap<>();
    }

    public Map<Character, TrieNode> getChildren() {
        return this.children;
    }

    public void setEnd() {
        this.end = true;
    }

    public boolean getEnd() {
        return this.end;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */