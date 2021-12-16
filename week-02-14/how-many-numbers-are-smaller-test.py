def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
        indices = {}
        print(sorted(nums))
        for idx, num in enumerate(sorted(nums)):
            indices.setdefault(num, idx)
        return [indices[num] for num in nums]

print(smallerNumbersThanCurrent([4,2,1,1,3,5]))