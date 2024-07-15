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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* aptr = list1;
        int i = 0;
        for(; i < a - 1; i++){
            aptr = aptr->next;
        }
        ListNode* bptr = aptr;
        for(; i <= b; i++){
            bptr = bptr->next;
        }
        aptr->next = list2;
        while(aptr->next){
            aptr = aptr->next;
        }
        aptr->next = bptr;
        return list1;
    }   
};      