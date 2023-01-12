Wyświetlanie wykresu funkcji równania kwadratowego. 
Endpoint przyjmuje (w url) następujące parametry:
- a, b, c: parametry równania y = ax2 + bx + c
- xmin, xmax, ymin, ymax: graniczne wartości obszaru wykresu do wyświetlenia

Przykładowy adres url:
http://localhost:5000/?a=1&b=0&c=0&xmin=-5&xmax=5&ymin=-1&ymax=10

Build image:
docker build -t docker_quadratic_function_app:v1.0 .

Run container:
docker run --rm -it -p 5000:5000 docker_quadratic_function_app:v1.0

Remove image:
docker image rm docker_quadratic_function_app:v1.0
