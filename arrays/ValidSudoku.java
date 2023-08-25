import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class ValidSudoku {

    public boolean isValidSudoku(char[][] board) {
        Map<Integer, List<Character>> tiles = new HashMap<>();

        for (int i = 0; i < board.length; i++) {
            Row r = new Row();
            Column c = new Column();

            for (int j = 0; j < board.length; j++) {
                int tile = determineTile(i, j);

                tiles.putIfAbsent(tile, new ArrayList<Character>());
                List<Character> current = tiles.get(tile);
                current.add(board[i][j]);
                tiles.put(tile, current);

                
                r.add(board[i][j]);
                c.add(board[j][i]);
            }

            if (!c.isValid() || !r.isValid()) {
                return false;
            }

        }

        for (Integer i : tiles.keySet()) {
            List<Character> chars = tiles.get(i);

            if (chars.stream().filter(c -> !c.equals('.')).filter(c -> chars.indexOf(c) != chars.lastIndexOf(c)).collect(Collectors.toList()).size() != 0) {
                return false;
            }
        }

        return true;
    }

    public int determineTile(int i, int j) {
        if (i >= 0 && i < 3 && j >= 0 && j < 3)  return 1;
        if (i >= 3 && i < 6 && j >= 0 && j < 3)  return 2;
        if (i >= 6 && i < 9 && j >= 0 && j < 3)  return 3;
        if (i >= 0 && i < 3 && j >= 3 && j < 6)  return 4;
        if (i >= 3 && i < 6 && j >= 3 && j < 6)  return 5;
        if (i >= 6 && i < 9 && j >= 3 && j < 6)  return 6;
        if (i >= 0 && i < 3 && j >= 6 && j < 9)  return 7;
        if (i >= 3 && i < 6 && j >= 6 && j < 9)  return 8;
        if (i >= 6 && i < 9 && j >= 6 && j < 9)  return 9;

        return -1;
    }
}



class Sudoku {
    private List<Character> chars = new ArrayList<>();

    public List<Character> getChars() {
        return chars;
    }

    public void add(Character c) {
        chars.add(c);
    }

    public boolean isValid() {
        return chars.stream().filter(c -> !c.equals('.')).filter(c -> chars.indexOf(c) != chars.lastIndexOf(c)).collect(Collectors.toList()).size() == 0;
    }


}
class Column extends Sudoku {

}

class Row extends Sudoku {

}
