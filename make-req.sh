for i in {1..10}
do
    echo "$(http GET $1 | jq -r .user_id)"
    sleep 1
done
