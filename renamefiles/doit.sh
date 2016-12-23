#f1 -> f1
#f2.txt -> f2-v1.txt
#f2-v1.txt -> f2-v1-v1.txt
#f2-v1-v1.txt -> f2-v1-v1-v1.txt
#foo.bar -> foo-v1.bar
#foo.bar.baz -> foo.bar-v1.baz
#.
#.
#.

SOURCE_DIR="src"
DEST_DIR="dest"
FILLER="v1"

# in real case, this list should come from ls
FILES="f1 f2.txt f2-v1.txt f2-v1-v1.txt foo.bar foo.bar.baz"

for file in $FILES; do
    echo $file
    if [[ $file =~ (.*)\.(.*) ]]; then
#        echo "  $file contains ."
        filebase="${BASH_REMATCH[1]}"
        fileext="${BASH_REMATCH[2]}"
        echo "    $filebase $fileext"
        newfile="${filebase}-${FILLER}.${fileext}"
    else
        newfile=$file
    fi

    # if file has no extension, leave it alone
    if [[ "$newfile" == "$file" ]];then
        echo "   $newfile has no extension, so noop."
    # if newfile exists in source_dir, move it to dest_dir
    elif [[ -e "$newfile" ]]; then
        echo "    moving newfile: $newfile from $SOURCE_DIR to $DEST_DIR"
    # else just rename file to newfile
    else
        echo "    renaming $file to $newfile"
    fi
done

# when done
# mv all files from DEST_DIR to SOURCE_DIR
# then rmdir DEST_DIR

