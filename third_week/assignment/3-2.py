def generate_permutations(nums, path, visited):
    if len(path) == len(nums):
        print(path)
        return

    for i in range(len(nums)):
        if not visited[i]:
            visited[i] = True
            generate_permutations(nums, path + [nums[i]], visited)
            visited[i] = False

nums = [1, 2, 3]
visited = [False] * len(nums)

generate_permutations(nums, [], visited)


# 더 간단한 버전....대박

def permute(nums, path=[]):
    # 모든 숫자를 사용한 경우, 순열 출력 후 종료
    if not nums:
        print(path)
        return

    # 남은 숫자 중 하나를 선택하고, 선택한 숫자를 제외한 리스트로 재귀 호출
    for i in range(len(nums)):
        permute(nums[:i] + nums[i + 1:], path + [nums[i]])


# 순열 생성 함수 호출
permute([1, 2, 3])

