class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_boxes = 0

        sorted_capacity = sorted(capacity, reverse=True)
        apples_sum = sum(apple)
        
        for cap in sorted_capacity:
            if apples_sum <= 0:
                break

            apples_sum -= cap
            total_boxes += 1
        
        return total_boxes


