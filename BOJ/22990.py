class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_level_order(arr, root, i, n):
    # 완전 이진트리에 메시지를 순서대로 삽입
    if i < n:
        temp = TreeNode(arr[i])
        root = temp

        # 왼쪽 자식 삽입
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)

        # 오른쪽 자식 삽입
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)

    return root

def post_order_traversal(root, result):
    # 후위 순회
    if root:
        post_order_traversal(root.left, result)
        post_order_traversal(root.right, result)
        result.append(root.value)

def encrypt_message(message):
    n = len(message)
    if n == 0:
        return ""

    # 메시지를 리스트로 변환
    arr = list(message)
    root = insert_level_order(arr, None, 0, n)

    # 후위 순회를 통해 암호화된 메시지를 생성
    result = []
    post_order_traversal(root, result)

    return ''.join(result)

# 사용 예시
message = "abcdefghijk"
encrypted_message = encrypt_message(message)
print("암호화된 메시지:", encrypted_message)
