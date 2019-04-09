
#   Hungry Rabbit

#There is a rabbit that starts in the middle of an n x m matrix, n > 0, m > 0.
# Each element of a matrix is an integer representing points gained for being on the spot.
# If there are multiple possible "middles" then choose the one which has the highest point value to start on.
# On each iteration, the rabbit can move up, left, right, or down.
# The rabbit will always move to the next spot with the highest point value and will "consume" those points
# (set the point value in that position to 0). The rabbit spots when all positions around it are 0s.
# Calculate how many points the rabbit will score for a given m x n matrix.

#Input

#5, 7, 8, 6, 3 0, 0, 7, 0, 4 4, 6, 3, 4, 9 3, 1, 0, 5, 8

#Output

#27


def hungry_rabbit(garden_matrix):
    if len(garden_matrix) == 0:
        return 0

    #make a copy of garden_matrix
    copy = [g_row[:] for g_row in garden_matrix]
    row, column = get_center(copy)

    return get_carrot_count(copy, row, column)


def get_center(garden_matrix):
    # finding center index's of matrix for row and column
    row_centers = [len(garden_matrix) // 2, len(garden_matrix) // 2]
    column_centers = [len(garden_matrix[0]) // 2, len(garden_matrix[0]) // 2]

    # Even case: needs to be 1 less on first index
    if len(garden_matrix) % 2 == 0:
        row_centers[0] -= 1

    if len(garden_matrix[0]) % 2 == 0:
        column_centers[0] -= 1

    max_count = 0
    column = None
    row = None

    # iterate through to find max_count of middle index's
    for row_center in row_centers:
        for column_center in column_centers:
            if garden_matrix[row_center][column_center] > max_count:
                max_count = garden_matrix[row_center][column_center]
                row = row_center
                column = column_center

    return row, column



def get_carrot_count(garden_matrix, row, column):
    max_count = 0
    next_row = None
    next_column = None

    #iterating through surrounding index's to find largest carrot count and set next row and column
    for row_option, column_option in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if row + row_option >= 0 and row + row_option < len(garden_matrix) and \
                column + column_option >= 0 and column + column_option < len(garden_matrix[row]):
            if garden_matrix[row + row_option][column + column_option] > max_count:
                max_count = garden_matrix[row + row_option][column + column_option]
                next_row = row + row_option
                next_column = column + column_option

    # adding current carrot count
    carrot_count = garden_matrix[row][column]
    # setting current index to zero to avoid repeating same number
    garden_matrix[row][column] = 0

    #using recursion to calculate carrot count
    if next_row is not None and next_column is not None:
        carrot_count += get_carrot_count(garden_matrix, next_row, next_column)

    return carrot_count


if __name__ == "__main__":
    garden_matrix = [
        [5, 7, 8, 6, 3],
        [0, 0, 7, 0, 4],
        [4, 6, 3, 4, 9],
        [3, 1, 0, 5, 8]
    ]

    print(hungry_rabbit(garden_matrix))
