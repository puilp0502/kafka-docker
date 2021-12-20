for I in {1..3}; do
	printf "Removing"
	docker compose exec kafka-0$I tc qdisc delete dev eth0 root netem
	printf "Adding"
	docker compose exec kafka-0$I tc qdisc add dev eth0 root netem delay 5ms
done

