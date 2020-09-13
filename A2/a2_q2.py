

def check_teams(graph, csp_sol):
    
    for i in range(len(graph)):

        for j in range(len(graph)):

            if csp_sol[i] == csp_sol[j] and j in graph[i] :

                return False
            
    return True

# Solution={0: 4, 1: 2, 2: 1, 3: 2, 4: 1, 5: 2, 6: 5, 7: 5, 8: 2, 9: 0, 10: 3, 11: 0, 12: 1, 13: 1, 14: 0, 15: 1, 16: 1, 17: 5, 18: 5, 19: 4, 20: 0, 21: 4, 22: 0, 23: 0, 24: 2, 25: 4, 26: 5, 27: 1, 28: 5, 29: 2, 30: 0, 31: 4, 32: 4, 33: 3, 34: 0, 35: 2, 36: 4, 37: 4, 38: 0, 39: 3, 40: 0, 41: 0, 42: 1, 43: 0, 44: 4, 45: 5, 46: 1, 47: 4, 48: 5, 49: 2, 50: 3, 51: 5, 52: 4, 53: 3, 54: 1, 55: 3, 56: 2, 57: 5, 58: 3, 59: 4, 60: 0, 61: 5, 62: 3, 63: 2, 64: 3, 65: 1, 66: 2, 67: 2, 68: 3, 69: 2, 70: 4, 71: 4, 72: 1, 73: 0, 74: 4, 75: 2, 76: 2, 77: 1, 78: 5, 79: 1, 80: 5, 81: 1, 82: 3, 83: 4, 84: 1, 85: 3, 86: 4, 87: 3, 88: 3, 89: 0, 90: 0, 91: 0, 92: 5, 93: 1, 94: 2, 95: 2, 96: 3, 97: 4, 98: 2, 99: 5, 100: 4, 101: 4, 102: 0, 103: 2, 104: 4}
# graph={0: [4, 14, 33, 63, 69, 78, 89], 1: [15, 18, 23, 32, 39, 44, 47, 50, 58, 71], 2: [6, 20, 38, 44, 49, 71], 3: [21, 34, 38, 42, 55, 59, 80, 81], 4: [0, 5, 11, 21, 37, 43, 66, 67, 92, 98, 99], 5: [4, 7, 16, 22, 37, 38, 50, 68, 70, 81, 92], 6: [2, 14, 16, 19, 21, 30, 37, 47, 58, 71, 73, 74, 88, 91, 94, 100], 7: [5, 8, 19, 23, 24, 27, 54, 71, 76, 82, 94], 8: [7, 12, 21, 26, 31, 33, 42, 48, 51, 57, 79], 9: [24, 28, 65, 74, 81, 82, 94, 99, 103], 10: [13, 14, 27, 29, 51, 65, 66, 67, 72], 11: [4, 19, 35, 37, 55, 59, 64, 80, 81, 83], 12: [8, 18, 22, 23, 26, 49, 59, 63, 68, 86, 90, 96], 13: [10, 14, 21, 24, 57, 59, 63, 74, 85, 89], 14: [0, 6, 10, 13, 19, 37, 39, 57, 61, 68, 78, 88], 15: [1, 25, 32, 37, 38, 50, 52, 57, 61, 71, 80, 83, 104], 16: [5, 6, 20, 36, 38, 43, 63, 68, 76, 78, 86, 99, 103], 17: [19, 25, 47, 77, 97], 18: [1, 12, 21, 35, 40, 54, 64, 82, 88, 104], 19: [6, 7, 11, 14, 17, 20, 29, 42, 58, 78, 80, 82, 91], 20: [2, 16, 19, 26, 58, 62, 68, 86, 94], 21: [3, 4, 6, 8, 13, 18, 38, 51, 54, 68, 73, 91], 22: [5, 12, 51, 53, 58, 65, 77, 86, 97], 23: [1, 7, 12, 24, 29, 39, 72, 75, 104], 24: [7, 9, 13, 23, 41, 43, 50, 54, 55, 65, 68, 77, 78], 25: [15, 17, 29, 33, 41, 62, 73, 91, 94], 26: [8, 12, 20, 72, 83], 27: [7, 10, 34, 44, 56, 60, 67, 68], 28: [9, 30, 70, 74, 75, 93, 95, 96, 98], 29: [10, 19, 23, 25, 30, 34, 52, 62, 71, 77, 80, 82, 100, 104], 30: [6, 28, 29, 46, 51, 52, 61, 63, 68, 70, 74, 78, 86, 88, 93, 98], 31: [8, 57, 63, 66, 67, 75, 78, 103], 32: [1, 15, 51, 54, 68, 77], 33: [0, 8, 25, 43, 45, 61, 63, 71, 81, 101, 104], 34: [3, 27, 29, 53, 64, 81, 84, 95], 35: [11, 18, 38, 40, 41, 51, 54, 55, 57, 62, 68, 104], 36: [16, 58, 62, 79, 84, 90, 99, 103], 37: [4, 5, 6, 11, 14, 15, 48, 58, 72, 89], 38: [2, 3, 5, 15, 16, 21, 35, 47, 48, 49, 56, 61, 62, 65, 66, 87, 93, 95], 39: [1, 14, 23, 42, 47, 51, 63, 69, 71, 77, 97], 40: [18, 35, 52, 59, 72, 76, 80], 41: [24, 25, 35, 50, 64, 69, 71], 42: [3, 8, 19, 39, 57, 62, 66, 73, 76, 85, 91, 94], 43: [4, 16, 24, 33, 44, 53, 54, 59, 82, 88, 93], 44: [1, 2, 27, 43, 58, 65, 77, 90, 93, 98], 45: [33, 46, 52, 70, 89, 90, 97, 100, 103], 46: [30, 45, 61, 67, 73, 89, 90], 47: [1, 6, 17, 38, 39, 72, 77, 78, 92, 96], 48: [8, 37, 38, 52, 64, 68, 69, 76, 77], 49: [2, 12, 38, 54, 72, 88, 104], 50: [1, 5, 15, 24, 41, 57, 65, 72, 83, 92], 51: [8, 10, 21, 22, 30, 32, 35, 39, 58, 65, 72, 76, 85], 52: [15, 29, 30, 40, 45, 48, 61, 67, 78, 94], 53: [22, 34, 43, 61, 78, 97, 98, 99, 102], 54: [7, 18, 21, 24, 32, 35, 43, 49], 55: [3, 11, 24, 35, 77, 78, 104], 56: [27, 38, 64, 93], 57: [8, 13, 14, 15, 31, 35, 42, 50, 67, 73, 75, 86, 87, 89, 95], 58: [1, 6, 19, 20, 22, 36, 37, 44, 51, 73, 79, 81, 97, 98, 100, 102], 59: [3, 11, 12, 13, 40, 43, 63, 67, 69, 80, 81, 90, 96], 60: [27, 68, 74, 84, 85, 88, 97, 101], 61: [14, 15, 30, 33, 38, 46, 52, 53, 67, 77, 94, 102, 103], 62: [20, 25, 29, 35, 36, 38, 42, 74, 75, 89], 63: [0, 12, 13, 16, 30, 31, 33, 39, 59, 70, 71, 73, 90, 102], 64: [11, 18, 34, 41, 48, 56, 80, 89], 65: [9, 10, 22, 24, 38, 44, 50, 51, 70, 78, 80, 91, 96, 102], 66: [4, 10, 31, 38, 42, 85, 93, 96, 100], 67: [4, 10, 27, 31, 46, 52, 57, 59, 61, 73, 83], 68: [5, 12, 14, 16, 20, 21, 24, 27, 30, 32, 35, 48, 60], 69: [0, 39, 41, 48, 59, 84], 70: [5, 28, 30, 45, 63, 65, 99], 71: [1, 2, 6, 7, 15, 29, 33, 39, 41, 63, 76, 82, 84, 91], 72: [10, 23, 26, 37, 40, 47, 49, 50, 51, 74, 82, 87, 103, 104], 73: [6, 21, 25, 42, 46, 57, 58, 63, 67], 74: [6, 9, 13, 28, 30, 60, 62, 72, 82], 75: [23, 28, 31, 57, 62, 92, 99], 76: [7, 16, 40, 42, 48, 51, 71, 83, 84, 88, 96, 102], 77: [17, 22, 24, 29, 32, 39, 44, 47, 48, 55, 61, 82, 83], 78: [0, 14, 16, 19, 24, 30, 31, 47, 52, 53, 55, 65, 79, 83, 88, 89, 93, 100, 103, 104], 79: [8, 36, 58, 78, 94, 100], 80: [3, 11, 15, 19, 29, 40, 59, 64, 65, 86, 90, 98, 100], 81: [3, 5, 9, 11, 33, 34, 58, 59, 82, 87], 82: [7, 9, 18, 19, 29, 43, 71, 72, 74, 77, 81, 84, 92], 83: [11, 15, 26, 50, 67, 76, 77, 78, 89], 84: [34, 36, 60, 69, 71, 76, 82, 97, 98], 85: [13, 42, 51, 60, 66, 91, 94], 86: [12, 16, 20, 22, 30, 57, 80, 90, 96, 98], 87: [38, 57, 72, 81, 97], 88: [6, 14, 18, 30, 43, 49, 60, 76, 78, 98], 89: [0, 13, 37, 45, 46, 57, 62, 64, 78, 83, 96, 100], 90: [12, 36, 44, 45, 46, 59, 63, 80, 86], 91: [6, 19, 21, 25, 42, 65, 71, 85, 94], 92: [4, 5, 47, 50, 75, 82, 95], 93: [28, 30, 38, 43, 44, 56, 66, 78], 94: [6, 7, 9, 20, 25, 42, 52, 61, 79, 85, 91, 97, 99, 101, 102], 95: [28, 34, 38, 57, 92, 102], 96: [12, 28, 47, 59, 65, 66, 76, 86, 89, 97, 103], 97: [17, 22, 39, 45, 53, 58, 60, 84, 87, 94, 96], 98: [4, 28, 30, 44, 53, 58, 80, 84, 86, 88, 104], 99: [4, 9, 16, 36, 53, 70, 75, 94, 104], 100: [6, 29, 45, 58, 66, 78, 79, 80, 89], 101: [33, 60, 94], 102: [53, 58, 61, 63, 65, 76, 94, 95, 103], 103: [9, 16, 31, 36, 45, 61, 72, 78, 96, 102], 104: [15, 18, 23, 29, 33, 35, 49, 55, 72, 78, 98, 99]}
# print(len(Solution))
# print(len(graph))
# print(check_teams(graph,Solution))