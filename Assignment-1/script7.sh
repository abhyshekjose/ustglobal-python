add() {
    echo "Result: $((a + b))"
}

subtract() {
    echo "Result: $((a - b))"
}

multiply() {
    echo "Result: $((a * b))"
}

divide() {
    if [ $b -eq 0 ]; then
        echo "Division by zero is not allowed"
    else
        echo "Result: $((a / b))"
    fi
}

while true
do
    echo " "
    echo " Menu Driven Calculator"
    echo " "
    echo "1. Addition"
    echo "2. Subtraction"
    echo "3. Multiplication"
    echo "4. Division"
    echo "5. Exit"
    echo "Enter your choice:"
    read choice

    case $choice in
        1)
            echo "Enter two numbers:"
            read a b
            add
            ;;
        2)
            echo "Enter two numbers:"
            read a b
            subtract
            ;;
        3)
            echo "Enter two numbers:"
            read a b
            multiply
            ;;
        4)
            echo "Enter two numbers:"
            read a b
            divide
            ;;
        5)
            echo "Exiting calculator... Bye "
            break
            ;;
        *)
            echo "Invalid choice. Try again!"
            ;;
    esac
done

