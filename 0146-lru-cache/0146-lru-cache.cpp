struct Node{
    int val;
    int key;
    Node* next;
    Node* prev;
    Node(): val(0), next(nullptr), prev(nullptr){}
    Node(int x): val(x), next(nullptr), prev(nullptr){}
    Node(int x, Node* next, Node* prev): val(x), next(next), prev(prev){}
};

class LRUCache {
private:
    int sz;
    int cap;
    Node* head;
    Node* tail;
    unordered_map<int, Node*> map;
public:
    LRUCache(int capacity) {
        cap = capacity;
        head = new Node();
        tail = new Node();
        head -> next = tail;
        tail -> prev = head;
        sz = 0;
    }
    
    int get(int key) {
        if(map.find(key) != map.end()){
            map[key]->prev->next = map[key] -> next;
            map[key]->next->prev = map[key] -> prev;
            map[key]->prev = head;
            map[key]->next = head -> next;
            head->next->prev = map[key];
            head->next = map[key];
            return map[key]->val;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if(map.find(key) != map.end()){
            map[key]->prev->next = map[key] -> next;
            map[key]->next->prev = map[key] -> prev;
            map[key]->prev = head;
            map[key]->next = head -> next;
            head->next->prev = map[key];
            head->next = map[key];
            map[key] -> val = value;
        }
        else{
            sz++;
            Node* n = new Node(value, head->next, head);
            n -> key = key;
            head->next->prev = n;
            head->next = n;
            map[key] = n;
            if(sz > cap){
                map.erase(tail -> prev -> key);
                tail -> prev -> prev -> next = tail;
                tail -> prev = tail -> prev -> prev;
                sz--;
            }
        }
        
        
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */