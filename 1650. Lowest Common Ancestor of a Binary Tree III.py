# 1650. Lowest Common Ancestor of a Binary Tree III
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pHead, qHead = p, q
        
        '''
         a + c     -> p [...a nodes] [convergent] [...c nodes]
         b + c     -> q [...b nodes] [convergent] [...c nodes]
         
         a + c + b -> p [...a nodes] [convergent] [...c nodes]
                      q [...b nodes] 

         b + c + a -> q [...b nodes] [convergent] [...c nodes]
                      p [...a nodes] 
        
         After both p & q moves a + c + b steps, it will reach the convergent node
         p can move a + c by going to root, and move b by begining from q
         q is vice versa.
         
         so...switch the begining node after each of them encounter the root
         
        '''
        
        while p != q:
            q = q.parent if q else pHead
            p = p.parent if p else qHead
        
        return p

        