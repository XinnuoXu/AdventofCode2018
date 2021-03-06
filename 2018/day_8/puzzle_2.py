#coding=utf8

if __name__ == '__main__':
    tree = [int(item) for item in open("test.txt").readline().strip().split(" ")]
    stack = []; idx = 0; metadata_sum = 0
    while idx < len(tree) - 1:
        while len(stack) > 0:
            s = stack.pop()
            if s[0] > 0:
                s[0] -= 1
                s[2].append(metadata_sum)
                stack.append(s)
                metadata_sum = 0
                break
            start = idx
            metadata = s[1]
            s[2].append(metadata_sum)
            metadata_sum = 0
            while idx < start + metadata:
                if tree[idx] < len(s[2]):
                    metadata_sum += s[2][tree[idx]]
                idx += 1
        if idx >= len(tree):
            break
        if tree[idx] != 0:
            stack.append([tree[idx], tree[idx + 1], []])
            metadata_sum = 0
            idx += 2
            continue
        else:
            metadata = tree[idx + 1]
            idx += 2
            start = idx
            while idx < start + metadata:
                metadata_sum += tree[idx]
                idx += 1
    print (metadata_sum)
