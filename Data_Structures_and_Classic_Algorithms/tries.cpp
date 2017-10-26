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


using namespace std;

TrieNode::TrieNode() {}

TrieNode::~TrieNode() {
  for(auto const& it : m_children)
    delete it;
}

TrieNode* TrieNode::findChild(char c) {
  for(auto const& it : m_children) {
    if(it->getContent() == c)
      return it;
  }

  return NULL;
}

Trie::Trie() {
  root = new TrieNode();
}

Trie::~Trie() {
  delete root;
}

void Trie::addWord(string s) {
  TrieNode* curr = root;
  if(s.length() == 0) {
    curr->setWordMarker();
    return;
  }

  for(int i = 0; i < s.length(); i++) {
    TrieNode* child = curr->findChild(s[i]);
    if(child != NULL) {
      curr = child;
    } else {
      TrieNode* tmp = new TrieNode();
      tmp->setContent(s[i]);
      curr->appendChild(tmp);
      curr = tmp;
    }

    if(i == s.length() - 1)
      curr->setWordMarker();
  }
}

bool Trie::searchWord(string s) {
  TrieNode* curr = root;

  while(curr != NULL) {
    for(int i = 0; i < s.length(); i++) {
      TrieNode* tmp = curr->findChild(s[i]);
      if(tmp == NULL)
        return false;
      curr = tmp;
    }

    if(curr->getWordMarker())
      return true;
    else
      return false;
  }

  return false;
}
