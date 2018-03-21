BEGIN { 
    word = ""
    count = 0 
}{
    if ($1 == word) {
        count += $2
    } else {
        if (word != "") {
            print word, count
        }
        word = $1
        count = $2
    }
}
