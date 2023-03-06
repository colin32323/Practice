class Solution():
    def noConseBits(self, n: int) -> int:
        # code here
        binary = str(bin(n))[2:]
        while '111' in binary:
            n -= 1
            binary = str(bin(n))[2:]
        return n


if __name__ == '__main__':
    sol = Solution()
    num = 59
    print(sol.noConseBits(num))
    print(str(bin(sol.noConseBits(num)))[2:])
    print(str(bin(51))[2:])
    print(str(bin(59))[2:])
