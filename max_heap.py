def is_max_heap(arr):
    n = len(arr)
    for i in range((n - 2) // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False
    return True

def is_max_heap_bfs(root):
    if root is None:
        return True
    queue = [root]
    should_be_leaf = False
    while len(queue) > 0:
        current = queue.pop(0)
        if current.left:
            if should_be_leaf or current.left.data > current.data:
                return False
            queue.append(current.left)
        else:
            should_be_leaf = True
        if current.right:
            if should_be_leaf or current.right.data > current.data:
                return False
            queue.append(current.right)
        else:
            should_be_leaf = True
    return True
