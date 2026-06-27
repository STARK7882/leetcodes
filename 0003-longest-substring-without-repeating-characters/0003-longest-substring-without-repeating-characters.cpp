class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0;
        int right = 0;

        int length = s.size();

        int maxi =0;

        unordered_map<char,int> mpp;
        int maxCount = 0;
        while(right < length)
        {
           if(mpp.find(s[right])==mpp.end())
           {
                mpp[s[right]]++;
                maxi = max(maxi,right-left+1);
                right++;
           }
           else
           {
                mpp[s[left]]--;
                if(mpp[s[left]]==0)
                {
                    mpp.erase(s[left]);
                }
                left++;
           }
        }
        return maxi;
    }
};