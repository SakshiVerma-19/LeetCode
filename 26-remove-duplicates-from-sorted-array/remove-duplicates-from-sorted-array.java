class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;
        if (n==0) return 0;
        int k =0;
            for (int j=1;j<n;j++){
                if(nums[j]!=nums[k]) 
                    k++ ;                 
                    nums[k]=nums[j];
            }return k+1;
        }
        
        
        
    }
