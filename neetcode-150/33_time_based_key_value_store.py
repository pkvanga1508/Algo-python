# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
#
# Implement the TimeMap class:
#
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
#
#
# Example 1:
#
# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]
#
# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"
#
#
# Constraints:
#
# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 107
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 105 calls will be made to set and get.


class TimeMap:

    def __init__(self):
        self.time_map = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            map_value = self.time_map[key]
            map_value.append([value, timestamp])
            self.time_map[key] = map_value
        else:
            self.time_map[key] = [[value, timestamp]]


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        else: #Binay search the key based on timestamp
            values = self.time_map[key]
            result = ""
            start = 0
            end = len(values) - 1
            while start <= end:
                mid = (start + end) // 2
                print(values[mid][1])
                if values[mid][1] == timestamp:
                    return values[mid][0]
                elif values[mid][1] < timestamp:
                    result = values[mid][0] #We need to get the value that is lower than the current timestamp
                    start = mid + 1
                else:
                    end = mid - 1
            return result




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)