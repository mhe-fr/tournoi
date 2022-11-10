import itertools

a = [
[[[12, 1], [2, 11]], [[3, 10], [4, 9]], [[5, 8], [6, 7]]],
[[[12, 7], [8, 6]], [[9, 5], [10, 4]], [[11, 3], [1, 2]]],
[[[12, 2], [3, 1]], [[4, 11], [5, 10]], [[6, 9], [7, 8]]],
[[[12, 8], [9, 7]], [[10, 6], [11, 5]], [[1, 4], [2, 3]]],
[[[12, 3], [4, 2]], [[5, 1], [6, 11]], [[7, 10], [8, 9]]],
[[[12, 9], [10, 8]], [[11, 7], [1, 6]], [[2, 5], [3, 4]]],
[[[12, 4], [5, 3]], [[6, 2], [7, 1]], [[8, 11], [9, 10]]],
[[[12, 10], [11, 9]], [[1, 8], [2, 7]], [[3, 6], [4, 5]]],
[[[12, 5], [6, 4]], [[7, 3], [8, 2]], [[9, 1], [10, 11]]],
[[[12, 11], [1, 10]], [[2, 9], [3, 8]], [[4, 7], [5, 6]]],
[[[12, 6], [7, 5]], [[8, 4], [9, 3]], [[10, 2], [11, 1]]]
]

b = [[[12, 1], [[2, 11], [3, 10], [4, 9], [5, 8], [6, 7]]], [[12, 7], [[8, 6], [9, 5], [10, 4], [0, 3], [1, 2]]], [[12, 2], [[3, 1], [4, 0], [5, 10], [6, 9], [7, 8]]], [[12, 8], [[9, 7], [10, 6], [0, 5], [1, 4], [2, 3]]], [[12, 3], [[4, 2], [5, 1], [6, 0], [7, 10], [8, 9]]], [[12, 9], [[10, 8], [0, 7], [1, 6], [2, 5], [3, 4]]], [[12, 4], [[5, 3], [6, 2], [7, 1], [8, 0], [9, 10]]], [[12, 10], [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]], [[12, 5], [[6, 4], [7, 3], [8, 2], [9, 1], [10, 0]]], [[12, 0], [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]], [[12, 6], [[7, 5], [8, 4], [9, 3], [10, 2], [0, 1]]]]

