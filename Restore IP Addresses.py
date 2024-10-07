class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(segment: str) -> bool:
            segment_length = len(segment)
            if (segment_length > 3):
                return False
            return int(segment) <= 255 if segment[0] != "0" else len(segment) == 1

        def update_segment(
            s: str, curr_dot: int, segments: List[str], result: List[str]):
            segment = s[curr_dot + 1 : len(s)]
            if valid(segment):
                segments.append(segment)
                result.append(".".join(segments))
                segments.pop()

        def backtrack(
            s: str, prev_dot: int, dots: int, segments: List[str], result: List[str]):
            size = len(s)
            for curr_dot in range(prev_dot + 1, min(size - 1, prev_dot + 4)):
                segment = s[prev_dot + 1 : curr_dot + 1]
                if valid(segment):
                    segments.append(segment)
                    if dots - 1 == 0:
                        update_segment(s, curr_dot, segments, result)
                    else:
                        backtrack(s, curr_dot, dots - 1, segments, result)
                    segments.pop()
        result, segments = [], []
        backtrack(s, -1, 3, segments, result)
        return result
