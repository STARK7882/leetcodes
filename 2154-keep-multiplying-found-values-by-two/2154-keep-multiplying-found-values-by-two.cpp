class Solution {
public:


    bool search(vector<int>& nums,int k)
    {
        for (auto s: nums)
        {
            if(s==k)
                return true;
        }
        return false;
    }

    int findFinalValue(vector<int>& nums, int original) {
        
        bool found = true;
        int k =original;

        while (found)
        {
            found = search(nums,k);
            if (found)
            {
                k*=2;
            }
        }
        return k;
    }
};