def chessBoardCellColor(cell1, cell2):
    return int(cell1[1])%2 ^ int(cell2[1])%2 == ord(cell1[0])%2 ^ ord(cell2[0])%2

