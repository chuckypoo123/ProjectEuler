def num_rect(width, height):
    total = 0
    for in_rect_w in range(1, width + 1):
        for in_rect_h in range(1, height + 1):
            total += (width - in_rect_w + 1) * (height - in_rect_h + 1)

    return total

def rect_with_inside_rect(inside_target):
    closest = inside_target
    sizes = []

    for max_side in range(1, 200):
        for w in range(1, max_side + 1):
            rects = num_rect(w, max_side)
            diff = abs(inside_target - rects)
            if  diff < closest:
                closest = diff
                sizes = [[w, max_side]]
            elif diff == closest:
                sizes.append(w, max_side)

            # No need to calculate with h because all the one with w are symmetrical

    return [closest, sizes]

if __name__ == "__main__":
    # print(num_rect(1, 10000))
    # print(rect_with_inside_rect(2000000))
    print(36 * 77)
