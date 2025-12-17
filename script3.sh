sum_numbers() {
    n=$1
    sum=0

    for (( i=1; i<=n; i++ ))
    do
        sum=$((sum + i))
    done

    echo "Sum of numbers from 1 to $n is: $sum"
}

echo "Enter the value of N:"
read num

sum_numbers $num
