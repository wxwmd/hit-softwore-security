import numpy as np


class CommonSubsqquence:

    def __init__(self, str1: str, str2: str):
        self.s1 = str1
        self.s2 = str2
        self.d = np.zeros(shape=[len(self.s1), len(self.s2)], dtype=int)
        self.longst_common_subsequences = set()

    def longest_common_subsequence_length(self) -> int:
        """
        两个字符串s1,s2之间的最长公共子串的长度
        :param s1: 字符串1
        :param s2: 字符串2
        :return: 最长子串长度
        :rtype int
        """
        len1 = len(self.s1)
        len2 = len(self.s2)

        if self.s1[0] == self.s2[0]:
            self.d[0][0] = 1
        for i in range(1, len1, 1):
            if self.s1[i] != self.s2[0] and self.d[i - 1][0] == 0:
                self.d[i][0] = 0
            else:
                self.d[i][0] = 1
        for j in range(1, len2, 1):
            if self.s2[j] != self.s1[0] and self.d[0][j - 1] == 0:
                self.d[0][j] = 0
            else:
                self.d[0][j] = 1

        for i in range(1, len1, 1):
            for j in range(1, len2, 1):
                length = max(self.d[i - 1][j], self.d[i][j - 1])
                if self.s1[i] == self.s2[j]:
                    length = self.d[i - 1][j - 1] + 1
                self.d[i][j] = length

        return self.d[len1 - 1][len2 - 1]

    def get_common_sequences(self, suffix: str, x_index: int, y_index: int) -> set:
        """
        深度优先获取公共子串
        :param suffix: 后缀
        :param x_index: 从d[x,y]向前回溯
        :param y_index: 从d[x,y]向前回溯
        :return: 包含所有公共子序列的列表
        """
        self.longest_common_subsequence_length()
        if self.d[x_index][y_index] == 0:
            self.longst_common_subsequences.add(suffix)
        if x_index > 0 and self.d[x_index][y_index] == self.d[x_index - 1][y_index]:
            self.get_common_sequences(suffix, x_index - 1, y_index)
        if y_index > 0 and self.d[x_index][y_index] == self.d[x_index][y_index - 1]:
            self.get_common_sequences(suffix, x_index, y_index - 1)
        if x_index > 0 and y_index > 0 and self.d[x_index][y_index] == self.d[x_index - 1][y_index - 1] + 1 and self.s1[
            x_index] == self.s2[y_index]:
            suffix = self.s1[x_index] + suffix
            self.get_common_sequences(suffix, x_index - 1, y_index - 1)
        if x_index > 0 and y_index == 0 and self.d[x_index][y_index] == 1 and self.d[x_index - 1][y_index] == 0:
            suffix = self.s1[x_index] + suffix
            self.get_common_sequences(suffix, x_index - 1, y_index)
        if x_index == 0 and y_index > 0 and self.d[x_index][y_index] == 1 and self.d[x_index][y_index - 1] == 0:
            suffix = self.s2[y_index] + suffix
            self.get_common_sequences(suffix, x_index, y_index - 1)
        if x_index == 0 and y_index == 0 and self.d[x_index][y_index]==1:
            suffix = self.s1[0] + suffix
            self.longst_common_subsequences.add(suffix)
        return self.longst_common_subsequences

    def get_longest_common_sequences(self):
        return self.get_common_sequences('', len(self.s1) - 1, len(self.s2) - 1)


c = CommonSubsqquence('daebfc', 'adbecf')
print(c.get_longest_common_sequences())
