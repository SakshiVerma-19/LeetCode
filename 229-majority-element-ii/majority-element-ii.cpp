class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> ls;
        map<int, int> map;
        int n = nums.size();
        int min = (n / 3) + 1;
        for (int i = 0; i < n; i++) {
            map[nums[i]]++;
            if (map[nums[i]] == min)
                ls.push_back(nums[i]);

            if (ls.size() == 2)
                break;
        }

        sort(ls.begin(), ls.end());
        return ls;
    }
};