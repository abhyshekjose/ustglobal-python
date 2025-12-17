check_number() {
    if [ "$1" -gt 0 ]; then
        echo "The number is Positive"
    elif [ "$1" -lt 0 ]; then
        echo "The number is Negative"
    else
        echo "The number is Zero"
    fi
}

echo "Enter a number:"
read num

check_number "$num"
