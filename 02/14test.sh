#! /bin/bash
diff <(head -5 hightemp.txt) <(python 14.py 5)
diff <(head -15 hightemp.txt) <(python 14.py 15)
diff <(head -100 hightemp.txt) <(python 14.py 100)
