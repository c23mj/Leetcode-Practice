/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(head == nullptr) return nullptr;
        ListNode* curr = head;
        int sz = 1;
        while(curr -> next != nullptr){
            curr = curr -> next;
            sz++;
        }
        curr -> next = head;
        curr = head;
        for(int i = 0; i < sz - k%sz - 1; i++){
            curr = curr -> next;
        }
        ListNode* newHead = curr -> next;
        curr -> next = nullptr;
        return newHead;
        

        





    }
};