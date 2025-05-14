/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* l) {
   if(l==NULL || l->next == NULL) return l;
    
    int temp=l->val;
    l->val=l->next->val;
    l->next->val=temp;

    swapPairs(l->next->next);

    return l;
}