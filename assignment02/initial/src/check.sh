#! /bin/sh
TESTCASES_DIR="./test/testcases/"
SOLUTIONS_DIR="./test/solutions/"
dir_lst=($TESTCASES_DIR
    $SOLUTIONS_DIR)

for dir in "${dir_lst[@]}"; do
    # echo "$dir"
    if [ ! -d "$dir" ]; then
        echo "Directory $dir DOES NOT exists. Making one"
        mkdir -p "$dir"
    fi
done

python3 run.py gen
# python3 run.py test LexerSuite
# python3 run.py test ParserSuite
python3 run.py test ASTGenSuite