class MatchGrid:
    def __init__(self, size):
        self.grid = []
        if size % 2 == 1:
            self.size = size + 1
        else:
            self.size = size

    def populate(self, data):
        for i in range(self.size):
            row = []
            for j in range(self.size//2 - 1):
                row.append([data, data])
            self.grid.append(row)

    def sort_grid(self):
        for round in self.grid:
            for match in round:
                # if isinstance(match[0], list):
                #     match[0].sort(reverse=True)
                #     match[1].sort(reverse=True)
                match.sort(reverse=True)
            round.sort(reverse=True)
        self.grid.sort(reverse=True)

    def substitution(self, vector):
        for round in self.grid:
            for match in round:
                match[0] = vector[match[0]-1]
                match[1] = vector[match[1]-1]

    def gen_berger(self):
        k = 1
        for i in range(self.size-1):
            if i % 2 == 0:
                self.grid.append([[self.size, k]])
            else:
                self.grid.append([[self.size, k + self.size//2]])
                k += 1
        n1, n2 = 1, self.size - 2
        for i in range(self.size - 1):
            row = []
            for j in range(self.size//2 - 1):
                row.append([n1 + 1, n2 + 1])
                n1 = (n1 + 1) % (self.size-1)
                n2 = (n2 - 1) % (self.size-1)

            n1 = (n1 + 1) % (self.size - 1)
            self.grid[i].extend(row)
        return

    def rate_grid_simple(self):
        score = 0
        match_list = []
        for j in range(len(self.grid)):
            round = self.grid[j]
            round_player = []
            for match in round:
                # each player play no more than once per round
                for k in (0, 1):
                    if match[k] in round_player:
                        score += 1
                    else:
                        round_player.append(match[k])
                # each player meet once another player
                if match[0] > match[1]:
                    if match in match_list:
                        score += 1
                    else:
                        match_list.append(match)
                else:
                    if [match[1], match[0]] in match_list:
                        score += 1
                    else:
                        match_list.append([match[1], match[0]])
        return score


    def rate_grid_double(self, grid2):
        score = 0
        partner_list = []
        opponent_list = []
        for j in range(len(grid2)):
            for i in range(len(grid2[j])):
                # each player of grid1 play once with a player of grid2
                for k in (0, 1):
                    a = [self.grid[j][i][k], grid2[j][i][k]]
                    if a in partner_list:
                        score += 1
                    else:
                        partner_list.append(a)
                    a = [self.grid[j][i][k], grid2[j][i][1-k]]
                    if a in opponent_list:
                        score += 1
                    else:
                        opponent_list.append(a)
        return score


grid_a = MatchGrid(len(a))
grid_a.grid = a
grid_a.sort_grid()
print(grid_a.grid)
print(grid_a.rate_grid_simple())
n = 4
grid_b = MatchGrid(n)
grid_b.gen_berger()
print(grid_b.grid)
grid_b.sort_grid()
print(grid_b.grid)
print("rated : {}".format(grid_b.rate_grid_simple()))
print("rate_double{}".format(grid_b.rate_grid_double([[[4,3],[2,1]],[[2,4],[1,3]],[[3,2], [4,1]]] )))

def find_berger_subst():
    grid_list = []
    perm = itertools.permutations(range(1, n+1))
    grid_list.append(grid_b.grid)
    for i in perm:
        grid_b.substitution(i)
        grid_b.sort_grid()
        if grid_b.grid not in grid_list:
            grid_list.append(grid_b.grid)
        grid_b = MatchGrid(n)
        grid_b.gen_berger()
        grid_b.sort_grid()

    print(len(grid_list))

class Heap:
    def __init__(self, item_list):
        self.size = len(item_list)
        self.item_list = item_list
        self.level = 0
        self.prev_level = 0
        self.count = [0] * self.size

    def all(self):
        while self.level < self.size:
            if self.count[self.level] < self.level:
                if self.level % 2 == 0:
                    self.item_list[0], self.item_list[self.level] = self.item_list[self.level], self.item_list[0]
                else:
                    self.item_list[self.count[self.level]], self.item_list[self.level] = self.item_list[self.level], self.item_list[self.count[self.level]]
                self.count[self.level] += 1
                self.prev_level = self.level
                self.level = 0
                print(self.item_list, self.count, self.level)
            else:
                self.count[self.level] = 0
                self.prev_level = self.level
                self.level += 1
                print(self.count, self.level)
        self.level = 0

    def next(self):
        done = False
        while not done:
            if self.level >= self.size:
                self.prev_level = 1
                self.level = 0
                self.count = list(range(self.size))
                return done
            if self.count[self.level] < self.level:
                if self.level % 2 == 0:
                    self.item_list[0], self.item_list[self.level] = self.item_list[self.level], self.item_list[0]
                else:
                    self.item_list[self.count[self.level]], self.item_list[self.level] = \
                        self.item_list[self.level], self.item_list[self.count[self.level]]
                done = True
                self.count[self.level] += 1
                self.prev_level = self.level
                self.level = 0
            else:
                self.count[self.level] = 0
                self.prev_level = self.level
                self.level += 1
        return done

    def previous(self):
        done = False
        if self.prev_level == 0:
            return done
        while self.prev_level > 0:
            if self.count[self.prev_level] == 0:
                self.count[self.prev_level] = self.prev_level
            else: # self.count[self.level] <= self.level
                self.count[self.prev_level] -= 1
            if self.level == 0:
                done = True
                if self.prev_level % 2 == 0:
                    self.item_list[0], self.item_list[self.prev_level] = self.item_list[self.prev_level], self.item_list[0]
                else:
                    self.item_list[self.count[self.prev_level]], self.item_list[self.prev_level] = \
                        self.item_list[self.prev_level], self.item_list[self.count[self.prev_level]]
                self.level = self.prev_level
            self.prev_level -= 1
        self.level = 0
        while self.count[self.prev_level] == 0:
            self.prev_level += 1
            if self.prev_level >= self.size:
                self.prev_level = 0
                break
        return done





a = Heap(['A', 'B', 'C', 'D'])
a.all()
b = Heap(['A', 'B', 'C', 'D'])
for i in range(4):
    b.next()
    print(b.item_list)
for i in range(4):
    b.previous()
    # print(b.item_list)

while b.next():
     print(b.item_list)

print("previous")
while b.previous():
     print(b.item_list)

# add new match
def add_new_match(i,j):
    m1 = grid_a.grid[i][j]
    m2 = grid_b.grid[i][j]
    if swap[i*n + j] == 0:
        if same_partner[m1[0]][m2[0]] == 0 and same_partner[m1[1]][m2[1]] == 0\
                and same_opponent[m1[0]][m2[1]] == 0 and same_opponent[m1[1]][m2[0]] == 0:
            same_partner[m1[0]][m2[0]] += 1
            same_partner[m1[1]][m2[1]] += 1
            same_opponent[m1[0]][m2[1]] += 1
            same_opponent[m1[1]][m2[0]] += 1
            return True
    else:
        if same_partner[m1[0]][m2[1]] == 0 and same_partner[m1[1]][m2[0]] == 0\
                and same_opponent[m1[0]][m2[0]] == 0 and same_opponent[m1[1]][m2[1]] == 0:
            same_partner[m1[0]][m2[1]] += 1
            same_partner[m1[1]][m2[0]] += 1
            same_opponent[m1[0]][m2[0]] += 1
            same_opponent[m1[1]][m2[1]] += 1
            return True
    return False

def next_match():
    j += 1
    if j == (n // 2):
        j = 0
        i += 1
        swap.append(0)
        if i == n:
            return False
        else:
            perm_match.append(Heap(list(range(n // 2))))
            return True

def backward():
    swap[i * n + j] = 0
    j -= 1
    if j == 0:
        j = n//2
        i -= 1
        swap.pop()
        if i == -1:
            return False
        else:
            perm_match.pop()
            return True




n = 4
grid_a = MatchGrid(n)
grid_a.gen_berger()
grid_a.sort_grid()

grid_b = grid_a

iter = 0
# min_rate = 999
round_index = 0
match_index = 0

perm_round = Heap(list(range(n-1)))
round = perm_round.item_list[round_index]
perm_match = []
perm_match.append(Heap(list(range(n//2))))
swap = [0]

same_partner = [[0]*n for i in range(n)]
same_opponent = [[0]*n for i in range(n)]

i, j = 0, 0

while next_match():
    if not add_new_match(i,j):
        if swap[i*n + j] == 0:
            swap[i * n + j] = 1
            if not add_new_match(i,j):
                while swap[i * n + j] == 1:
                    backward()
                swap[i * n + j] = 1




# if good  add next match
# else add reverse match
#   if good add new match
#   else backward



# for round_order in perm_round:
#     perm_match = itertools.permutations(range(n//2))
#     for match_order in perm_match:
#         for permut in range(2**(n//2)):
#             test_grid =[]
#             for i in range(n-1):
#                 test_row = []
#                 for j in range(n//2):
#                     if permut & 2**j :
#                         test_row.append(grid_b.grid[round_order[i]][match_order[j]][::-1])
#                     else:
#                         test_row.append(grid_b.grid[round_order[i]][match_order[j]])
#                 test_grid.append(test_row)
#             rating = grid_b.rate_grid_double(test_grid)
#             print(rating, test_grid)
#             iter += 1
#             if rating < min_rate:
#                 min_rate = rating
#             if rating == 0:
#                 print("a good one {}".format(test_grid))
#
# print("min_rate = {} iter = {}".format(min_rate, iter))





