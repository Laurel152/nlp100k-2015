#! /bin/bash
diff <(cut -f1 hightemp.txt) col1.txt
diff <(cut -f2 hightemp.txt) col2.txt
