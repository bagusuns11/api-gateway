API-GATEWAY-Project
API Gateway (Kong) + Prometheus + Loki + Promtail + Grafana

# Cara install :
- copy repo project
git clone https://github.com/bagusuns11/api-gateway.git

- edit file docker-compose.yml ganti pada bagian service kong :
      # penting: GUI diarahkan ke proxy nginx
      - KONG_ADMIN_GUI_URL=http://<ip_host_docker>:8080
      - KONG_ADMIN_API_URL=http://<ip_host_docker>:8080/admin/
ganti <ip_host_docker> dengan IP Host docker

- kemudian jalankan :
docker compose up --build -d


# Cara tes API

- akse langsung ke app (dari host docker)

curl -i http://localhost:5000/api/akademik/students
curl -i http://localhost:5001/api/kepegawaian/employees

- akses dari API Gateway
Test 100 request, 5 concurrent 
ab -n 100 -c 5 http://<ip_host_docker>:8080/akademik/api/akademik/students
ab -n 100 -c 5 http://<ip_host_docker>:8080/kepegawaian/api/kepegawaian/employees
