#include <string>
#include <vector>

class TrieNode {
    
    char m_content;
    bool m_marker;
    std::vector<TrieNode*> m_children;
    
  public:
    TrieNode();
    ~TrieNode();
    char getContent() { return m_content; }
    void setContent(char c) { m_content = c; }

    bool getWordMarker() { return m_marker; }
    void setWordMarker() {m_marker = true;}
    TrieNode* findChild(char c);
    void appendChild(TrieNode* child) { m_children.push_back(child); }
    std::vector<TrieNode*> children() { return m_children; }
};


class Trie { 

    TrieNode* root;

  public:
    Trie();
    ~Trie();
    void addWord(std::string s);
    bool searchWord(std::string s);
};
