class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l = 0
        r = len(A)

        while True:
            i = (l + r) // 2
            j = half - i

            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")

            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:

                if total % 2:
                    return min(Aright, Bright)

                leftMax = max(Aleft, Bleft)
                rightMin = min(Aright, Bright)

                return (leftMax + rightMin) / 2

            elif Aleft > Bright:
                r = i - 1

            else:
                l = i + 1       